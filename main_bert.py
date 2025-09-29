#メイン処理
#⚠️ promptがopen_llmとgptで異なる。要確認!!
######################以下選択必須#####################################

#事例を呼び出し
import pandas as pd
import pprint
import json
import os
from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer, util
# bert_model = SentenceTransformer('intfloat/e5-large')
#open_ai_apiキーを取得

"""""""①APIデータ"""""""""
# 複合サービスに利用されているAPI情報のみ抽出(メイン)
api_data = './data/filtered_api_data.json'
# 全てのAPI情報を取得(メイン)
# api_data = './data/api_data_new.json'
"""""""①mashupデータ"""""""""
#複合サービスの内、完全データand api数が2以上
mashup_data = './data/filtered_mashup_data.json'
#複合サービスの内、完全データ and api数が1も含む
"#未実装#(フィルタしていない為)"
"""""""③llmモデル選択"""""""""
# model = "deepseek-r1:70b"
# model = "llama3.3:latest"
model = "gpt-4.1-mini"
# model = "deepseek-r1:32b"
"""""""④プロンプト選択"""""""""
prompt_method_name = "few_shot_cot_with_inference_process"
"""""""⑤使用GPU指定"""""""""
# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
"""""""⑥評価サービスの選定"""""""""
#特定の以降サービスのみ評価時(サービス名を指定)
# start_key='collection-trakr'
#全てのサービスを評価時
start_key= None
"""""""⑦要件文ごとの評価回数・llm呼び出し上限"""""""""
#要件文ごとの評価回数
iterations = 1
#llm呼び出し上限
max_calls = 2000

"""""""⑧事例に使用しているサービスは評価しない"""""""""
skip_mashp_names = {}

#####################################################################
####################################################################
from sentence_transformers import util
import torch

def save_similar_services_to_json(service_name, similar_services, filename="./output/top3_low3_similar_services.json"):
    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = {}
        else:
            existing_data = {}

        # データ追加
        existing_data[service_name] = similar_services

        # 保存
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

        print(f"類似サービスリストを保存しました: {filename}（キー: {service_name}）")

    except Exception as e:
        print(f"保存エラー: {e}")

class MashupSimilarityAnalyzer:
    def __init__(self, embeddings, keys):
        # keys は Python の str 型で受け取る前提
        self.embeddings = embeddings
        self.keys = keys
        self.key_to_index = {key: i for i, key in enumerate(keys)}

    def _get_similarity_scores(self, mashup_name):
        idx = self.key_to_index.get(mashup_name)
        if idx is None:
            return None, None, None

        current_vector = self.embeddings[idx]
        similarities = util.cos_sim(current_vector, self.embeddings)[0]

        all_indices = torch.arange(len(self.keys))
        filtered_indices = all_indices[all_indices != idx]
        filtered_similarities = similarities[filtered_indices]

        return idx, filtered_indices, filtered_similarities

    def get_top_k_keys(self, mashup_name, k=6):
        idx, filtered_indices, similarities = self._get_similarity_scores(mashup_name)
        if similarities is None:
            return []
        top_indices = torch.topk(similarities, k=k).indices
        return [str(self.keys[filtered_indices[i]]) for i in top_indices]  # ← 明示的にstr化

    def get_bottom_k_keys(self, mashup_name, k=6):
        idx, filtered_indices, similarities = self._get_similarity_scores(mashup_name)
        if similarities is None:
            return []
        bottom_indices = torch.topk(-similarities, k=k).indices
        return [str(self.keys[filtered_indices[i]]) for i in bottom_indices]  # ← 明示的にstr化

    def get_high3_low3_keys(self, mashup_name):
        # 一つのリストで返すよう修正
        top_keys = self.get_top_k_keys(mashup_name, k=3)
        bottom_keys = self.get_bottom_k_keys(mashup_name, k=3)
        return top_keys + bottom_keys  # 合体して単一リストで返す

    
"""""""①データ抽出"""""""""
######APIデータ抽出#########
import pprint
from get_information import GetAvailableAPIData
api_data_getter = GetAvailableAPIData(api_data)
# API情報を取得
available_apis, available_apis_name = api_data_getter.get_available_apis()
# カテゴリ一覧取得
available_categories = api_data_getter.get_available_categories()


def filter_mashup(data, start_key=None):
    if start_key is None:
        return data  # 全体を返す

    keys = list(data.keys())
    if start_key in keys:
        start_index = keys.index(start_key)
        filtered_keys = keys[start_index:]
        return {k: data[k] for k in filtered_keys}
    else:
        return {}  # 指定キーが見つからなかった場合は空辞書

######mashupデータ抽出#########
from get_information import GetAvailableMashupData
# JSONファイルパスを渡してインスタンス作成
mashup_data_getter = GetAvailableMashupData(mashup_data)
# 複合サービスの詳細情報を取得
available_mashup = mashup_data_getter.get_mashup_details()

available_mashup = filter_mashup(available_mashup, start_key)
########################################################################
"""""""②プロンプト呼び出し"""""""""
# モデル名から使用クラスを判定してインポート
if "gpt" in model.lower():
    from prompt.prompt_bert_openai import MashupServiceRecommendation_openai as MashupServiceRecommendation
