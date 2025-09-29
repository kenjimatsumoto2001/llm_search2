#これはファイルからスコアを計算する

import json
from ollama import Client
import os
import re
import ast
from ollama import Client
"""""""①評価したいllmモデル選択"""""""""
# input_model = "deepseek"
# input_model = "llama"
input_model = "gpt"
"""""""②整形したいプロンプト選択"""""""""
# prompt_method_name = "few_shot_cot"
prompt_method_name = "few_shot_cot_with_inference_process"
# prompt_method_name = "few_shot"
# prompt_method_name = "few_shot_ablation"
# prompt_method_name ="plan_and_solve"
# prompt_method_name = "zero_shot_cot"
# prompt_method_name = "zero_shot_cot_with_inference_process"
# prompt_method_name ="zero_shot"

#再整形上限
max_retries=3
########################################################################
# メソッド名 → ファイル名のマッピング
filename_map = {
    "zero_shot":"zero_shot",
    "zero_shot_cot": "zero_cot",
    "zero_shot_cot_with_inference_process": "zero_cot_infer",
    "few_shot":"few_shot",
    "few_shot_ablation":"few_shot_ablation",
    "few_shot_cot": "few_cot",
    "few_shot_cot_with_inference_process": "few_cot_infer",
    "plan_and_solve":"plan_and_solve"
    # 必要に応じて他も追加可能
}

# 各プロンプト手法に対して期待される [] の数を指定
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

input_model_name = extract_model_name(input_model)
short_name = filename_map.get(prompt_method_name, prompt_method_name)
# input_path = f"./output/{input_model_name}/{short_name}/responses.json"
# output_path = f"./output/{input_model_name}/{short_name}/responses_formatted.json"
input_path = f"./output/{input_model_name}/bert_top6/bert_responses.json"
output_path = f"./output/{input_model_name}/bert_top6/responses_formatted.json"

