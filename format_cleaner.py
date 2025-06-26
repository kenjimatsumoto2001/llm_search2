#これはrun_openai.py or run_open_llm.pyでoutputされたものを整形するプログラム
#ollamaのllama3.3:latestを使用
import json
from ollama import Client
import os
"""""""③整形したいllmモデル選択"""""""""
# input_model = "deepseek-r1:70b"
input_model = "llama3.3:latest"
#input_model = "gemma3:27b"
"""""""②整形したいプロンプト選択"""""""""
# prompt_method_name = "zero_shot_cot"
# prompt_method_name = "few_shot_cot"
prompt_method_name = "zero_shot_cot_with_inference_process"
# prompt_method_name = "few_shot_cot_with_inference_process"
# prompt_method_name ="plan_and_solve"
"""""""③使用したいGPU"""""""""
os.environ["CUDA_VISIBLE_DEVICES"] = "3"

########################################################################
# メソッド名 → ファイル名のマッピング
filename_map = {
    "few_shot_cot_with_inference_process": "few_cot_infer",
    "few_shot_cot": "few_cot",
    "zero_shot_cot": "zero_cot",
    "zero_shot_cot_with_inference_process": "zero_cot_infer",
    "plan_and_solve":"plan_and_solve"
    # 必要に応じて他も追加可能
}
# モデル名を短縮名に変換
def extract_model_name(model_str):
    if "deepseek" in model_str.lower():
        return "deepseek"
    elif "llama" in model_str.lower():
        return "llama"
    elif "gemma" in model_str.lower():
        return "gemma"
    else:
        return "other"
#モデル名を変換
input_model_name = extract_model_name(input_model)

# 変換されたファイル名（短縮名がなければそのまま使う）
short_name = filename_map.get(prompt_method_name, prompt_method_name)


client = Client(
    host='http://localhost:11434',
    headers={'Content-Type': 'application/json'}
)

###################### 整形プロンプトの構築 ####################### 
def get_formatting_prompt(prompt_method_name: str, text: str) -> str:
    if prompt_method_name in ["zero_shot_cot"]:
        return f"""
---
{text}
---
Therefore, The answer is
   Recommend categories: ['Category_name', 'Category_name', ...]\n
   Recommend All matched APIs: ['API_name', 'API_name', ...]\n

"""
    

    elif prompt_method_name in ["few_shot_cot"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    
    elif prompt_method_name in ["few_shot_cot_with_inference_process"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    

    elif prompt_method_name in ["zero_shot_cot_with_inference_proces"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    

    elif prompt_method_name == "plan_and_solve":
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""

###################### LLMで整形 ####################### 
def format_text_with_model(text: str, prompt_method_name: str) -> str:
    system_message = {
        "role": "system",
        "content": "You are a system that extracts and formats structured recommendations from the input."
        "Only include the structured answer. Do not include explanations or additional commentary."
    }
    user_prompt = {
        'role': 'user',
        'content': get_formatting_prompt(prompt_method_name, text)
    }
    response = client.chat(model='llama3.3:latest', messages=[system_message, user_prompt])
    return response['message']['content']

###################### 逐次処理本体 ####################### 

def process_json_file_incremental(input_file: str, output_file: str, prompt_method_name: str):
    # 入力ファイル読み込み
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 出力ファイルが既に存在する場合、そこまでのデータを再利用
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            formatted_data = json.load(f)
    else:
        formatted_data = {}

    for i, (service_name, content) in enumerate(data.items(), start=1):
        if service_name in formatted_data:
            print(f"{i}件目 スキップ済: {service_name}")
            continue

        print(f"{i}件目 整形中: {service_name}")
        try:
            formatted_result = format_text_with_model(content, prompt_method_name)
            formatted_data[service_name] = formatted_result
        except Exception as e:
            print(f"{service_name} の整形に失敗しました: {e}")
            formatted_data[service_name] = content  # 失敗したら元のまま

        # 整形結果を1件ずつ保存
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, ensure_ascii=False, indent=2)

    print(f"整形完了: {output_file} に保存しました")

if __name__ == "__main__":
    input_path = f"./output/{input_model_name}/{short_name}/responses.json"
    output_path = f"./output/{input_model_name}/{short_name}/responses_formatted.json"
    print("整形するファイルパス", input_path)
    print("###########################################################")
    process_json_file_incremental(input_path, output_path, prompt_method_name)