else:
    from prompt.prompt_bert_open_llm import MashupServiceRecommendation_open_llm as MashupServiceRecommendation

########################################################################

#JsonファイルにGPTの出力結果を保存
def save_to_json(data, prompt_method_name, mashup_name):
    """
    JSONファイルに番号付きでデータを追加保存し、値内の改行をそのまま反映する。
    :param data: 保存するデータ（文字列）
    :param prompt_method_name: 保存先ファイル名（変数として渡される）
    :param mashup_name: キーとして使用する名前
    """

    # モデル名を短縮名に変換
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
    #モデル名を変換
    model_name = extract_model_name(model)

    
    # ファイル名の生成
    filename = f"./output/{model_name}/bert_responses.json"
    print(filename)

    try:
        # ファイルが存在する場合、既存の内容を読み取る
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                try:
                    existing_data = json.load(file)  # JSONを辞書に読み込む
                except json.JSONDecodeError:
                    # JSONが壊れている場合は初期化
                    existing_data = {}
        else:
            # ファイルが存在しない場合は空の辞書を作成
            existing_data = {}

        # 同じ mashup_name のキーがいくつあるかカウント
        existing_keys = [key for key in existing_data.keys() if key.startswith(mashup_name)]
        next_key_number = len(existing_keys) + 1
        new_key = f"{mashup_name}-{next_key_number}"

        # 新しいデータを追加
        existing_data[new_key] = data

        # JSON形式でファイルに書き込む
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

        print(f"データが保存されました: {filename} (キー: {new_key})")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

"""""""②llmの実行"""""""""

call_count = 0  # LLM呼び出し回数（全体で1回だけ定義）
stop_flag = False


""""""""""""""""""""""""""""""""""""""""""""""""""
# descriptionのみ抽出
descriptions = {key: value['description'] for key, value in available_mashup.items()}

import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util

# モデル読み込み
bert_model = SentenceTransformer('intfloat/e5-large')
device = "cuda" if torch.cuda.is_available() else "cpu"

# ベクトル読み込み
data = np.load("description_embeddings.npz", allow_pickle=True)
embeddings = torch.tensor(data['embeddings']).to(device)
keys = [str(k) for k in data['keys']]  # ← これで純粋な Python の str 型になる

# 類似度分析クラス初期化
analyzer = MashupSimilarityAnalyzer(embeddings, keys)


# JSON データの読み込み（既に dict である場合はこれ不要）
with open("./output/gpt/few_shot.json", "r") as f:
    shot_data = json.load(f)


def build_few_shot_prompt_examples(matched_results):
    few_shot_examples = []

    for item in matched_results:
        desc = item.get("description", "").strip()
        llm = item.get("llm_output", "").strip()

        if not desc or not llm:
            continue  # 空要素をスキップ

        few_shot_examples.append({
            "role": "user",
            "content": f"Requirements: {desc}"
        })
        few_shot_examples.append({
            "role": "assistant",
            "content": llm
        })

    return few_shot_examples



#一つずつサービスを実行する
for mashup_name, details in available_mashup.items():
    #現在のmash upサービス情報取得
    true_categories = details.get('api_categories', [])
    true_apis = details.get('apis', [])
    description = details.get('description', "")


    if mashup_name not in analyzer.key_to_index:
        print(f"[警告] {mashup_name} はベクトルに存在しません。スキップ。")
        continue

    """""""これを変更する"""""""
    #これは 類似度高い6
    # bert_shot = analyzer.get_top_k_keys(mashup_name)
    #これは 類似度低い6
    # bert_shot = analyzer.get_bottom_k_keys(mashup_name)
    # #これは 類似度高い3 + 低い3
    bert_shot = analyzer.get_high3_low3_keys(mashup_name)

    # ← このタイミングで保存
    save_similar_services_to_json(mashup_name, bert_shot)



    # json_dataのキーを正規化して対応表を作る（'xxx-1' → 'xxx'）
    normalized_llm = {}
    for key, value in shot_data.items():
        base_key = key.rsplit("-", 1)[0]
        if base_key not in normalized_llm:
            normalized_llm[base_key] = value  # 最初の一致だけ採用

    # 結果格納リスト
    matched_results = []

    for key in bert_shot:
        item = {}
        item["mashup_name"] = key
        item["description"] = available_mashup.get(key, {}).get("description", "[No description]")
        item["llm_output"] = normalized_llm.get(key, "[No LLM output]")
        matched_results.append(item)
    print("類似度が高いmashupサービス：",[item["mashup_name"] for item in matched_results])
    
    few_shot_examples = build_few_shot_prompt_examples(matched_results)

    #推薦システムの初期設定
    recommendation_system = MashupServiceRecommendation(few_shot_examples, available_categories, available_apis, description)
    print("-" * 30)
    print("評価中のサービス:",mashup_name)

    # iteration数だけ評価
    for i in range(iterations):  
        if call_count >= max_calls:
            print(f"呼び出し回数が {max_calls} に達しました。処理を終了します。")
            stop_flag = True
            break
        # LLM呼び出し回数カウント
        call_count += 1
        print(f"Iteration {i+1}, Total call: {call_count}")
        # response = recommendation_system.choice_prompt(prompt_method_name, model)       
        # print(response)
        # save_to_json(response, prompt_method_name, mashup_name)

    if stop_flag:
        break