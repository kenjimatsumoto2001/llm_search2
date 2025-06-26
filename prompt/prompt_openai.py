#プロンプト一覧
#zero_shot(推論プロセス)
#few_shot_cot(事例)
#zero_shot_cot_with_inference_process(推論プロセス)
#few_shot_cot_with_inference_process(事例+推論プロセス)

import openai
class MashupServiceRecommendation_openai:
    def __init__(self, few_shot_examples, available_categories, available_apis, service_requirements):
        self.few_shot_examples =few_shot_examples
        self.available_categories = available_categories
        self.available_apis = available_apis
        self.service_requirements = service_requirements

    def plan_and_solve(self):
        messages = [
            # 1. system ロールでAIの振る舞いを定義
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and recommends suitable categories and APIs from the specified Available categories and Available APIs according to the given requirements.\n"
                    
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
    
    def zero_shot(self):
        messages = [
            # 1. system ロールでAIの振る舞いを定義
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and recommends suitable categories and APIs from the specified Available categories and Available APIs according to the given requirements\n"
                )
            },

            # 2. ユーザー入力を user ロールとして分離
            {
                "role": "user",
                "content": (
                    f"Available categories: {', '.join(self.available_categories)}\n"
                    f"Available APIs: {self.available_apis}\n"
                    f"Requirements: {self.service_requirements}\n\n"
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


    def zero_shot_cot(self):
        messages = [
            # 1. system ロールでAIの振る舞いを定義
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and recommends suitable categories and APIs from the specified Available categories and Available APIs according to the given requirements\n"
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
    
    def few_shot(self):
        # 1. system 指示
        messages = [
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and recommends suitable categories and APIs from the specified Available categories and Available APIs according to the given requirements\n"
                )
            }
        ]

            # Few-shot examples
        examples = [
            # 1
            {
                "role": "user",
                "content": "Requirements: Mashup showing locations of 200 places mentioned in the Bible. Going for accuracy they try to pinpoint the locations of the ruins of ancient cities instead of using the locations of modern cities with ancient names.\n"
            },
            {
                "role": "assistant",
                "content": 
                "   - Recommend categories: ['mapping', 'reference']\n"
                "   - recommended APIs: ['google-maps', 'esv-bible-lookup']\n"
            },

            # 2
            {
                "role": "user",
                "content": "Requirements: WishGenies lets you ask for gift recommendations for those on your shopping list. You'll get great ideas because WishGenies asks people who like the same things as your recipient.\n"
            },
            {
                "role": "assistant",
                "content": 
                "   - Recommend categories: ['social', 'ecommerce']\n"
                "   - recommended APIs: ['facebook', 'amazon-product-advertising']\n"
            },

            # 3
            {
                "role": "user",
                "content": "Requirements: RADAAR is a powerful social media management and collaboration platform designed for handling multiple brands. It helps marketers at every step, from scheduling and publishing posts on their profiles to analyzing their efforts. Whether you're a small business focusing on a few social media networks, an agency managing multiple brands, or an enterprise company that needs it all, RADAAR will help you drastically streamline your workflows, simplify your social media management, and save time. RADAAR provides a variety of features including tools for publishing, social media inbox, social media monitoring, and analytics.\n"
            },
            {
                "role": "assistant",
                "content": 
                "   - Recommend categories: ['social', 'photos', 'video']\n"
                "   - recommended APIs: ['twitter', 'instagram-graph', 'facebook', 'linkedin', 'youtube', 'vimeo']\n"
            },

            # 4
            {
                "role": "user",
                "content": "Requirements: Bing Search in 2 separate languages. 2lingual Bing Search is a dual-language search tool that performs both a Bing Search and a Cross-language Bing Search. It also provides a query translation option that can be activated or deactivated for Cross-language Bing Searches. The top-ranking Bing Search Results from 2 user-selected search languages are displayed in side-by-side columns. Other features include Search Suggestions, Spelling Corrections, Cached Pages and Related Search Links.\n"
            },
            {
                "role": "assistant",
                "content": 
                "   - Recommend categories: ['search', 'translation', 'tools']\n"
                "   - recommended APIs: ['microsoft-bing', 'bing', 'microsoft-translator', 'bing-translator']\n"
            },

            # 5
            {
                "role": "user",
                "content": "Requirements: A new method of communication involving VOIP/wireless and cable call management phone booth systems. AirCellCall's technical architecture system combines several communication methods into one device that you can use to communicate even if you do not have a cell phone available. Designed to serve the general public, corporate and government entities.\n"
            },
            {
                "role": "assistant",
                "content": 
                "   - Recommend categories: ['telephony', 'messaging']\n"
                "   - recommended APIs: ['twilio', 'twilio-sms']\n"
            }
        ]

        messages.extend(examples)

        # 3. 本リクエストを追加
        messages.append({
            "role": "user",
            "content": (
                f"Available categories: {', '.join(self.available_categories)}\n"
                f"Available APIs: {self.available_apis}\n"
                f"Requirements: {self.service_requirements}\n\n"
                "Please provide the following:\n"
                "**Reasoning**:\n"
                "   - Detailed breakdown of the thought process\n\n"
                "**Conclusion**:\n"
                "   - Recommend categories: ['Category_name', 'Category_name', ...]\n"
                "   - Recommended APIs: ['API_name', 'API_name', ...]"
            )
        })

        return messages
    
    def few_shot_ablation(self):
        # 1. system 指示
        messages = [
            {
                "role": "system",
                "content": (
                    "This is a system for proposing appropriate APIs based on the Requirements of mashup service.\n"
                    "It selects and recommends suitable categories and APIs from the specified Available categories and Available APIs according to the given requirements\n"
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
                    "- Detailed breakdown of the thought process\n\n"
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
    def choice_prompt(self, prompt_method_name,model):
        prompt_method = getattr(self, prompt_method_name, None)
        messages = prompt_method()
        response = openai.ChatCompletion.create(
            model = model,
            messages=messages,
        )
        return response['choices'][0]['message']['content']
    