# ========== 整形プロンプト生成 ==========
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
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    
    elif prompt_method_name in ["few_shot_cot_with_inference_process"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    

    elif prompt_method_name in ["zero_shot_cot_with_inference_process"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    

    elif prompt_method_name in ["plan_and_solve"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    
    elif prompt_method_name in ["few_shot_ablation"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    Recommend All matched APIs: ['API_name', 'API_name', ...]\n
    Final recommended APIs: ['API_name', 'API_name', ...]\n
"""
    
    elif prompt_method_name in ["few_shot"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    recommended APIs: ['API_name', 'API_name', ...]\n
"""
    
    elif prompt_method_name in ["zero_shot"]:
        return f"""
---
{text}
---
Therefore, The answer is
    Recommend categories: ['Category_name', 'Category_name', ...]\n
    recommended APIs: ['API_name', 'API_name', ...]\n
"""
    else:
        raise ValueError(f"Unknown prompt method: {prompt_method_name}")
    
client = Client(
    host='http://localhost:11434',
    headers={'Content-Type': 'application/json'}
)

# ========== LLM で整形 ==========
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

# ========== 整形チェック ==========
def is_properly_formatted(response_text: str, prompt_method_name: str) -> bool:
    expected_count = expected_bracket_counts.get(prompt_method_name, 0)
    lists_in_brackets = re.findall(r"\[.*?\]", response_text)

    if len(lists_in_brackets) < expected_count:
        return False
    if any(item.strip() == "[]" for item in lists_in_brackets):
        return False
    return True

# ========== 不完全エントリ抽出 ==========
def detect_incomplete_entries(output_path, prompt_method_name):
    with open(output_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    no_list_keys = []
    expected_count = expected_bracket_counts.get(prompt_method_name, 0)

    for key, value in data.items():
        lists_in_brackets = re.findall(r"\[.*?\]", value)

        # []の数が足りない、または空リストが含まれる場合
        if len(lists_in_brackets) < expected_count or any(item.strip() == "[]" for item in lists_in_brackets):
            no_list_keys.append(key)
            continue

        # 構文が壊れている場合や ... が含まれる場合も追加
        invalid = False
        for lst in lists_in_brackets:
            if "..." in lst:
                invalid = True
                break
            try:
                parsed = ast.literal_eval(lst)
                if not isinstance(parsed, list):
                    invalid = True
                    break
            except Exception:
                invalid = True
                break

        if invalid:
            no_list_keys.append(key)

    return no_list_keys


# ========== 再整形処理 ==========
def reformat_failed_entries(no_list_keys, input_path, output_path, prompt_method_name, max_retries):
    with open(input_path, 'r', encoding='utf-8') as f:
        original_data = json.load(f)

    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            formatted_data = json.load(f)
    else:
        formatted_data = {}

    for key in no_list_keys:
        print(f"\n再整形対象: {key}")
        original_text = original_data.get(key)
        if original_text is None:
            print(f"  元データに存在しません。スキップ。")
            continue

        retry_count = 0
        while retry_count < max_retries:
            try:
                print(f"  {retry_count + 1}回目の整形...")
                reformatted = format_text_with_model(original_text, prompt_method_name)

                if is_properly_formatted(reformatted, prompt_method_name):
                    formatted_data[key] = reformatted
                    print("  整形成功 ✅")
                    break
                else:
                    print("  整形結果が不正 ❌ → 再試行")
                    retry_count += 1

            except Exception as e:
                print(f"  整形失敗 ❌（例外）: {e}")
                retry_count += 1

        if retry_count == max_retries:
            print("  整形失敗 → 元のまま保存")
            formatted_data[key] = original_text

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(formatted_data, f, ensure_ascii=False, indent=2)

# ========== 実行 ==========
import pandas as pd
class prf_Calculator:
    def calculate_metrics(self, true_set, predicted_set):
        true_positive = len(true_set.intersection(predicted_set))
        precision = true_positive / len(predicted_set) if predicted_set else 0
        recall = true_positive / len(true_set) if true_set else 0
        f_score = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0
        return precision, recall, f_score

    def average_metrics(self, metrics_list):
        avg_precision = sum(m[0] for m in metrics_list) / len(metrics_list) if metrics_list else 0
        avg_recall = sum(m[1] for m in metrics_list) / len(metrics_list) if metrics_list else 0
        avg_f_score = sum(m[2] for m in metrics_list) / len(metrics_list) if metrics_list else 0
        return avg_precision, avg_recall, avg_f_score

# ===== 評価実行関数 =====
def evaluate_responses(formatted_path, mashup_csv_path, prompt_method_name, expected_bracket_counts):
    with open(formatted_path, 'r', encoding='utf-8') as f:
        formatted_data = json.load(f)

    mashup_df = pd.read_csv(mashup_csv_path)
    mashup_data = {}
    for _, row in mashup_df.iterrows():
        mashup_data[row['mashup_name']] = {
            'apis': set(row['api_name'].strip("[]").replace("'", "").split(", ")),
            'api_categories': set(row['api_category'].strip("[]").replace("'", "").split(", "))
        }

    expected_count = expected_bracket_counts.get(prompt_method_name, 0)
    prf = prf_Calculator()
    api_inter_scores = []
    api_final_scores = []
    category_scores = []

    for mashup_name, response_text in formatted_data.items():
        normalized_name = mashup_name.rsplit("-", 1)[0]
        if normalized_name not in mashup_data:
            continue
        lists = re.findall(r"\[.*?\]", response_text)
        parsed_lists = []
        valid = True  # 有効な出力かどうかのフラグ
        for lst in lists:
            if "..." in lst:
                print(f"⚠️ Ellipsis（...）検出: {mashup_name} → スキップ")
                valid = False
                break
            try:
                parsed = ast.literal_eval(lst)
                if not isinstance(parsed, list):
                    raise ValueError("Not a list")
                parsed_lists.append(parsed)
            except Exception:
                print(f"⚠️ 無効なリスト構文: {mashup_name} → スキップ")
                valid = False
                break

        # 不正な出力 or 不足している場合はスキップ
        if not valid or len(parsed_lists) < expected_count:
             # スコア0として記録
            category_scores.append((0, 0, 0))
            api_inter_scores.append((0, 0, 0))
            api_final_scores.append((0, 0, 0))
            continue

        if len(parsed_lists) < expected_count:
            continue  # 不完全な出力はスキップ

        # 正解データ
        gold = mashup_data[normalized_name]
        true_apis = gold['apis']
        true_categories = gold['api_categories']

        # 予測データ
        # 各リストを評価（中間APIと最終APIを分ける）
        if expected_count == 3:
            pred_categories = set(parsed_lists[0])
            pred_apis_intermediate = set(parsed_lists[1])
            pred_apis_final = set(parsed_lists[2])
        else:
            pred_categories = set(parsed_lists[0])
            pred_apis_intermediate = set(parsed_lists[1])  # 2つしかない場合、これが唯一のAPI予測
            pred_apis_final = set(parsed_lists[1])         # 同じものを使う

        # 小文字・ハイフン処理（オプションで強化）
        # 正解データ
        gold = mashup_data[normalized_name]
        true_categories = {x.lower().replace(" ", "-") for x in gold['api_categories']}
        true_apis = {x.lower().replace(" ", "-") for x in gold['apis']}

        # 予測データ（前処理）
        # 小文字・ハイフン処理（None を除いてから）
        pred_categories = {x.lower().replace(" ", "-") for x in pred_categories if isinstance(x, str)}
        pred_apis_intermediate = {x.lower().replace(" ", "-") for x in pred_apis_intermediate if isinstance(x, str)}
        pred_apis_final = {x.lower().replace(" ", "-") for x in pred_apis_final if isinstance(x, str)}


        # スコア評価
        category_scores.append(prf.calculate_metrics(true_categories, pred_categories))
        api_inter_scores.append(prf.calculate_metrics(true_apis, pred_apis_intermediate))
        api_final_scores.append(prf.calculate_metrics(true_apis, pred_apis_final))
        # print(gold)
        # print(pred_categories)
        # print(pred_apis_intermediate)
        # print(pred_apis_final)
        # print("###########")
        # print("カテゴリ精度",category_scores)
        # print("API精度",api_inter_scores)
        # print("最終提示API精度",api_final_scores)

    print("\n=== API Recommendation Metrics ===")
    print("\n=== Category Recommendation Metrics ===")
    print(f"全mashup件数: {len(formatted_data)}")
    p, r, f = prf.average_metrics(category_scores)
    print(f"Category - Precision: {p:.3f}, Recall: {r:.3f}, F1: {f:.3f}")

    p, r, f = prf.average_metrics(api_inter_scores)
    print(f"API  - Precision: {p:.3f}, Recall: {r:.3f}, F1: {f:.3f}")

    p, r, f = prf.average_metrics(api_final_scores)
    print(f"最終提示API  - Precision: {p:.3f}, Recall: {r:.3f}, F1: {f:.3f}")


if __name__ == "__main__":
    print("整形ファイル:", output_path)

    no_list_keys = detect_incomplete_entries(output_path, prompt_method_name)
    print(f"\n再整形対象数: {len(no_list_keys)} 件")

    # reformat_failed_entries(
    #     no_list_keys=no_list_keys,
    #     input_path=input_path,
    #     output_path=output_path,
    #     prompt_method_name=prompt_method_name,
    #     max_retries=max_retries
    # )
    evaluate_responses(
        formatted_path=output_path,
        mashup_csv_path="./data/filterd_mashup_data.csv",
        prompt_method_name=prompt_method_name,
        expected_bracket_counts=expected_bracket_counts
    )