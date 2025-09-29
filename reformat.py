import os
import json
import re
import ast
from ollama import Client

# ===== 設定 =====
input_model = "gpt"  # ここを "deepseek" や "gpt" に変更可能
#llamaは完了
max_retries = 3
model="llama3.3:latest" #再整形のモデル 
# model='llama3.2:3b'

# ===== プロンプト手法とファイルマッピング =====
filename_map = {
    "zero_shot": "zero_shot",
    "zero_shot_cot": "zero_cot",
    "zero_shot_cot_with_inference_process": "zero_cot_infer",
    "few_shot": "few_shot",
    "few_shot_ablation": "few_shot_ablation",
    "few_shot_cot": "few_cot",
    "few_shot_cot_with_inference_process": "few_cot_infer",
    "plan_and_solve": "plan_and_solve"
}

expected_bracket_counts = {
    "few_shot_cot": 3,
    "few_shot_cot_with_inference_process": 3,
    "few_shot": 2,
    "few_shot_ablation": 3,
    "plan_and_solve": 3,
    "zero_shot_cot_with_inference_process": 3,
    "zero_shot_cot": 2,
    "zero_shot": 2
}

def extract_model_name(model_str):
    if "deepseek" in model_str.lower():
        return "deepseek"
    elif "llama" in model_str.lower():
        return "llama"
    elif "gemma" in model_str.lower():
        return "gemma"
    elif "gpt" in model_str.lower():
        return "gpt"
    else:
        return "other"

# ===== 整形プロンプト =====
def get_formatting_prompt(prompt_method_name: str, text: str) -> str:
    common = "---\n" + text + "\n---\nTherefore, The answer is\n"
    if prompt_method_name in ["few_shot_cot", "few_shot_cot_with_inference_process", 
                              "few_shot_ablation", "plan_and_solve", "zero_shot_cot_with_inference_process"]:
        return common + \
"""    Recommend categories: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n"""
    elif prompt_method_name in ["few_shot", "zero_shot"]:
        return common + \
"""    Recommend categories: ['Category_name', 'Category_name', ...]\n
    recommended APIs: ['API_name', 'API_name', ...]\n"""
    elif prompt_method_name in ["zero_shot_cot"]:
        return common + \
"""   Recommend categories: ['Category_name', 'Category_name', ...]\n
   Recommend All matched APIs: ['API_name', 'API_name', ...]\n"""
    else:
        raise ValueError(f"Unknown prompt method: {prompt_method_name}")

# ===== LLM呼び出し =====
client = Client(host='http://localhost:11434')

def format_text_with_model(text: str, prompt_method_name: str) -> str:
    system_message = {
        "role": "system",
        "content": "You are a system that extracts and formats structured recommendations from the input."
                   "Only include the structured answer. Do not include explanations or additional commentary."
    }
    user_prompt = {
        "role": "user",
        "content": get_formatting_prompt(prompt_method_name, text)
    }
    response = client.chat(model=model, messages=[system_message, user_prompt])
    return response["message"]["content"]

# ===== 整形チェック =====
def is_properly_formatted(response_text: str, prompt_method_name: str) -> bool:
    expected_count = expected_bracket_counts.get(prompt_method_name, 0)
    lists_in_brackets = re.findall(r"\[.*?\]", response_text)

    # リストの数が不足 or 空リスト含む
    if len(lists_in_brackets) < expected_count or any(item.strip() == "[]" for item in lists_in_brackets):
        return False

    # Ellipsis (...) 含む、または構文が壊れている
    for lst in lists_in_brackets:
        if "..." in lst:
            return False
        try:
            parsed = ast.literal_eval(lst)
            if not isinstance(parsed, list):
                return False
        except Exception:
            return False

    return True

# ===== 整形処理 =====
def reformat_all_entries(input_model_name, model_dir_path, max_retries):
    for prompt_method_name, short_name in filename_map.items():
        input_path = os.path.join(model_dir_path, short_name, "responses.json")
        output_path = os.path.join(model_dir_path, short_name, "responses_formatted.json")

        if not os.path.exists(input_path):
            print(f"🚫 入力ファイルが存在しません: {input_path}")
            continue

        with open(input_path, 'r', encoding='utf-8') as f:
            original_data = json.load(f)

        if os.path.exists(output_path):
            with open(output_path, 'r', encoding='utf-8') as f:
                formatted_data = json.load(f)
        else:
            formatted_data = {}

        incomplete_keys = []

        for key, value in original_data.items():
            if key in formatted_data:
                # 既に整形済み → それが不完全なら再整形対象
                if not is_properly_formatted(formatted_data[key], prompt_method_name):
                    incomplete_keys.append(key)
            else:
                # まだ整形されていないので追加
                incomplete_keys.append(key)

        print(f"\n📄 処理対象: {input_path}")
        print(f"🔢 整形対象数: {len(incomplete_keys)} 件 (プロンプト: {prompt_method_name})")

        for key in incomplete_keys:
            original_text = original_data.get(key)
            if original_text is None:
                print(f"  ❌ 元データに存在しません: {key}")
                continue

            retry_count = 0
            while retry_count < max_retries:
                try:
                    reformatted = format_text_with_model(original_text, prompt_method_name)
                    if is_properly_formatted(reformatted, prompt_method_name):
                        formatted_data[key] = reformatted
                        print(f"  ✅ 整形成功: {key}")
                        break
                    else:
                        retry_count += 1
                        print(f"  ❌ 整形失敗（フォーマット不正）: {key} → {retry_count}回目")
                except Exception as e:
                    print(f"  ❌ 整形失敗（例外）: {key} → {e}")
                    retry_count += 1

            if retry_count == max_retries:
                print(f"  ⚠️ 最大リトライ超過: {key}")
                formatted_data[key] = original_text  # 元のまま残す

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, ensure_ascii=False, indent=2)


# ===== メイン実行 =====
if __name__ == "__main__":
    input_model_name = extract_model_name(input_model)
    model_dir_path = f"./output/{input_model_name}"

    reformat_all_entries(
        input_model_name=input_model,
        model_dir_path=model_dir_path,
        max_retries=max_retries
    )