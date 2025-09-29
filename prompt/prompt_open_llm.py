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

        # Few-shot examples
        examples = [
            # 1
            {
                "role": "user",
                "content": "Requirements: Mashup showing locations of 200 places mentioned in the Bible. Going for accuracy they try to pinpoint the locations of the ruins of ancient cities instead of using the locations of modern cities with ancient names.\n"
            },
            {
                "role": "assistant",
                "content": (
                "To fulfill the requirements for a mashup service showing locations of the 200 places mentioned in the Bible, the following needs to be taken into consideration:\n\n"
                "1. **Mapping Capability**: The primary requirement involves mapping the locations of ancient cities accurately as opposed to modern cities with ancient names. For this task, a mapping API is needed to plot the locations of these cities on a map with precise accuracy.\n\n"
                "2. **Reference Data**: The service will require reliable reference data for the places mentioned in the Bible. This can include details about the biblical references corresponding to each ancient location, which can guide users through exploring the historical significance of each site.\n\n"
                "3. **API Options**:\n"
                "   - **Mapping APIs**: The Google Maps API and Bing Maps API would be effective for mapping functionalities. Both APIs provide powerful capabilities for displaying maps, geolocation, and routing information, which can be beneficial for pinpointing the locations of ancient cities.\n"
                "   - **Reference APIs**: The ESV Bible Lookup API appears to be very appropriate here, as it provides access to biblical text, which can be linked with the corresponding geographical locations of the cities. This gives context and allows for a deeper exploration of each location mentioned in the Bible.\n\n"
                "4. **Focus on Precision**: Given the requirement states a focus on pinpointing ruins of ancient cities instead of modern names, it is crucial to select APIs that can handle detailed geographical data which might be essential for adequately representing locations of ruins accurately.\n\n"
                "5. **Combining Data**: The final mashup needs to combine both mapping and textual references seamlessly to provide an integrated experience for the users exploring biblical locations.\n"
                "- Recommend categories: ['mapping', 'reference']\n"
                "- Recommended APIs: ['google-maps', 'esv-bible-lookup']\n")
                
            },

            # 2
            {
                "role": "user",
                "content": "Requirements: WishGenies lets you ask for gift recommendations for those on your shopping list. You'll get great ideas because WishGenies asks people who like the same things as your recipient.\n"
            },
            {
                "role": "assistant",
                "content": (
                "To determine the appropriate APIs for the WishGenies project, we need to analyze the requirements of the service, which focuses on generating gift recommendations based on social interests. The key features discussed in the requirements include:\n\n"
                "1. **Gift Recommendations**: Suggesting gifts that resonate with recipients' interests.\n"
                "2. **Social Connections**: The ability to leverage social data from users who have shared interests with the recipient.\n\n"
                "Given these aspects, the primary categories that seem relevant are **ecommerce** and **social**. Here's the breakdown:\n\n"
                "- **Ecommerce**: Since WishGenies is helping users find gift recommendations, we need access to product databases that can provide product information. APIs that can pull product details, images, availability, and pricing would be essential. The Amazon Product Advertising API is a clear match for this need, as it has a robust database of products and allows businesses to tap into Amazon's extensive ecommerce functionalities.\n\n"
                "- **Social**: Since the service seeks recommendations based on shared interests and social connections, accessing social media data is vital. APIs from social media platforms can facilitate obtaining user interests, friend connections, or activity data which can guide gift suggestions. The Facebook and Google+ APIs can provide insights into individuals' preferences, Likes, and shared activities that can guide recommendations.\n\n"
                "Based on this, the ecommerce category should include APIs that can access product databases and the social category should encompass APIs that can pull user interest data.\n"
                "   - Recommend categories: ['social', 'ecommerce']\n"
                "   - recommended APIs: ['facebook', 'amazon-product-advertising']\n")
            },

            # 3
            {
                "role": "user",
                "content": "Requirements: RADAAR is a powerful social media management and collaboration platform designed for handling multiple brands. It helps marketers at every step, from scheduling and publishing posts on their profiles to analyzing their efforts. Whether you're a small business focusing on a few social media networks, an agency managing multiple brands, or an enterprise company that needs it all, RADAAR will help you drastically streamline your workflows, simplify your social media management, and save time. RADAAR provides a variety of features including tools for publishing, social media inbox, social media monitoring, and analytics.\n"
            },
            {
                "role": "assistant",
                "content": (
                "RADAAR is a comprehensive social media management platform aimed at simplifying social media workflows for brands, marketers, and agencies. Its functionality spans across various operations such as scheduling and publishing posts, monitoring social media interactions, and analyzing performance metrics.\n\n"
                    "### Breakdown of Requirements Related to APIs:\n"
                    "1. **Social Media Management**:\n"
                    "   - RADAAR is designed specifically to manage multiple social media accounts, allowing users to interact with platforms directly from its interface.\n\n"
                    "2. **Post Scheduling & Publishing**:\n"
                    "   - To schedule and publish posts timely across various platforms (like Twitter, Facebook, Instagram, etc.), the appropriate APIs should allow for post creation and scheduling.\n\n"
                    "3. **Social Media Monitoring**:\n"
                    "   - The platform’s need to monitor social media interactions means it requires APIs that can fetch the latest posts, user activities, and engagement metrics.\n\n"
                    "4. **Analytics**:\n"
                    "   - RADAAR offers analytics functionality, thus requiring APIs that provide performance data, insights, and reporting tools to help users measure the success of their social media strategies.\n\n"
                    "5. **Multi-platform Support**:\n"
                    "   - RADAAR supports multiple brands which implies the need for APIs that cater to a wide variety of social media platforms.\n\n"
                    "### Matching API Categories:\n"
                    "Given these requirements, the APIs should primarily fall under the 'social' and 'analytics' categories to match the functionalities expected from RADAAR.\n\n"
                    "- **Social APIs**: These will allow for managing social media interactions, publishing, and scheduling content.\n"
                    "- **Analytics APIs**: These can help with measuring and reporting the effectiveness of the content being published across social networks.\n\n"
                    "### Recommended APIs:\n"
                    "After evaluating the available APIs in those categories:\n"
                    "- **From the 'social' category**:\n"
                    "  - **Twitter**: Essential for posting and interactions on Twitter.\n"
                    "  - **Instagram Graph**: For managing Instagram accounts and posts.\n"
                    "  - **Facebook**: To handle Facebook posts and interactions.\n"
                    "  - **LinkedIn**: For managing professional networking and company pages.\n\n"
                    "- **From the 'analytics' category**:\n"
                    "  - **New Relic**: While not a direct social analytics tool, it can offer insights into application performance, which can indirectly assist in understanding user engagement on social platforms.\n\n"
                    "- Additionally, the **Vimeo** and **YouTube** APIs can be relevant if any video content is part of the social media strategy.\n"
                    "   - Recommend categories: ['social', 'photos', 'video']\n"
                    "   - recommended APIs: ['twitter', 'instagram-graph', 'facebook', 'linkedin', 'youtube', 'vimeo']\n")
            },

            # 4
            {
                "role": "user",
                "content": "Requirements: Bing Search in 2 separate languages. 2lingual Bing Search is a dual-language search tool that performs both a Bing Search and a Cross-language Bing Search. It also provides a query translation option that can be activated or deactivated for Cross-language Bing Searches. The top-ranking Bing Search Results from 2 user-selected search languages are displayed in side-by-side columns. Other features include Search Suggestions, Spelling Corrections, Cached Pages and Related Search Links.\n"
            },
            {
                "role": "assistant",
                "content": (
                "The requirements specify that this service will be a dual-language search tool using Bing, capable of performing searches in two different languages at once. It uses Bing for both standard and cross-language searches. Additionally, it includes features like query translations, which can be toggled, as well as other helpful methods such as search suggestions and spelling corrections.\n\n"
                "1. **Basic Search Requirement**:\n"
                "   - The foundational requirement of conducting a search fundamentally leads us to use the Bing-related APIs. They are designed for integrating Bing's search capabilities into applications.\n\n"
                "2. **Language Translation Requirement**:\n"
                "   - Since the service needs to provide searches in two different languages and supports query translation, APIs that offer translation services would be crucial.\n"
                "   - The Microsoft Translator API is relevant as it provides language translation capabilities.\n\n"
                "3. **Result Handling**:\n"
                "   - The requirement specifies displaying results in side-by-side columns. This doesn't directly imply an additional API but suggests that we'll need a way to format and display data once we've received it from the search and translation API.\n\n"
                "4. **Additional Features**:\n"
                "   - Features like search suggestions, spelling corrections, cached pages, and related search links can typically be handled through a comprehensive search API, such as the Bing Search API itself, which can extend its capabilities with suggestions and corrections.\n\n"
                "5. **API Considerations**:\n"
                "   - **bing**: This would help in conducting general search queries.\n"
                "   - **microsoft-bing**: This acts as the core search functionality through Bing which allows for robust querying and obtaining results.\n"
                "   - **bing-translator**: Specifically offers translation services, fitting the requirement for translating searches.\n"
                "   - **microsoft-translator**: Also suitable for translation functionality.\n\n"
                "By piecing these together, the essential requirements of the 2lingual Bing Search can be met effectively.\n"
                "   - Recommend categories: ['search', 'translation', 'tools']\n"
                "   - recommended APIs: ['microsoft-bing', 'bing', 'microsoft-translator', 'bing-translator']\n")
            },

            # 5
            {
                "role": "user",
                "content": "Requirements: A new method of communication involving VOIP/wireless and cable call management phone booth systems. AirCellCall's technical architecture system combines several communication methods into one device that you can use to communicate even if you do not have a cell phone available. Designed to serve the general public, corporate and government entities.\n"
            },
            {
                "role": "assistant",
                "content":(
                "1. **Understanding the requirements**:\n"
                "   - The service mentioned is centered around VOIP (Voice Over Internet Protocol) and cable call management, emphasizing various communication methods that can work together. It seems that the service is aimed at providing a unified platform for communication for the general public, corporate, and government entities.\n"
                "   - Hence, the focus is on telecommunication capabilities, which points towards Telephony as a key category.\n\n"
                "2. **Identifying relevant categories**:\n"
                "   - The correct categories mentioned were 'telephony' and 'messaging'.\n"
                "   - The telephony category primarily covers APIs related to voice communication, call management, and any applications that support VOIP functionalities.\n"
                "   - The messaging category is relevant as the service would likely need features to send texts or notifications in addition to voice communication.\n\n"
                "3. **Searching for suitable APIs**:\n"
                "   - Two APIs were recommended: **Twilio** and **Twilio-SMS**.\n"
                "   - **Twilio**: This API supports sending and receiving voice calls and integrates easily into applications which makes it ideal for creating a call management service.\n"
                "   - **Twilio-SMS**: This API will allow for SMS messaging functionalities, enhancing communication capabilities beyond just voice to text and notifications.\n\n"
                "4. **Additional considerations**:\n"
                "   - Although other APIs exist in messaging and interactivity, Twilio excels in flexibility and documentation, making it a popular choice among developers for integrating diverse communication solutions.\n"
                "   - Other APIs in categories such as chat or additional messaging frameworks could be explored, but for the main functionality outlined in the requirements, Twilio provides a robust foundation.\n"
                "   - Recommend categories: ['telephony', 'messaging']\n"
                "   - recommended APIs: ['twilio', 'twilio-sms']\n")
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
                    "2. Identify and propose relevant API categories from the available categories based on the core functionalities and available apis.\n"
                    "3. Match APIs from each category based on descriptions and requirement.\n"
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
    