#プロンプト一覧
#zero_shot(推論プロセス)
#few_shot_cot(事例)
#zero_shot_cot_with_inference_process(推論プロセス)
#few_shot_cot_with_inference_process(事例+推論プロセス)

import openai
class make_few_openai:
    def __init__(self, available_categories, available_apis, service_requirements,correct_categories,correct_apis):
        self.available_categories = available_categories
        self.available_apis = available_apis
        self.service_requirements = service_requirements
        self.correct_categories = correct_categories
        self.correct_apis = correct_apis
    
    def make_few(self):
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
                    "During steps 2 and 3, include some plausible but ultimately incorrect candidates to simulate realistic reasoning.\n"
                    "At the end of the reasoning process, explicitly output the final Correct categories and Correct APIs that best match the given Requirements.\n"
                    
                )
            },

            # 2. ユーザー入力を user ロールとして明確に分ける
            {
                "role": "user",
                "content": (
                    f"Available categories: {', '.join(self.available_categories)}\n"
                    f"Available APIs: {self.available_apis}\n"
                    f"Requirements: {self.service_requirements}\n\n"
                    f"Correct categories: {self.correct_categories}\n"
                    f"Correct APIs: {self.correct_apis}\n"

                    "Please provide the following:\n"
                        "1. **Identify Core Features**:\n"
                        "   - Feature_name: reason\n"
                        "   - Feature_name: reason\n"
                        "   ...\n\n"
                        "2. **Identify Relevant API Categories**:\n"
                        "   - Category_name: reason\n"
                        "   - Category_name: reason\n"
                        "   ...\n\n"
                        "3. **Match APIs from Relevant Categories**:\n"
                        "   - **Category APIs**:\n"
                        "       - API_name: reason\n"
                        "       - API_name: reaspn\n"
                        "       ...\n\n"
                        "   - **Category APIs**:\n"
                        "       - API_name: reason\n"
                        "       - API_name: reason\n"
                        "       ...\n\n"
                        "4. **Select the Most Suitable APIs**:\n"
                        "   - API_name: reason\n"
                        "   - API_name: reason\n"
                        "   ...\n\n"
                        "### Conclusion:\n"
                        "   - Recommend categories from 2.:['Category_name', 'Category_name', ...]\n"
                        "   - Recommend All matched APIs in 3.:['API_name', 'API_name', ...]\n"
                        "   - Final recommended APIs: ['API_name', 'API_name', ...]"
                )
            }
        ]

        return messages
    
    
    #回答を作成するプロンプト
    def choice_prompt(self, prompt_method_name,model):
        prompt_method = getattr(self, prompt_method_name, None)
        messages = prompt_method()
        # # === 毎回プロンプトの「完成形（全体）」を表示 ===
        # print("\n===== [COMPLETE PROMPT TO LLM] =====")
        # for msg in messages:
        #     print(f"Role: {msg['role']}")
        #     print(msg['content'])
        #     print("------------------------------------")
        response = openai.ChatCompletion.create(
            model = model,
            messages=messages,
        )
        return response['choices'][0]['message']['content']
    