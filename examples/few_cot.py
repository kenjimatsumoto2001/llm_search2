#few_shotで使用するサービス一覧
#使用サービス：bible-mapped, wishgenies, RADAAR, 2lingual-bing-search, aircellcall
few_shot_examples = [
    #1つ目
    {
        "role": "user",
        "content": 
            "Requirements: Mashup showing locations of 200 places mentioned in the Bible. Going for accuracy they try to pinpoint the locations of the ruins of ancient cities instead of using the locations of modern cities with ancient names.\n"
    },
    {   
        "role": "assistant",
        "content":
            "1. **Identify Core Features**:\n"
            "   - mapping: The mashup requires depicting the precise locations of historical biblical sites, which entails utilizing geolocation and mapping services to represent these places accurately.\n"
            "   - historical reference: The need to locate ancient city ruins ties into accessing historical references about biblical sites, ensuring that the mapped locations are historically accurate.\n\n"
            "2. **Identify Relevant API Categories**:\n"
            "   - mapping: Essential for visualizing and geolocating the ruins of ancient cities mentioned in the Bible.\n"
            "   - reference: Useful for obtaining detailed, historically accurate information about the biblical places to ensure correct representation on the map.\n\n"
            "3. **Match APIs from Relevant Categories**:\n"
            "   - **mapping APIs**:\n"
            "       - google-maps: Provides comprehensive mapping capabilities, including geolocation, which is essential for accurately depicting the locations of ancient ruins.\n"
            "       - google-geocoding: Offers geocoding and reverse geocoding services which can help transform location data into map coordinates.\n\n"
            "   - **reference APIs**:\n"
            "       - esv-bible-lookup: Allows for accessing specific references and data related to biblical texts, which can aid in verifying the historical context and accuracy of the locations.\n"
            "       - wikipedia: The API provides access to a broad database that may include historical details about ancient cities, supporting the validation of their locations.\n\n"
            "4. **Select the Most Suitable APIs**:\n"
            "   - google-maps: Known for its robust and precise mapping capabilities making it ideal for accurately plotting and displaying ancient biblical locations.\n"
            "   - esv-bible-lookup: Directly relates to biblical references which is necessary for validating the historical context of the mapped locations.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 2.: ['mapping', 'reference']\n"
            "   - Recommend All matched APIs in 3.: ['google-maps', 'google-geocoding', 'esv-bible-lookup', 'wikipedia']\n"
            "   - Final recommended APIs: ['google-maps', 'esv-bible-lookup']\n"
    },
    #2つ目
    {
        "role": "user",
        "content": 
            "Requirements: WishGenies lets you ask for gift recommendations for those on your shopping list. You'll get great ideas because WishGenies asks people who like the same things as your recipient.\n"
    },
    {   
        "role": "assistant",
        "content":
            "1. **Identify Core Features**:\n"
            "   - Gift Recommendations: The primary feature is offering curated gift ideas based on recipient preferences.\n"
            "   - Social Preference Sharing: WishGenies leverages social data to match preferences of similar users.\n\n"
            "2. **Identify Relevant API Categories**:\n"
            "   - social: This category is relevant because WishGenies uses social preference data to obtain recommendations, potentially incorporating user profiles and interests.\n"
            "   - ecommerce: This category is relevant because the service deals with gifts, shopping lists, and potentially integrates with ecommerce platforms for product information and transactions.\n\n"
            "3. **Match APIs from Relevant Categories**:\n"
            "   - **social APIs**:\n"
            "       - facebook: Allows accessing social connections and interests that can help tailor gift recommendations based on friends' liked pages, interests, and activities.\n"
            "       - google-plus: Offers access to social data, providing a lesser option for user interaction insights compared to Facebook.\n"
            "       - topsy: Focuses on Twitter data conversations, which is useful for current preferences and social trend analysis.\n\n"
            "   - **ecommerce APIs**:\n"
            "       - bolcom-open: Offers access to product data from an online marketplace, suitable for providing gift options.\n"
            "       - shopify-admin: Integrates ecommerce functionalities that could support managing product data and transactions.\n"
            "       - amazon-product-advertising: Allows access to Amazon's extensive product catalog, ideal for sourcing gift ideas.\n"
            "       - shoppingcom: Offers product catalogs and merchant offers, useful for price comparisons and product availability.\n\n"
            "4. **Select the Most Suitable APIs**:\n"
            "   - facebook: The most suitable due to its wide array of personal interest data, ability to access friend connections, and insights into user behavior which are crucial for making relevant gift recommendations.\n"
            "   - amazon-product-advertising: As one of the largest online marketplaces with a comprehensive product catalog, it is optimal for accessing varied gift options and purchasing links.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 2.: ['social', 'ecommerce']\n"
            "   - Recommend All matched APIs in 3.: ['facebook', 'google-plus', 'topsy', 'bolcom-open', 'shopify-admin', 'amazon-product-advertising', 'shoppingcom']\n"
            "   - Final recommended APIs: ['facebook', 'amazon-product-advertising']\n"
    },
    #3つ目
    {
        "role": "user",
        "content": 
            "Requirements: RADAAR is a powerful social media management and collaboration platform designed for handling multiple brands. It helps marketers at every step, from scheduling and publishing posts on their profiles to analyzing their efforts. Whether you're a small business focusing on a few social media networks, an agency managing multiple brands, or an enterprise company that needs it all, RADAAR will help you drastically streamline your workflows, simplify your social media management, and save time. RADAAR provides a variety of features including tools for publishing, social media inbox, social media monitoring, and analytics.\n"
    },
    {   
        "role": "assistant",
        "content":
            "1. **Identify Core Features**:\n"
            "   - Social Media Scheduling: Supports scheduling and publishing posts, which is a critical component of social media management.\n"
            "   - Analytics and Monitoring: Provides tools for analyzing social media efforts and monitoring interactions, crucial for performance tracking.\n"
            "   - Social Media Collaboration: Enables managing multiple brands, implying the need for collaboration features.\n"
            "   - Content Management: Involves handling media like photos and videos across different social platforms.\n\n"
            "2. **Identify Relevant API Categories**:\n"
            "   - social: Essential for interacting with major social media platforms, managing posts, and analyzing engagement.\n"
            "   - photos: Important for handling image content shared on social media platforms.\n"
            "   - video: Vital for managing and sharing video content across social media channels.\n\n"
            "3. **Match APIs from Relevant Categories**:\n"
            "   - **social APIs**:\n"
            "       - twitter: Integrates with Twitter for posting, analyzing tweets, and engagement.\n"
            "       - instagram-graph: Provides access to Instagram's photo and social media functionalities.\n"
            "       - facebook:Allows accessing social connections and interests that can help tailor gift recommendations based on friends' liked pages, interests, and activities.\n"
            "       - linkedIn: Facilitates managing professional social interactions.\n"
            "       - foursquare: Offers location-based social interaction data.\n\n"
            "   - **photos APIs**:\n"
            "       - imgur: Supports sharing photos and is suitable for managing image-based content.\n"
            "       - snipshot: Allows online image editing, useful for quick modifications before posting.\n"
            "       - flickr: Access to extensive photo libraries for sharing and posting.\n\n"
            "   - **video APIs**:\n"
            "       - youtube: Essential for managing video content and integrating with YouTube's platform.\n"
            "       - vimeo: Offers tools for video processing and distribution.\n"
            "       - brightcove: Supports hosting and managing video content, suitable for enterprises.\n\n"
            "4. **Select the Most Suitable APIs**:\n"
            "   - twitter: Key for integrating with a major social media platform.\n"
            "   - instagram-graph: Crucial for managing Instagram's photo sharing capabilities.\n"
            "   - facebook:Allows accessing social connections and interests that can help tailor gift recommendations based on friends' liked pages, interests, and activities.\n"
            "   - linkedIn: Important for handling professional networking functionalities.\n"
            "   - youtube: Ideal for video content management on YouTube.\n"
            "   - vimeo: Useful for video hosting and sharing for enterprises.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 2.: ['social', 'photos', 'video']\n"
            "   - Recommend All matched APIs in 3.: ['twitter', 'instagram-graph', 'facebook', 'linkedin', 'foursquare', 'imgur', 'snipshot', 'flickr', 'youtube', 'vimeo', 'brightcove']\n"
            "   - Final recommended APIs: ['twitter', 'instagram-graph', 'facebook', 'linkedin', 'youtube', 'vimeo']\n"
    },
    #4つ目
    {
        "role": "user",
        "content": 
            "Requirements: Bing Search in 2 separate languages. 2lingual Bing Search is a dual-language search tool that performs both a Bing Search and a Cross-language Bing Search. It also provides a query translation option that can be activated or deactivated for Cross-language Bing Searches. The top-ranking Bing Search Results from 2 user-selected search languages are displayed in side-by-side columns. Other features include Search Suggestions, Spelling Corrections, Cached Pages and Related Search Links.\n"
    },
    {   
        "role": "assistant",
        "content":
            "1. **Identify Core Features**:\n"
            "   - Dual-language Search: The service needs to perform searches in two languages.\n"
            "   - Cross-language Search: Queries should allow searches in multiple languages and translations.\n"
            "   - Query Translation: The option to translate queries during searches.\n"
            "   - Search Features: The inclusion of features like Search Suggestions, Spelling Corrections, and Related Search Links.\n"
            "   - Display Results: Display top results side-by-side in columns for different languages.\n\n"
            "2. **Identify Relevant API Categories**:\n"
            "   - search: Required for performing basic and cross-language search operations.\n"
            "   - translation: Necessary for translating queries and results into different languages.\n"
            "   - tools: Useful for implementing additional functionalities like search suggestions and spelling corrections.\n\n"
            "3. **Match APIs from Relevant Categories**:\n"
            "   - **search APIs**:\n"
            "       - microsoft-bing: Provides search capabilities and offers rich data APIs.\n"
            "       - bing: Provides search similar to Bing.com offering search results, and various extra data like images and more.\n\n"
            "   - **translation APIs**:\n"
            "       - microsoft-translator: A cloud-based machine translation API for translating terms and query data.\n\n"
            "   - **tools APIs**:\n"
            "       - bing-translator: A Microsoft translation service useful for translating queries and results in applications.\n\n"
            "4. **Select the Most Suitable APIs**:\n"
            "   - microsoft-bing: Offers comprehensive search features along with suggestions, corrections, and related links.\n"
            "   - bing: Known for search reliability and integration capabilities.\n"
            "   - microsoft-translator: Allows straightforward integration for translating search queries and results, aligning with dual-language operation.\n"
            "   - bing-translator: Complements the search features with translation capabilities.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 2.: ['search', 'translation', 'tools']\n"
            "   - Recommend All matched APIs in 3.: ['microsoft-bing', 'bing', 'microsoft-translator', 'bing-translator']\n"
            "   - Final recommended APIs: ['microsoft-bing', 'bing', 'microsoft-translator', 'bing-translator']\n"
    },
     #5つ目 
        {
        "role": "user",
        "content": 
            "Requirements: A new method of communication involving VOIP/wireless and cable call management phone booth systems. AirCellCall's technical architecture system combines several communication methods into one device that you can use to communicate even if you do not have a cell phone available. Designed to serve the general public, corporate and government entities.\n"
    },
    { 
        "role": "assistant",
        "content":
            "1. **Identify Core Features**:\n"
            "   - **VOIP/Wireless Communication**: The service involves VOIP, which is a core feature for handling voice and telephony services.\n"
            "   - **Call Management**: Requires managing calls, indicating the need for telephony solutions.\n"
            "   - **SMS and Messaging**: Integration for communication might involve SMS and other messaging services.\n"
            "   - **Interoperability Across Devices**: Integration of various communication methods for use without a cell phone suggests the need for versatile messaging and telephony APIs.\n"
            "   - **User Engagement for Public and Corporate Use**: Requires APIs that can scale and offer diverse functionalities for a wide user base, including corporations.\n\n"
            "2. **Identify Relevant API Categories**:\n"
            "   - telephony: Because of VOIP and call management functionalities.\n"
            "   - messaging: For handling SMS and other forms of messaging as part of communication.\n\n"
            "3. **Match APIs from Relevant Categories**:\n"
            "   - **telephony APIs**:\n"
            "       - twilio: Offers a cloud API for voice and SMS communications, catering directly to VOIP needs, scalable and reliable for a wide user base.\n"
            "       - plum-fuse: Provides IVR, outbound calling, and other telephony features suitable for call management.\n"
            "       - myvox: Voice-enable applications, good for handling calls.\n"
            "       - opencnam: Provides access to Caller ID information, complementary to call management.\n"
            "       - kookoo: API for voice and SMS suitable for building telephony apps.\n\n"
            "   - **messaging APIs**:\n"
            "       - twilio-sms: Specifically handles SMS, matches the requirement for SMS messaging support.\n"
            "       - vonage-nexmo-sms: Another API for sending and receiving SMS messages.\n"
            "       - postalmethods: Deals with messaging services through the postal gateway.\n"
            "       - amazon-sns: Provides messaging services including SMS via notifications.\n\n"
            "4. **Select the Most Suitable APIs**:\n"
            "   - twilio: Covers both voice (telephony) and SMS (messaging), making it versatile and well-suited for integrated communication services.\n"
            "   - twilio-sms: Specialized for SMS, directly supports messaging needs aligned with the service requirements.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 2.: ['telephony', 'messaging']\n"
            "   - Recommend All matched APIs in 3.: ['twilio', 'plum-fuse', 'myvox', 'opencnam', 'kookoo', 'twilio-sms', 'vonage-nexmo-sms', 'postalmethods', 'amazon-sns']\n"
            "   - Final recommended APIs: ['twilio', 'twilio-sms']\n"
    }
]