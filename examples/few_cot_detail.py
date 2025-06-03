#few_shot_examples_infer　説明の詳細化を追加
#使用サービス：bible-mapped, wishgenies, RADAAR, 2lingual-bing-search, aircellcall
few_shot_examples_detail = [
    {
        "role": "user",
        "content": 
            "Requirements: Mashup showing locations of 200 places mentioned in the Bible. Going for accuracy they try to pinpoint the locations of the ruins of ancient cities instead of using the locations of modern cities with ancient names.\n"
    },
    #一つ目
    {   
        "role": "assistant",
        "content":
            "1. **Expanding Requirements**:\n"
            "   - The mashup service's goal is to create an accurate informational display of 200 locations based on places mentioned in the Bible, emphasizing historical and archaeological accuracy rather than modern city parallels. This involves mapping features to correctly locate ancient ruins or sites and a reference system to authenticate these locations according to their biblical context.\n\n"
            "2. **Identify Core Features**:\n"
            "   - Mapping Functionality: To pinpoint the geographical locations of ancient ruins and accurately represent them on a map.\n"
            "   - Reference Data: To accurately cross-reference and retrieve data related to biblical places for validation and information accuracy.\n\n"
            "3. **Identify Relevant API Categories**:\n"
            "   - mapping: Essential to provide services like geolocation, mapping, and spatial data needed for accurately plotting ancient biblical sites.\n"
            "   - reference: Necessary to link historical and archaeological data with biblical texts for accurate identification and verification of the locations.\n\n"
            "4. **Match APIs from Relevant Categories**:\n"
            "   - **mapping APIs**:\n"
            "       - google-maps: A powerful tool for mapping and geolocation that supports detailed geospatial data visualization and location pinpointing.\n"
            "       - bing-maps: Provides comprehensive mapping facilities and geolocation services which can support the mashup's requirement for precise location mapping.\n"
            "       - mapquest: Offers mapping and geolocation services that could also be considered for alternatives.\n"
            "       - openstreetmap: A useful resource for detailed and freely-accessible mapping data.\n\n"
            "   - **reference APIs**:\n"
            "       - esv-bible-lookup: Directly supports fetching biblical texts and their correlations, vital for referencing and validating biblical locations.\n"
            "       - dbpedia: Can be used for structured data extraction related to biblical sites.\n"
            "       - wolfram-alpha: Offers computational knowledge that might support historical and biblical reference data needs.\n"
            "       - wikipedia: Provides access to a comprehensive range of historical data including references to biblical sites.\n\n"
            "5. **Select the Most Suitable APIs**:\n"
            "   - google-maps: Chosen for its superior mapping capabilities, up-to-date data, and robust API support for integrating maps with pinpoint accuracy.\n"
            "   - esv-bible-lookup: Chosen for its direct support for fetching textual and contextual biblical references, essential for validating and referencing biblical locations.\n\n"
            "### Conclusion:\n"
            "   - Recommended categories from 3.: ['mapping', 'reference']\n"
            "   - Recommended All matched APIs in 4.: ['google-maps', 'bing-maps', 'mapquest', 'esv-bible-lookup', 'openstreetmap', 'wolfram-alpha', 'wikipedia']\n"
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
            "1. **Expanding Requirements**:\n"
            "   - WishGenies is a unique mashup service designed to provide personalized gift recommendations for users' shopping lists. This service leverages preference data from individuals who share common interests with the gift recipients, enhancing the relevance and appeal of the suggestions. The goal of WishGenies is to simplify the gift selection process by offering curated, high-quality gift ideas that align with the recipient's tastes. Core functionalities include user profile management for capturing and analyzing recipient preferences, integration with e-commerce platforms to access vast product catalogs, and social network data mining to identify users with similar interest profiles.\n\n"
            "2. **Identify Core Features**:\n"
            "   - **user Profile Management**: Critical for storing and processing recipient preferences to offer tailored gift suggestions.\n"
            "   - **ecommerce Integration**: Necessary for accessing and displaying a wide range of products.\n"
            "   - **social Network Data Integration**: Important for identifying and leveraging interest data from users with similar preferences.\n\n"
            "3. **Identify Relevant API Categories**:\n"
            "   - social: To access data from users with similar interests for personalized recommendations.\n"
            "   - ecommerce: To retrieve and present product information for the gift recommendations.\n\n"
            "4. **Match APIs from Relevant Categories**:\n"
            "   - **social APIs**:\n"
            "       - facebook-graph: Provides access to data from Facebook's social network, crucial for identifying users with similar interests.\n"
            "       - linkedin: Offers access to social data but may not directly cater to personal interests as required.\n\n"
            "   - **ecommerce APIs**:\n"
            "       - amazon-product-advertising: Comprehensive access to Amazon's vast product catalog, essential for sourcing and displaying potential gifts.\n"
            "       - woocommerce: Good for e-commerce integration, but may not offer the same breadth of products as Amazon.\n"
            "       - shopify-admin: Offers product data but may require more integration effort compared to Amazon for a wider audience reach.\n\n"
            "5. **Select the Most Suitable APIs**:\n"
            "   - facebook-graph: Best suited for accessing social graph data to connect users with similar gifting preferences.\n"
            "   - amazon-product-advertising: Ideal due to the extensive range of products and established integration capabilities.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 3.: ['social', 'ecommerce']\n"
            "   - Recommend All matched APIs in 4.: ['facebook-graph','linkedin', 'amazon-product-advertising', 'woocommerce', 'shopify-admim']\n"
            "   - Final recommended APIs: ['facebook-graph', 'amazon-product-advertising']\n"
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
            "1. **Expanding Requirements**:\n"
            "   - RADAAR is a social media management platform aimed at multiple brands, streamlining workflows, and offering tools for post-scheduling, publishing, social inbox management, monitoring, and analytics. The goal is to simplify social media management for businesses of all sizes and provide comprehensive analytics and monitoring capabilities.\n\n"
            "2. **Identify Core Features**:\n"
            "   - **Social Media Interaction**: To manage multiple social media accounts and brands, interact with platforms such as Facebook, Instagram, Twitter, and LinkedIn.\n"
            "   - **Content Publishing**: Scheduling and publishing capabilities for posts across multiple channels.\n"
            "   - **Analytics and Monitoring**: Tools for monitoring brand mentions, analyzing performance, and gaining insights from social media analytics.\n"
            "   - **Multimedia Handling**: Support for handling photos and videos within the social media context as part of publishing and engagement.\n\n"
            "3. **Identify Relevant API Categories**:\n"
            "   - social: Interfaces with platforms like Facebook, Instagram, Twitter, and LinkedIn are crucial for social media management.\n"
            "   - photos: Required for handling photo-related content on platforms like Instagram.\n"
            "   - video: Essential for managing video content on platforms like YouTube and Vimeo. These platforms are also a part of the social media engagement and content strategies.\n\n"
            "4. **Match APIs from Relevant Categories**:\n"
            "   - **social APIs**:\n"
            "       - twitter: Allows interaction with Twitter data and services, useful for managing postings and analytics.\n"
            "       - facebook: Provides integration with Facebook social graph for posting, monitoring, and analytics.\n"
            "       - linkedin: Essential for managing professional social content.\n\n"
            "   - **photos APIs**:\n"
            "       - instagram-graph: Manages photo content specific to Instagram, blending photo management with social capabilities.\n"
            "       - flickr: While not initially listed as a goal, it is relevant for extended photo content handling but not necessarily essential.\n\n"
            "   - **video APIs**:\n"
            "       - youtube: Supports YouTube video management for content uploading and engagement.\n"
            "       - vimeo: Similar to YouTube but catering to a different audience and purpose in video content provision.\n\n"
            "5. **Select the Most Suitable APIs**:\n"
            "   - twitter: Integral for comprehensive social media management on this major network.\n"
            "   - instagram-graph**: Provides both social and photo management features essential for RADAAR.\n"
            "   - facebook: Critical for handling Facebook-specific content, social activity, and monitoring.\n"
            "   - linkedin: Needed for professional network management.\n"
            "   - youTube: Necessary for integration and video content management.\n"
            "   - vimeo: Also necessary for hosting and managing video content alongside YouTube.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 3.: ['social', 'photos', 'video']\n"
            "   - Recommend All matched APIs in 4.: ['twitter', 'facebook', 'linkedin', 'instagram-graph', 'flickr', 'youtube', 'vimeo']\n"
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
            "1. **Expanding Requirements**:\n"
            "   - The mashup service will be called \"2lingual Bing Search,\" which offers dual-language search capabilities by performing both a Bing Search and a Cross-language Bing Search. Users can enable or disable a translation feature for cross-language searches, ensuring that results from two chosen languages are presented side by side. Additional expected functionalities will include Search Suggestions, Spelling Corrections, Cached Pages, and Related Search Links. This will provide users with a comprehensive tool for multilingual search queries, enhancing user experience by presenting streamlined search results in multiple languages.\n\n"
            "2. **Identify Core Features**:\n"
            "   - **Multilingual Search**: Required to perform searches in two different languages at the same time.\n"
            "   - **Cross-Language Search**: Important to handle queries in one language and retrieve results in another.\n"
            "   - **Query Translation**: Necessary for the cross-language part to translate queries from one language to another.\n"
            "   - **Search Suggestions**: Helps users with query formulation by providing suggestions.\n"
            "   - **Spelling Corrections**: Ensures accuracy in search results by correcting any typos.\n"
            "   - **Cached Pages**: Allows access to cached versions of web pages.\n"
            "   - **Related Search Links**: Provides links to related searches for expanded results.\n\n"
            "3. **Identify Relevant API Categories**:\n"
            "   - search: To facilitate web searches in various languages and formats.\n"
            "   - translation: Required to translate queries between different languages.\n"
            "   - tools: To manage and enhance the presentation and handling of search data.\n\n"
            "4. **Match APIs from Relevant Categories**:\n"
            "   - **search APIs**:\n"
            "       - bing: Capable of handling regular and advanced search operations including suggestions.\n"
            "       - microsoft-bing: Provides powerful search capabilities similar to Bing API.\n\n"
            "   - **translation APIs**:\n"
            "       - microsoft-translator: Provides a robust suite of translation services for handling multiple languages.\n\n"
            "   - **tools API**s:\n"
            "       - datadog: Offers data management utilities that could assist with translation and search data organization.\n"
            "       - zapier: Enables the integration and automation of tools for optimized workflow.\n\n"
            "       - bing-translator: Offers translation capabilities needed for cross-language search.\n"
            "5. **Select the Most Suitable APIs**:\n"
            "   - bing: Directly fits the need for a traditional web search service within two languages.\n"
            "   - microsoft-bing: Ensures comprehensive search capability and complements Bing.\n"
            "   - bing-translator: Enables cross-language query translation and supports multilingual interactions.\n"
            "   - microsoft-translator: Provides enhanced translation services necessary for cross-language operations.\n\n"
            "### Conclusion:\n"
            "   - Recommended categories from 3.: ['search', 'translation', 'tools']\n"
            "   - Recommended All matched APIs in 4.: ['bing', 'microsoft-bing', 'bing-translator', 'microsoft-translator', 'datadog', 'zapier']\n"
            "   - Final recommended APIs: ['bing', 'microsoft-bing', 'bing-translator', 'microsoft-translator']\n"
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
            "1. **Expanding Requirements**:\n"
            "   - The mashup service aims to provide a comprehensive communication platform leveraging VOIP/wireless and cable call management systems. The goal is to facilitate communication without needing a personal cell phone, targeting the general public, corporates, and government entities. It should integrate multiple communication methods to operate as an advanced phone booth system, enabling calls and messages to be sent wirelessly and through cable networks.\n\n"
            "2. **Identify Core Features**:\n"
            "   - VOIP Integration: The service must support voice calling over the internet, minimizing the need for traditional phone lines.\n"
            "   - Messaging Capabilities: To allow for sending and receiving text messages as a form of communication.\n"
            "   - Call Management: Features for managing incoming and outgoing calls efficiently, possibly including call queuing and IVR systems.\n\n"
            "3. **Identify Relevant API Categories**:\n"
            "   - telephony: To support VOIP calling and integrate voice applications.\n"
            "   - messaging: Required for SMS and other messaging capabilities to complement VOIP.\n\n"
            "4. **Match APIs from Relevant Categories**:\n"
            "   - **telephony APIs**:\n"
            "       - twilio: Offers a robust telephony infrastructure for VOIP and advanced voice communications, widely used for such applications.\n"
            "       - plum-fuse: Provides cloud-based telephony services including IVR and call routing, suitable for a phone booth system.\n"
            "       - opencnam: Useful for accessing caller ID information, could enhance call management features.\n\n"
            "   - **messaging APIs**:\n"
            "       - twilio-sms: Specially designed for integrating SMS capabilities, supports sending and receiving messages.\n"
            "       - postalmethods: Offers services for sending physical mail, which can be useful for message delivery in varied formats.\n"
            "       - vonage-nexmo-sms: Provides global SMS sending capabilities, useful for a broad audience reach.\n\n"
            "5. **Select the Most Suitable APIs**:\n"
            "   - twilio: Select for its comprehensive cloud telephony services, which encompass VOIP and messaging, aligning with both telephony and messaging needs.\n"
            "   - twilio-sms: Specifically tailored for SMS integration, perfectly meeting the messaging feature requirement.\n\n"
            "### Conclusion:\n"
            "   - Recommend categories from 3.: ['telephony', 'messaging']\n"
            "   - Recommend All matched APIs in 4.: ['twilio', 'plum-fuse', 'opencnam', 'twilio-sms', 'postalmethods', 'vonage-nexmo-sms']\n"
            "   - Final recommended APIs: ['twilio', 'twilio-sms']\n"
    }
]