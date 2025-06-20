#プロンプト一覧
#zero_shot(推論プロセス)
#few_shot_cot(事例)
#zero_shot_cot_with_inference_process(推論プロセス)
#few_shot_cot_with_inference_process(事例+推論プロセス)

from ollama import Client
class MashupServiceRecommendation_open_llm:
    def __init__(self, few_shot_examples, available_categories, available_apis, service_requirements):
        self.few_shot_examples =few_shot_examples
        self.available_categories = available_categories
        self.available_apis = available_apis
        self.service_requirements = service_requirements
        self.client = Client(
            host='http://localhost:11434',
            headers={'Content-Type': 'application/json'}
        )
    
    def plan_and_solve(self):
        messages = [
            # 1. system ロールでAIの振る舞いを定義
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and proposes suitable APIs from the specified Available categories and Available APIs based on the given Requirements.\n"
                    
                )
            },

            # 2. ユーザー入力を user ロールとして分離
            {
                "role": "user",
                "content": (
                    f"Available categories: {', '.join(self.available_categories)}\n"
                    f"Available APIs: {self.available_apis}\n"
                    f"Requirements: {self.service_requirements}\n\n"
                    "Let's first understand the problem and devise a plan to solve the problem. Then, let's carry out the plan and solve the problem step by step."

                )
            }
        ]

        return messages


    def zero_shot_cot(self):
        messages = [
            # 1. system ロールでAIの振る舞いを定義
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and proposes suitable APIs from the specified Available categories and Available APIs based on the given Requirements.\n"
                )
            },

            # 2. ユーザー入力を user ロールとして分離
            {
                "role": "user",
                "content": (
                    f"Available categories: {', '.join(self.available_categories)}\n"
                    f"Available APIs: {self.available_apis}\n"
                    f"Requirements: {self.service_requirements}\n\n"
                    "Let's think step by step."
                    "Please provide the following:\n"
                    "**Reasoning**:\n"
                    "   - Detailed breakdown of the thought process\n\n"
                    "**Conclusion**:\n"
                    "   - Recommend categories: ['Category_name', 'Category_name', ...]\n"
                    "   - Recommend All matched APIs: ['API_name', 'API_name', ...]"
                )
            }
        ]

        return messages


    def few_shot_cot(self):
        # 1. system 指示
        messages = [
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and proposes suitable APIs from the specified available categories and available APIs based on the given Requirements.\n"
                )
            }
        ]

        # 2. few-shot 例（user → assistant のペアであることを前提）
        messages.extend(self.few_shot_examples)

        # 3. 本リクエストを追加
        messages.append({
            "role": "user",
            "content": (
                f"Available categories: {', '.join(self.available_categories)}\n"
                f"Available APIs: {self.available_apis}\n"
                f"Requirements: {self.service_requirements}\n\n"
                "Let's think step by step."
                "Please provide the following:\n"
                "**Reasoning**:\n"
                "   - Detailed breakdown of the thought process\n\n"
                "**Conclusion**:\n"
                "   - Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n"
                "   - Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n"
                "   - Final recommended APIs: ['API_name', 'API_name', ...]"
            )
        })

        return messages
    
    def zero_shot_cot_with_inference_process(self):
        messages = [
            # 1. system ロールでAIの推論手順と目的を明確に
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of a mashup service.\n"
                    "The goal is to logically progress from the given Requirements to the core functionalities, "
                    "then to the proposed API categories, and finally to the selected and recommended APIs.\n"
                    "Follow this reasoning process:\n"
                    "1. Infer the core functionalities of the mashup service based on the given Requirements.\n"
                    "2. Identify and propose multiple highly relevant API categories from the Available categories.\n"
                    "3. Match APIs from the proposed categories and identify relevant ones based on their descriptions.\n"
                    "4. Select and recommend the best-suited APIs with reasons.\n"
                )
            },

            # 2. ユーザー入力を user ロールとして明確に分ける
            {
                "role": "user",
                "content": (
                    f"Available categories: {', '.join(self.available_categories)}\n"
                    f"Available APIs: {self.available_apis}\n"
                    f"Requirements: {self.service_requirements}\n\n"
                    "Let's think step by step."
                    "Please provide the following:\n"
                    "**Reasoning**:\n"
                    "   - Detailed breakdown of the thought process (based on the 4-step inference process above)\n\n"
                    "**Conclusion**:\n"
                    "   - Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n"
                    "   - Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n"
                    "   - Final recommended APIs: ['API_name', 'API_name', ...]"
                )
            }
        ]

        return messages
    
    def few_shot_cot_with_inference_process(self):
        messages = [
            # 1. systemメッセージ：推論プロセスと目的を定義
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "The goal is to logically progress from the given Requirements to the core functionalities, "
                    "then to the proposed API categories, and finally to the selected and recommended APIs.\n"
                    "It follows the reasoning process below:\n"
                    "1. Infer the core functionalities of the mashup service based on the given Requirements.\n"
                    "2. Identify and propose relevant API categories from the available categories.\n"
                    "3. Match APIs from each category based on descriptions and requirement alignment.\n"
                    "4. Select and recommend the best-suited APIs with reasons.\n"
                )
            }
        ]

        # 2. few-shot examples（user → assistant のペア）を追加
        messages.extend(self.few_shot_examples)

        # 3. タスク入力（userロール）を追加
        messages.append({
            "role": "user",
            "content": (
                f"Available categories: {', '.join(self.available_categories)}\n"
                f"Available APIs: {self.available_apis}\n"
                f"Requirements: {self.service_requirements}\n\n"
                "Please follow the reasoning process and provide:\n"
                "**Reasoning**:\n"
                "   - Detailed breakdown of the thought process (Steps 1–4)\n\n"
                "**Conclusion**:\n"
                "   - Recommend categories from 2.: ['Category_name', 'Category_name', ...]\n"
                "   - Recommend All matched APIs in 3.: ['API_name', 'API_name', ...]\n"
                "   - Final recommended APIs: ['API_name', 'API_name', ...]"
            )
        })

        return messages

    
    #回答を作成するプロンプト
    def choice_prompt(self, prompt_method_name, model):
        prompt_method = getattr(self, prompt_method_name, None)
        if not prompt_method:
            raise ValueError(f"Method {prompt_method_name} not found")

        messages = prompt_method()
        
        try:
            response = self.client.chat(model=model, messages=messages,options={
                "temperature": 0
            })
            return response.message.content
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return None
    