#これはopenai_apiを使用する
######################以下選択必須#####################################
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
# model = "gpt-4o"
model = "gpt-4o-mini"
"""""""④プロンプト選択"""""""""
#prompt_method_name = "zero_shot_cot"
#prompt_method_name = "few_shot_cot"
#prompt_method_name = "zero_shot_cot_with_inference_process"
prompt_method_name = "few_shot_cot_with_inference_process"
"""""""⑤評価サービスの選定"""""""""
#全てのサービスを評価時
single_service_name = None
#特定のサービスのみ評価時(サービス名を指定)
"#未実装(それ以降のサービスを評価するか, 単一だけ評価するか悩み中のため)"
"""""""⑥要件文ごとの評価回数・llm呼び出し上限"""""""""
#要件文ごとの評価回数
iterations = 1
#llm呼び出し上限
max_calls = 2000

"""""""⑦事例に使用しているサービスは評価しない"""""""""
skip_mashp_names = {"radaar", "2lingual-bing-search", "aircellcall", "wishgenies", "bible-mapped"}
#####################################################################

#事例を呼び出し
import openai
import pandas as pd
import re
import pprint
import json
import os
from dotenv import load_dotenv
#open_ai_apiキーを取得
load_dotenv()  # .envファイルを読み込む
openai.api_key = os.getenv("OPENAI_API_KEY")

####################################################################
"""""""①データ抽出"""""""""
######APIデータ抽出#########
import pprint
from get_information import GetAvailableAPIData
api_data_getter = GetAvailableAPIData(api_data)
# API情報を取得
available_apis, available_apis_name = api_data_getter.get_available_apis()
# カテゴリ一覧取得
available_categories = api_data_getter.get_available_categories()

######mashupデータ抽出#########
from get_information import GetAvailableMashupData
# JSONファイルパスを渡してインスタンス作成
mashup_data_getter = GetAvailableMashupData(mashup_data)
# 複合サービスの詳細情報を取得
available_mashup = mashup_data_getter.get_mashup_details()
########################################################################
"""""""②プロンプト呼び出し"""""""""
from prompt.prompt_openai import MashupServiceRecommendation_openai
########################################################################

#JsonファイルにGPTの出力結果を保存
def save_to_json(data, prompt_method_name, mashup_name):
    """
    JSONファイルに番号付きでデータを追加保存し、値内の改行をそのまま反映する。
    :param data: 保存するデータ（文字列）
    :param prompt_method_name: 保存先ファイル名（変数として渡される）
    :param mashup_name: キーとして使用する名前
    """
    # メソッド名 → ファイル名のマッピング
    filename_map = {
        "few_shot_cot_with_inference_process": "few_cot_infer",
        "few_shot_cot": "few_cot",
        "zero_shot_cot": "zero_cot",
        "zero_shot_cot_with_inference_process": "zero_cot_infer",
        # 必要に応じて他も追加可能
    }
    # 変換されたファイル名（短縮名がなければそのまま使う）
    short_name = filename_map.get(prompt_method_name, prompt_method_name)
    
    # ファイル名の生成
    filename = f"./output/openai/{short_name}/responses.json"

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
#事例呼び出し
from examples.few_cot import few_shot_examples
from examples.few_cot_detail import few_shot_examples_detail

call_count = 0  # LLM呼び出し回数（全体で1回だけ定義）
stop_flag = False
#一つずつサービスを実行する
for mashup_name, details in available_mashup.items():
    #事例に使用したサービスをスキップ
    if mashup_name in skip_mashp_names:
        continue 
    #現在のmash upサービス情報取得
    true_categories = details.get('api_categories', [])
    true_apis = details.get('apis', [])
    description = details.get('description', "")

    #推薦システムの初期設定
    recommendation_system = MashupServiceRecommendation_openai(few_shot_examples, available_categories, available_apis, description)
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
        response = recommendation_system.choice_prompt(prompt_method_name, model)
        save_to_json(response, prompt_method_name, mashup_name)

    if stop_flag:
        break

