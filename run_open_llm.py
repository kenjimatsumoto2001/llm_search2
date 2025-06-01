#これは研究室に配備されているllmを実行するllm
#事例を呼び出し
from examples.few_cot import few_shot_examples
from examples.few_cot_infer import few_shot_examples_infer

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
"#未実装#"
"""""""③llmモデル選択"""""""""
# model = "gpt-4o"
model = "gpt-4o-mini"
"""""""④プロンプト選択"""""""""
#prompt_method_name = "zero_shot_cot"
prompt_method_name = "few_shot_cot"
#prompt_method_name = "zero_shot_cot_with_inference_process"
#prompt_method_name = "few_shot_cot_with_inference_process"
"""""""⑤評価サービスの選定"""""""""
#全てのサービスを評価時
single_service_name = None
#特定のサービスのみ評価時(サービス名を指定)
single_service_name = "linda"
"""""""⑥要件文ごとの評価回数・llm呼び出し上限"""""""""
#要件文ごとの評価回数
iterations = 1
#llm呼び出し上限
max_calls = 2000
#####################################################################