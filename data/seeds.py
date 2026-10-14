"""
FIELDAI Database Seeds & Knowledge Engine
Contains authentic agronomic data for Indian agriculture:
- Diseases & Pests (ICAR / PAU / IARI guidelines) with full English, Punjabi & Hindi localized text
- CIBRC approved agrochemical treatments & bio-controls
- APMC Mandi price benchmarks & MSP 2026-27
- Soil health parameters
- Agro-meteorological advisory logic
- Multi-language UI dictionaries (English, Punjabi, Hindi)
- Demo farmer profiles & UPI Gateway Configuration
"""

# Complete Directory of all 33 Districts, Cities and Agricultural Hubs of Punjab
PUNJAB_CITIES = [
    {"id": "ludhiana", "name": "Ludhiana", "name_pa": "ਲੁਧਿਆਣਾ", "name_hi": "लुधियाना", "temp": 24, "hum": 68, "wind": 8, "rain": 12, "spray": 88, "market": "Khanna & Ludhiana Mandi"},
    {"id": "amritsar", "name": "Amritsar", "name_pa": "ਅੰਮ੍ਰਿਤਸਰ", "name_hi": "अमृतसर", "temp": 23, "hum": 70, "wind": 9, "rain": 15, "spray": 85, "market": "Bhagtanwala Grain Market"},
    {"id": "jalandhar", "name": "Jalandhar", "name_pa": "ਜਲੰਧਰ", "name_hi": "जालंधर", "temp": 24, "hum": 66, "wind": 7, "rain": 10, "spray": 90, "market": "Maqsudan Sabzi & Potato Mandi"},
    {"id": "patiala", "name": "Patiala", "name_pa": "ਪਟਿਆਲਾ", "name_hi": "पटियाला", "temp": 25, "hum": 65, "wind": 8, "rain": 14, "spray": 87, "market": "Patiala & Rajpura Mandi"},
    {"id": "bathinda", "name": "Bathinda", "name_pa": "ਬਠਿੰਡਾ", "name_hi": "बठिंडा", "temp": 26, "hum": 58, "wind": 10, "rain": 8, "spray": 92, "market": "Bathinda Cotton & Wheat Yard"},
    {"id": "khanna", "name": "Khanna", "name_pa": "ਖੰਨਾ", "name_hi": "खन्ना", "temp": 24, "hum": 67, "wind": 8, "rain": 10, "spray": 89, "market": "Asia's Largest Grain Market"},
    {"id": "abohar", "name": "Abohar", "name_pa": "ਅਬੋਹਰ", "name_hi": "अबोहर", "temp": 27, "hum": 54, "wind": 11, "rain": 5, "spray": 94, "market": "Abohar Cotton & Kinnow Mandi"},
    {"id": "sangrur", "name": "Sangrur", "name_pa": "ਸੰਗਰੂਰ", "name_hi": "संगरूर", "temp": 25, "hum": 64, "wind": 8, "rain": 12, "spray": 88, "market": "Sunam & Sangrur Grain Terminal"},
    {"id": "moga", "name": "Moga", "name_pa": "ਮੋਗਾ", "name_hi": "मोगा", "temp": 24, "hum": 65, "wind": 9, "rain": 10, "spray": 89, "market": "Moga Main Wheat Market"},
    {"id": "muktsar", "name": "Sri Muktsar Sahib", "name_pa": "ਸ੍ਰੀ ਮੁਕਤਸਰ ਸਾਹਿਬ", "name_hi": "श्री मुक्तसर साहिब", "temp": 26, "hum": 60, "wind": 9, "rain": 7, "spray": 91, "market": "Muktsar Cotton & Grain Market"},
    {"id": "hoshiarpur", "name": "Hoshiarpur", "name_pa": "ਹੁਸ਼ਿਆਰਪੁਰ", "name_hi": "होशियारपुर", "temp": 22, "hum": 74, "wind": 7, "rain": 20, "spray": 80, "market": "Hoshiarpur Citrus & Grain Mandi"},
    {"id": "mohali", "name": "SAS Nagar (Mohali)", "name_pa": "ਸਾਸ ਨਗਰ (ਮੋਹਾਲੀ)", "name_hi": "मोहाली", "temp": 24, "hum": 66, "wind": 8, "rain": 12, "spray": 88, "market": "Kharar & Lalru Agri Mandi"},
    {"id": "firozpur", "name": "Firozpur", "name_pa": "ਫ਼ਿਰੋਜ਼ਪੁਰ", "name_hi": "फिरोज़पुर", "temp": 25, "hum": 69, "wind": 9, "rain": 11, "spray": 86, "market": "Firozpur Cantt Grain Market"},
    {"id": "fazilka", "name": "Fazilka", "name_pa": "ਫ਼ਾਜ਼ਿਲਕਾ", "name_hi": "फाज़िल्का", "temp": 26, "hum": 56, "wind": 10, "rain": 6, "spray": 93, "market": "Fazilka Border Cotton Mandi"},
    {"id": "gurdaspur", "name": "Gurdaspur", "name_pa": "ਗੁਰਦਾਸਪੁਰ", "name_hi": "गुरदासपुर", "temp": 22, "hum": 76, "wind": 8, "rain": 22, "spray": 78, "market": "Gurdaspur Sugarcane & Paddy Yard"},
    {"id": "pathankot", "name": "Pathankot", "name_pa": "ਪਠਾਨਕੋਟ", "name_hi": "पठानकोट", "temp": 21, "hum": 78, "wind": 7, "rain": 25, "spray": 76, "market": "Pathankot Foothill Agri Market"},
    {"id": "tarn_taran", "name": "Tarn Taran", "name_pa": "ਤਰਨ ਤਾਰਨ", "name_hi": "तरन तारण", "temp": 23, "hum": 71, "wind": 8, "rain": 14, "spray": 84, "market": "Patti & Tarn Taran Mandi"},
    {"id": "faridkot", "name": "Faridkot", "name_pa": "ਫ਼ਰੀਦਕੋਟ", "name_hi": "फरीदकोट", "temp": 25, "hum": 62, "wind": 9, "rain": 9, "spray": 90, "market": "Faridkot Malwa Grain Yard"},
    {"id": "kapurthala", "name": "Kapurthala", "name_pa": "ਕਪੂਰਥਲਾ", "name_hi": "कपूरथला", "temp": 23, "hum": 69, "wind": 7, "rain": 12, "spray": 87, "market": "Sultanpur Lodhi Agri Market"},
    {"id": "mansa", "name": "Mansa", "name_pa": "ਮਾਨਸਾ", "name_hi": "मानसा", "temp": 26, "hum": 57, "wind": 10, "rain": 7, "spray": 92, "market": "Budhlada & Mansa Cotton Mandi"},
    {"id": "barnala", "name": "Barnala", "name_pa": "ਬਰਨਾਲਾ", "name_hi": "बरनाला", "temp": 25, "hum": 63, "wind": 8, "rain": 10, "spray": 89, "market": "Barnala Main Grain Market"},
    {"id": "malerkotla", "name": "Malerkotla", "name_pa": "ਮਾਲੇਰਕੋਟਲਾ", "name_hi": "मलेरकोटला", "temp": 24, "hum": 66, "wind": 8, "rain": 11, "spray": 88, "market": "Punjab's Vegetable Capital Mandi"},
    {"id": "fatehgarh_sahib", "name": "Fatehgarh Sahib", "name_pa": "ਫ਼ਤਹਿਗੜ੍ਹ ਸਾਹਿਬ", "name_hi": "फतेहगढ़ साहिब", "temp": 24, "hum": 67, "wind": 8, "rain": 13, "spray": 87, "market": "Sirhind Grain Market"},
    {"id": "ropar", "name": "Rupnagar (Ropar)", "name_pa": "ਰੂਪਨਗਰ", "name_hi": "रूपनगर", "temp": 23, "hum": 73, "wind": 7, "rain": 18, "spray": 82, "market": "Rupnagar Agri Mandi"},
    {"id": "nawanshahr", "name": "SBS Nagar (Nawanshahr)", "name_pa": "ਨਵਾਂਸ਼ਹਿਰ", "name_hi": "नवांशहर", "temp": 23, "hum": 70, "wind": 8, "rain": 14, "spray": 86, "market": "Banga & Nawanshahr Grain Mandi"},
    {"id": "rajpura", "name": "Rajpura", "name_pa": "ਰਾਜਪੁਰਾ", "name_hi": "राजपुरा", "temp": 25, "hum": 65, "wind": 8, "rain": 12, "spray": 88, "market": "Rajpura Major Grain Terminal"},
    {"id": "batala", "name": "Batala", "name_pa": "ਬਟਾਲਾ", "name_hi": "बटाला", "temp": 22, "hum": 73, "wind": 8, "rain": 19, "spray": 81, "market": "Historic Batala Grain Market"},
    {"id": "phagwara", "name": "Phagwara", "name_pa": "ਫਗਵਾੜਾ", "name_hi": "फगवाड़ा", "temp": 24, "hum": 67, "wind": 7, "rain": 11, "spray": 89, "market": "Phagwara Sugar & Grain Hub"},
    {"id": "kotkapura", "name": "Kotkapura", "name_pa": "ਕੋਟਕਪੂਰਾ", "name_hi": "कोटसपूरा", "temp": 25, "hum": 61, "wind": 9, "rain": 8, "spray": 91, "market": "Kotkapura Premier Grain Market"},
    {"id": "jagraon", "name": "Jagraon", "name_pa": "ਜਗਰਾਉਂ", "name_hi": "जगराओं", "temp": 24, "hum": 66, "wind": 8, "rain": 11, "spray": 88, "market": "Jagraon Main Wheat Mandi"},
    {"id": "nakodar", "name": "Nakodar", "name_pa": "ਨਕੋਦਰ", "name_hi": "नकोदर", "temp": 24, "hum": 67, "wind": 7, "rain": 12, "spray": 88, "market": "Nakodar Doaba Trading Yard"},
    {"id": "sunam", "name": "Sunam", "name_pa": "ਸੁਨਾਮ", "name_hi": "सुनाम", "temp": 25, "hum": 63, "wind": 8, "rain": 10, "spray": 90, "market": "Sunam Grain Market"},
    {"id": "samana", "name": "Samana", "name_pa": "ਸਮਾਣਾ", "name_hi": "समाना", "temp": 25, "hum": 64, "wind": 8, "rain": 12, "spray": 88, "market": "Samana Paddy & Wheat Mandi"}
]

DEMO_FARMERS = [
    {
        "id": "farmer_gill",
        "email": "gillamritpal2007-1@gmail.com",
        "password": "password123",
        "name": "Amritpal Singh Gill",
        "name_pa": "ਅੰਮ੍ਰਿਤਪਾਲ ਸਿੰਘ ਗਿੱਲ",
        "name_hi": "अमृतपाल सिंह गिल",
        "phone": "9876543210",
        "village": "Gill Kalan",
        "village_pa": "ਗਿੱਲ ਕਲਾਂ",
        "village_hi": "गिल कलां",
        "district": "Ludhiana",
        "district_pa": "ਲੁਧਿਆਣਾ",
        "district_hi": "लुधियाना",
        "state": "Punjab",
        "kisan_id": "PB-LDH-2026-0701",
        "total_acres": 18.5,
        "primary_crop": "Wheat, Paddy & Mustard",
        "tubewells": 2,
        "shc_id": "PAU-SHC-2007",
        "upi_id": "gillamritpal2007-1@okicici",
        "lang": "pa"
    },
    {
        "id": "farmer_1",
        "email": "gurpreet.singh@gmail.com",
        "password": "punjab123",
        "name": "Sardar Gurpreet Singh",
        "name_pa": "ਸਰਦਾਰ ਗੁਰਪ੍ਰੀਤ ਸਿੰਘ",
        "name_hi": "सरदार गुरप्रीत सिंह",
        "phone": "9876543211",
        "village": "Bhamian Kalan",
        "village_pa": "ਭਾਮੀਆਂ ਕਲਾਂ",
        "village_hi": "भामियां कलां",
        "district": "Ludhiana",
        "district_pa": "ਲੁਧਿਆਣਾ",
        "district_hi": "लुधियाना",
        "state": "Punjab",
        "kisan_id": "PB-LU-2026-8812",
        "total_acres": 14.5,
        "primary_crop": "Wheat & Mustard",
        "tubewells": 2,
        "shc_id": "PAU-SHC-9042",
        "upi_id": "gillamritpal2007-1@okicici",
        "lang": "pa"
    },
    {
        "id": "farmer_2",
        "email": "ramesh.patel@gmail.com",
        "password": "kisan123",
        "name": "Ramesh Patel",
        "name_pa": "ਰਮੇਸ਼ ਪਟੇਲ",
        "name_hi": "रमेश पटेल",
        "phone": "9812345678",
        "village": "Mogar",
        "village_pa": "ਮੋਗਰ",
        "village_hi": "मोगर",
        "district": "Anand",
        "district_pa": "ਆਨੰਦ",
        "district_hi": "आनंद",
        "state": "Gujarat",
        "kisan_id": "GJ-AN-2026-4421",
        "total_acres": 9.0,
        "primary_crop": "Cotton & Tobacco",
        "tubewells": 1,
        "shc_id": "AAU-SHC-3120",
        "upi_id": "gillamritpal2007-1@okicici",
        "lang": "hi"
    },
    {
        "id": "farmer_3",
        "email": "rajendra.sharma@gmail.com",
        "password": "kisan123",
        "name": "Chaudhary Rajendra Sharma",
        "name_pa": "ਚੌਧਰੀ ਰਾਜੇਂਦਰ ਸ਼ਰਮਾ",
        "name_hi": "चौधरी राजेंद्र शर्मा",
        "phone": "9923456789",
        "village": "Daurala",
        "village_pa": "ਦੌਰਾਲਾ",
        "village_hi": "दौराला",
        "district": "Meerut",
        "district_pa": "ਮੇਰਠ",
        "district_hi": "मेरठ",
        "state": "Uttar Pradesh",
        "kisan_id": "UP-ME-2026-9034",
        "total_acres": 18.0,
        "primary_crop": "Sugarcane & Wheat",
        "tubewells": 3,
        "shc_id": "SVPU-SHC-8819",
        "upi_id": "gillamritpal2007-1@okicici",
        "lang": "hi"
    }
]

CROPS = [
    {
        "id": "wheat",
        "name": "Wheat",
        "name_hi": "गेहूँ",
        "name_pa": "ਕਣਕ",
        "season": "Rabi",
        "stages": ["Seedling (0-20 DAS)", "Crown Root Initiation (21-35 DAS)", "Tillering & Jointing", "Booting & Heading", "Milking & Dough", "Maturity / Harvest"],
        "stages_pa": ["ਪੁੰਗਰਨ (0-20 ਦਿਨ)", "ਤਾਜ ਜੜ੍ਹਾਂ ਨਿਕਲਣਾ (CRI 21-35 ਦਿਨ)", "ਫੁਟਾਰਾ ਤੇ ਗੰਢਾਂ ਬਣਨਾ", "ਗੋਭ ਤੇ ਸਿੱਟੇ ਨਿਕਲਣਾ", "ਦੋਧਾ ਪੜਾਅ", "ਪੱਕਣਾ / ਵਾਢੀ"],
        "stages_hi": ["अंकुरण (0-20 दिन)", "क्राउन रूट (CRI 21-35 दिन)", "कल्ले फूटना व गांठें बनना", "गाभा व बालियां निकलना", "दूधिया अवस्था", "परिपक्वता / कटाई"],
        "icon": "🌾"
    },
    {
        "id": "rice",
        "name": "Rice / Paddy",
        "name_hi": "धान / चावल",
        "name_pa": "ਝੋਨਾ",
        "season": "Kharif",
        "stages": ["Nursery", "Tillering", "Panicle Initiation", "Flowering", "Grain Filling", "Maturity"],
        "stages_pa": ["ਪਨੀਰੀ", "ਫੁਟਾਰਾ", "ਸਿੱਟਾ ਸ਼ੁਰੂਆਤ", "ਬੂਰ ਪੈਣਾ", "ਦਾਣਾ ਭਰਨਾ", "ਪੱਕਣਾ"],
        "stages_hi": ["नर्सरी", "कल्ले फूटना", "बालियां बनना", "फूल आना", "दाना भराव", "परिपक्वता"],
        "icon": "🌾"
    },
    {
        "id": "mustard",
        "name": "Mustard / Rapeseed",
        "name_hi": "सरसों / राई",
        "name_pa": "ਸਰ੍ਹੋਂ",
        "season": "Rabi",
        "stages": ["Seedling", "Vegetative rosette", "Flowering", "Siliqua development", "Maturity"],
        "stages_pa": ["ਪੁੰਗਰਨ", "ਪੱਤੇ ਫੈਲਣਾ", "ਫੁੱਲ ਪੈਣਾ", "ਫਲੀਆਂ ਬਣਨਾ", "ਪੱਕਣਾ"],
        "stages_hi": ["अंकुरण", "वानस्पतिक विकास", "फूल आना", "फलियां बनना", "परिपक्वता"],
        "icon": "🌱"
    },
    {
        "id": "cotton",
        "name": "Cotton",
        "name_hi": "कपास / नरमा",
        "name_pa": "ਨਰਮਾ / ਕਪਾਹ",
        "season": "Kharif",
        "stages": ["Emergence", "Squaring (Bud formation)", "Flowering", "Boll development", "Boll opening"],
        "stages_pa": ["ਪੁੰਗਰਨ", "ਡੋਡੀਆਂ ਬਣਨਾ", "ਫੁੱਲ ਪੈਣਾ", "ਟੀਂਡੇ ਬਣਨਾ", "ਟੀਂਡੇ ਖਿੜਨਾ"],
        "stages_hi": ["अंकुरण", "कलियां बनना", "फूल आना", "टिंडे बनना", "टिंडे खिलना"],
        "icon": "☁️"
    },
    {
        "id": "potato",
        "name": "Potato",
        "name_hi": "आलू",
        "name_pa": "ਆਲੂ",
        "season": "Rabi",
        "stages": ["Sprout development", "Vegetative growth", "Tuber initiation", "Tuber bulking", "Maturation"],
        "stages_pa": ["ਅੱਖਾਂ ਫੁੱਟਣਾ", "ਬੂਟਾ ਵਧਣਾ", "ਆਲੂ ਬਣਨਾ ਸ਼ੁਰੂ", "ਆਲੂ ਮੋਟੇ ਹੋਣਾ", "ਪੱਕਣਾ"],
        "stages_hi": ["अंकुरण", "पौधा वृद्धि", "कंद निर्माण", "कंद फुलाव", "परिपक्वता"],
        "icon": "🥔"
    },
    {
        "id": "tomato",
        "name": "Tomato",
        "name_hi": "टमाटर",
        "name_pa": "ਟਮਾਟਰ",
        "season": "Year-round",
        "stages": ["Seedling/Transplanting", "Vegetative", "First cluster flowering", "Fruit set", "Harvesting"],
        "stages_pa": ["ਪਨੀਰੀ ਲਗਾਉਣਾ", "ਵਧ-ਫੁੱਲ", "ਫੁੱਲ ਪੈਣਾ", "ਟਮਾਟਰ ਲੱਗਣਾ", "ਤੁੜਾਈ"],
        "stages_hi": ["पौध रोपाई", "वानस्पतिक वृद्धि", "फूल आना", "फल लगना", "तुड़ाई"],
        "icon": "🍅"
    },
    {
        "id": "chilli",
        "name": "Chilli / Mirch",
        "name_hi": "मिर्च",
        "name_pa": "ਮਿਰਚ",
        "season": "Rabi/Kharif",
        "stages": ["Transplant", "Branching", "Flowering", "Pod setting", "Ripening"],
        "stages_pa": ["ਰੋਪਾਈ", "ਟਾਹਣੀਆਂ ਫੁੱਟਣਾ", "ਫੁੱਲ ਪੈਣਾ", "ਮਿਰਚਾਂ ਲੱਗਣਾ", "ਲਾਲ ਹੋਣਾ"],
        "stages_hi": ["रोपाई", "शाखाएं निकलना", "फूल आना", "मिर्च लगना", "पकना"],
        "icon": "🌶️"
    },
    {
        "id": "maize",
        "name": "Maize / Corn",
        "name_hi": "मक्का",
        "name_pa": "ਮੱਕੀ",
        "season": "Kharif/Rabi",
        "stages": ["V3-V6 Vegetative", "Knee-high", "Tasseling/Silking", "Blister/Milk", "Physiological maturity"],
        "stages_pa": ["ਸ਼ੁਰੂਆਤੀ ਵਾਧਾ", "ਗੋਡਾ ਉੱਚਾ", "ਬੂਰ ਤੇ ਛੱਲੀ ਨਿਕਲਣਾ", "ਦੁੱਧ ਭਰਨਾ", "ਪੱਕਣਾ"],
        "stages_hi": ["प्रारंभिक वृद्धि", "घुटने तक ऊंचाई", "मंजरी व भुट्टा आना", "दूधिया अवस्था", "परिपक्वता"],
        "icon": "🌽"
    }
]

DISEASES = [
    {
        "id": "wheat_yellow_rust",
        "crop_id": "wheat",
        "name": "Yellow Rust (Stripe Rust)",
        "name_hi": "पीला रतुआ (स्ट्राइप रस्ट)",
        "name_pa": "ਪੀਲੀ ਕੁੰਗੀ (ਸਟ੍ਰਾਈਪ ਰਸਟ)",
        "scientific_name": "Puccinia striiformis f. sp. tritici",
        "severity": "Critical",
        "severity_pa": "ਗੰਭੀਰ (Critical)",
        "severity_hi": "गंभीर (Critical)",
        "severity_color": "#DC2626",
        "confidence_base": 94.8,
        "sample_image": "/static/img/samples/wheat_yellow_rust.jpg",
        "symptoms": [
            "Bright yellow pustules (uredinia) arranged in distinct parallel stripes along leaf veins",
            "Yellow powdery fungal spores visible on fingers upon touching infected leaves",
            "Chlorosis and drying of leaf tips proceeding downward",
            "Reduced chlorophyll resulting in poor grain filling and shriveled grains"
        ],
        "symptoms_pa": [
            "ਪੱਤਿਆਂ ਦੀਆਂ ਨਾੜਾਂ ਦੇ ਸਮਾਨਾਂਤਰ ਪੀਲੀਆਂ ਧਾਰੀਆਂ ਵਿੱਚ ਉੱਭਰੇ ਹੋਏ ਪੀਲੇ ਦਾਣੇ (ਪਸਟਿਊਲ)",
            "ਪੱਤਿਆਂ ਨੂੰ ਹੱਥ ਲਗਾਉਣ 'ਤੇ ਉਂਗਲੀਆਂ 'ਤੇ ਹਲਦੀ ਵਰਗਾ ਪੀਲਾ ਪਾਊਡਰ ਲੱਗਣਾ",
            "ਪੱਤਿਆਂ ਦੇ ਸਿਰਿਆਂ ਦਾ ਪੀਲਾ ਪੈ ਕੇ ਸੁੱਕਣਾ",
            "ਫ਼ਸਲ ਵਿੱਚ ਪ੍ਰਕਾਸ਼ ਸੰਸਲੇਸ਼ਣ ਘਟਣ ਕਾਰਨ ਦਾਣਿਆਂ ਦਾ ਬਰੀਕ ਰਹਿ ਜਾਣਾ"
        ],
        "symptoms_hi": [
            "पत्तियों की शिराओं के समानांतर स्पष्ट पीली धारियों में उभरे हुए फफोले",
            "संक्रमित पत्तियों को छूने पर उंगलियों पर हल्दी जैसा पीला पाउडर चिपकना",
            "पत्तियों के सिरों का पीला पड़कर सूखना",
            "प्रकाश संश्लेषण कम होने से दाने सिकुड़ना और हल्का होना"
        ],
        "likely_causes": [
            "Cool temperatures ranging between 10°C to 18°C combined with frequent morning dew or fog",
            "Continuous relative humidity above 85% for more than 48 hours",
            "Susceptible varieties sown without resistant certified seed blends",
            "Windborne spore migration from Sub-Himalayan foothill plains"
        ],
        "likely_causes_pa": [
            "ਤਾਪਮਾਨ 10°C ਤੋਂ 18°C ਵਿਚਕਾਰ ਰਹਿਣਾ ਅਤੇ ਸਵੇਰ ਵੇਲੇ ਭਾਰੀ ਤਰੇਲ ਜਾਂ ਧੁੰਦ",
            "ਲਗਾਤਾਰ 48 ਘੰਟਿਆਂ ਤੋਂ ਵੱਧ ਸਮੇਂ ਲਈ ਹਵਾ ਵਿੱਚ 85% ਤੋਂ ਵੱਧ ਨਮੀ ਰਹਿਣਾ",
            "ਗੈਰ-ਪ੍ਰਮਾਣਿਤ ਪੁਰਾਣੇ ਬੀਜਾਂ ਦੀ ਬਿਜਾਈ",
            "ਹਿਮਾਲਿਆ ਦੇ ਪਹਾੜੀ ਇਲਾਕਿਆਂ ਵੱਲੋਂ ਹਵਾ ਰਾਹੀਂ ਉੱਲੀ ਦੇ ਕਣਾਂ ਦਾ ਆਉਣਾ"
        ],
        "likely_causes_hi": [
            "तापमान 10°C से 18°C के बीच रहना और सुबह भारी ओस या कोहरा",
            "लगातार 48 घंटे से अधिक समय तक 85% से अधिक सापेक्ष आर्द्रता",
            "रोगग्राही किस्मों की बिना बीजोपचार बुवाई",
            "तराई व पहाड़ी क्षेत्रों से हवा द्वारा बीजाणुओं का फैलाव"
        ],
        "recommended_steps": [
            "Immediately spray Propiconazole 25% EC (Tilt) @ 200 ml or Tebuconazole + Trifloxystrobin (Nativo) @ 120 g in 200L water per acre.",
            "Repeat spray after 12-15 days if cloudy, cool weather persists.",
            "Avoid overhead irrigation or flood irrigation during heavy dew mornings.",
            "Notify your local Krishi Vigyan Kendra (KVK) or Block Agriculture Officer if widespread infestation occurs."
        ],
        "recommended_steps_pa": [
            "ਤੁਰੰਤ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ 25% EC (ਟਿਲਟ / Tilt) @ 200 ਮਿ.ਲੀ. ਜਾਂ ਨੈਟਿਵੋ (Nativo) @ 120 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ 200 ਲੀਟਰ ਪਾਣੀ ਵਿੱਚ ਮਿਲਾ ਕੇ ਛਿੜਕਾਅ ਕਰੋ।",
            "ਜੇਕਰ ਬੱਦਲਵਾਈ ਅਤੇ ਠੰਢਾ ਮੌਸਮ ਬਣਿਆ ਰਹੇ ਤਾਂ 12-15 ਦਿਨਾਂ ਬਾਅਦ ਦੂਜਾ ਸਪਰੇਅ ਕਰੋ।",
            "ਸਵੇਰ ਦੀ ਭਾਰੀ ਤਰੇਲ ਵੇਲੇ ਖੇਤ ਵਿੱਚ ਭਾਰੀ ਸਿੰਚਾਈ ਕਰਨ ਤੋਂ ਬਚੋ।",
            "ਜੇਕਰ ਬਿਮਾਰੀ ਵੱਧ ਫੈਲੇ ਤਾਂ ਆਪਣੇ ਨੇੜਲੇ ਖੇਤੀਬਾੜੀ ਦਫ਼ਤਰ ਜਾਂ ਕੇ.ਵੀ.ਕੇ. (KVK) ਨੂੰ ਸੂਚਿਤ ਕਰੋ।"
        ],
        "recommended_steps_hi": [
            "तत्काल प्रोपिकोनाजोल 25% EC (टिल्ट) 200 मिली अथवा नेटिवो 120 ग्राम प्रति एकड़ 200 लीटर पानी में मिलाकर छिड़काव करें।",
            "यदि मौसम ठंडा और बादलों भरा रहे तो 12-15 दिन बाद दोबारा स्प्रे करें।",
            "सुबह तेज ओस के समय खेत में भारी पानी देने से बचें।",
            "अधिक प्रकोप होने पर अपने स्थानीय कृषि विज्ञान केंद्र (KVK) से संपर्क करें।"
        ],
        "prevention_tips": [
            "Adopt rust-resistant PAU varieties such as PBW-826, PBW-725, or DBW-187/303 for future sowings.",
            "Avoid late sowing after November 25 in northern plains.",
            "Treat seeds before sowing with Trichoderma viride or Carboxin + Thiram."
        ],
        "prevention_tips_pa": [
            "ਅੱਗੇ ਤੋਂ ਪੀਲੀ ਕੁੰਗੀ ਦਾ ਟਾਕਰਾ ਕਰਨ ਵਾਲੀਆਂ ਪੀ.ਏ.ਯੂ. ਕਿਸਮਾਂ ਜਿਵੇਂ ਕਿ PBW-826, PBW-725 ਜਾਂ DBW-187 ਦੀ ਬਿਜਾਈ ਕਰੋ।",
            "25 ਨਵੰਬਰ ਤੋਂ ਬਾਅਦ ਪਛੇਤੀ ਬਿਜਾਈ ਕਰਨ ਤੋਂ ਪਰਹੇਜ਼ ਕਰੋ।",
            "ਬਿਜਾਈ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜ ਨੂੰ ਟ੍ਰਾਈਕੋਡਰਮਾ ਜਾਂ ਕਾਰਬਾਕਸਿਨ ਨਾਲ ਸੋਧੋ।"
        ],
        "prevention_tips_hi": [
            "आगामी बुवाई में रतुआ प्रतिरोधी किस्में जैसे PBW-826, PBW-725 या DBW-187/303 का चयन करें।",
            "उत्तरी मैदानों में 25 नवंबर के बाद पछेती बुवाई से बचें।",
            "बुवाई से पूर्व ट्राइकोडर्मा विरिडी अथवा फफूंदनाशक से बीजोपचार अवश्य करें।"
        ],
        "treatment_product_ids": ["prod_tilt", "prod_nativo", "prod_amistar"],
        "bounding_boxes": [
            {"x": 18, "y": 24, "w": 42, "h": 55, "label": "Yellow Uredinia Stripes", "confidence": 0.96},
            {"x": 58, "y": 38, "w": 32, "h": 46, "label": "Sporulating Chlorosis", "confidence": 0.92}
        ]
    },
    {
        "id": "rice_blast",
        "crop_id": "rice",
        "name": "Rice Blast (Leaf & Neck Blast)",
        "name_hi": "धान का झुलसा रोग (ब्लास्ट)",
        "name_pa": "ਝੋਨੇ ਦਾ ਬਲਾਸਟ ਰੋਗ (ਧੌਣ ਤੋੜ)",
        "scientific_name": "Magnaporthe oryzae (Pyricularia oryzae)",
        "severity": "Critical",
        "severity_pa": "ਗੰਭੀਰ (Critical)",
        "severity_hi": "गंभीर (Critical)",
        "severity_color": "#DC2626",
        "confidence_base": 96.2,
        "sample_image": "/static/img/samples/rice_blast.jpg",
        "symptoms": [
            "Spindle-shaped / diamond-shaped lesions with greyish-white center and distinct reddish-brown borders",
            "Lesions enlarge and coalesce, causing entire leaf blades to blast and wither",
            "Blackish necrotic ring at panicle base ('neck blast') leading to empty chaffy panicles"
        ],
        "symptoms_pa": [
            "ਪੱਤਿਆਂ 'ਤੇ ਵਿਚਕਾਰੋਂ ਸੁਆਹ ਰੰਗੇ ਅਤੇ ਕੰਢਿਆਂ ਤੋਂ ਲਾਲ-ਭੂਰੇ ਹੀਰੇ ਵਰਗੇ (ਤ੍ਰਿਕੋਣੇ) ਧੱਬੇ",
            "ਧੱਬੇ ਆਪਸ ਵਿੱਚ ਜੁੜ ਕੇ ਪੂਰੇ ਪੱਤੇ ਨੂੰ ਸੁਕਾ ਦਿੰਦੇ ਹਨ",
            "ਸਿੱਟੇ ਦੇ ਮੁੱਢ 'ਤੇ ਕਾਲਾ ਧੱਬਾ ਪੈਣਾ ਜਿਸ ਨਾਲ ਸਿੱਟਾ ਟੁੱਟ ਜਾਂਦਾ ਹੈ ਅਤੇ ਦਾਣੇ ਫੋਕੇ ਰਹਿ ਜਾਂਦੇ ਹਨ"
        ],
        "symptoms_hi": [
            "पत्तियों पर मध्य में धूसर-सफेद और किनारों पर लाल-भूरे नाव या हीरे के आकार के धब्बे",
            "धब्बों के आपस में मिलने से पूरी पत्ती झुलसकर सूख जाती है",
            "बाली के आधार पर काला घेरा पड़ना (गर्दन तोड़) जिससे बालियां खाली और सफेद हो जाती हैं"
        ],
        "likely_causes": [
            "Intermittent rains, cloud cover, and relative humidity exceeding 90%",
            "Night temperatures dropping to 19-23°C",
            "Excessive nitrogenous fertilizers without adequate potassium"
        ],
        "likely_causes_pa": [
            "ਰੁਕ-ਰੁਕ ਕੇ ਮੀਂਹ, ਬੱਦਲਵਾਈ ਅਤੇ 90% ਤੋਂ ਵੱਧ ਹਵਾ ਵਿੱਚ ਨਮੀ",
            "ਰਾਤ ਦਾ ਤਾਪਮਾਨ 19-23°C ਤੱਕ ਡਿੱਗਣਾ",
            "ਬਿਨਾਂ ਪੋਟਾਸ਼ ਦੇ ਯੂਰੀਆ ਖਾਦ ਦੀ ਬਹੁਤ ਜ਼ਿਆਦਾ ਵਰਤੋਂ"
        ],
        "likely_causes_hi": [
            "रुक-रुक कर बारिश, बदली का मौसम और 90% से अधिक आर्द्रता",
            "रात का तापमान 19-23°C के बीच गिरना",
            "पोटाश के बिना अत्यधिक यूरिया का अंधाधुंध उपयोग"
        ],
        "recommended_steps": [
            "Foliar spray of Tricyclazole 75% WP @ 120 g/acre or Isoprothiolane 40% EC @ 300 ml/acre in 200L water.",
            "In severe panicle emergence cases, spray Nativo (Tebuconazole + Trifloxystrobin) @ 100 g/acre.",
            "Withhold nitrogen top-dressing until disease spread is arrested."
        ],
        "recommended_steps_pa": [
            "ਟ੍ਰਾਈਸਾਈਕਲਾਜ਼ੋਲ 75% WP @ 120 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ ਜਾਂ ਨੈਟਿਵੋ (Nativo) @ 100 ਗ੍ਰਾਮ 200 ਲੀਟਰ ਪਾਣੀ ਵਿੱਚ ਮਿਲਾ ਕੇ ਸਪਰੇਅ ਕਰੋ।",
            "ਜਦੋਂ ਤੱਕ ਬਿਮਾਰੀ ਕੰਟਰੋਲ ਨਾ ਹੋਵੇ, ਯੂਰੀਆ ਖਾਦ ਪਾਉਣਾ ਤੁਰੰਤ ਬੰਦ ਕਰੋ।",
            "ਖੇਤ ਵਿੱਚੋਂ ਪਾਣੀ ਬਦਲੋ ਤਾਂ ਜੋ ਜੜ੍ਹਾਂ ਨੂੰ ਹਵਾ ਲੱਗ ਸਕੇ।"
        ],
        "recommended_steps_hi": [
            "ट्राइसाइक्लाजोल 75% WP @ 120 ग्राम अथवा नेटिवो @ 100 ग्राम प्रति एकड़ 200 लीटर पानी में मिलाकर स्प्रे करें।",
            "रोग नियंत्रण में आने तक यूरिया का छिड़काव पूरी तरह रोक दें।",
            "खेत का जमा पानी 2-3 दिन के लिए निकाल दें।"
        ],
        "prevention_tips": [
            "Seed treatment with Tricyclazole 75% WP @ 2g/kg seed before sowing.",
            "Maintain proper field drainage and avoid continuous stagnant deep water."
        ],
        "prevention_tips_pa": [
            "ਬਿਜਾਈ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜ ਨੂੰ ਟ੍ਰਾਈਸਾਈਕਲਾਜ਼ੋਲ @ 2 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਕਿੱਲੋ ਨਾਲ ਸੋਧੋ।",
            "ਖੇਤ ਵਿੱਚ ਲਗਾਤਾਰ ਡੂੰਘਾ ਪਾਣੀ ਖੜ੍ਹਾ ਨਾ ਰਹਿਣ ਦਿਓ।"
        ],
        "prevention_tips_hi": [
            "बुवाई से पूर्व ट्राइसाइक्लाजोल 2 ग्राम/किग्रा बीज दर से बीजोपचार करें।",
            "खेत में लगातार गहरा पानी खड़ा न रहने दें।"
        ],
        "treatment_product_ids": ["prod_nativo", "prod_amistar", "prod_saaf"],
        "bounding_boxes": [
            {"x": 22, "y": 18, "w": 38, "h": 45, "label": "Diamond Blast Lesion", "confidence": 0.97},
            {"x": 52, "y": 42, "w": 36, "h": 40, "label": "Spindle Necrosis", "confidence": 0.94}
        ]
    },
    {
        "id": "cotton_leaf_curl",
        "crop_id": "cotton",
        "name": "Cotton Leaf Curl Virus (CLCuV)",
        "name_hi": "कपास का पत्ती मरोड़ रोग",
        "name_pa": "ਨਰਮੇ ਦਾ ਚਿੱਟਾ ਮੱਖੀ / ਪੱਤਾ ਮਰੋੜ ਰੋਗ",
        "scientific_name": "Cotton leaf curl virus (Begomovirus / Whitefly vector)",
        "severity": "High",
        "severity_pa": "ਵੱਧ (High)",
        "severity_hi": "उच्च (High)",
        "severity_color": "#EF4444",
        "confidence_base": 95.1,
        "sample_image": "/static/img/samples/cotton_leaf_curl.jpg",
        "symptoms": [
            "Upward or downward cupping and curling of young terminal leaves",
            "Severe thickening and darkening of leaf veins visible against sunlight",
            "Enations (small leaf-like outgrowths) on the lower surface of infected leaves",
            "Stunted plant stature and severe reduction in boll formation"
        ],
        "symptoms_pa": [
            "ਉੱਪਰਲੇ ਨਵੇਂ ਪੱਤਿਆਂ ਦਾ ਉੱਪਰ ਜਾਂ ਹੇਠਾਂ ਵੱਲ ਨੂੰ ਮੋੜ ਖਾਣਾ",
            "ਧੁੱਪ ਵੱਲ ਵੇਖਣ 'ਤੇ ਪੱਤੇ ਦੀਆਂ ਨਾੜਾਂ ਦਾ ਮੋਟਾ ਤੇ ਗੂੜ੍ਹਾ ਹਰਾ ਦਿੱਸਣਾ",
            "ਪੱਤਿਆਂ ਦੇ ਹੇਠਲੇ ਪਾਸੇ ਛੋਟੀਆਂ-ਛੋਟੀਆਂ ਪੱਤੀਆਂ ਵਰਗੇ ਵਾਧੂ ਉਭਾਰ ਬਣਨਾ",
            "ਬੂਟੇ ਦਾ ਕੱਦ ਛੋਟਾ ਰਹਿ ਜਾਣਾ ਅਤੇ ਟੀਂਡੇ ਘੱਟ ਲੱਗਣਾ"
        ],
        "symptoms_hi": [
            "ऊपरी नई पत्तियों का ऊपर या नीचे की ओर मुड़ना व कटोरीनुमा होना",
            "पत्तियों की नसों का असामान्य रूप से मोटा व गहरा हरा होना",
            "पत्तियों की निचली सतह पर छोटे पत्तीनुमा उभार बनना",
            "पौधों की बढ़वार रुकना और टिंडों की संख्या में भारी गिरावट"
        ],
        "likely_causes": [
            "High population of Whitefly (Bemisia tabaci) acting as the primary transmission vector",
            "Hot, dry periods followed by sudden humidity spikes in July-August",
            "Presence of alternative weed hosts like Kanghi buti along field borders"
        ],
        "likely_causes_pa": [
            "ਚਿੱਟੀ ਮੱਖੀ (Whitefly) ਦਾ ਹਮਲਾ ਜੋ ਇਸ ਵਾਇਰਸ ਨੂੰ ਇੱਕ ਬੂਟੇ ਤੋਂ ਦੂਜੇ ਬੂਟੇ ਤੱਕ ਫੈਲਾਉਂਦੀ ਹੈ",
            "ਖੇਤ ਦੀਆਂ ਵੱਟਾਂ 'ਤੇ ਕੰਘੀ ਬੂਟੀ ਜਾਂ ਪੀਲੀ ਬੂਟੀ ਵਰਗੇ ਨਦੀਨਾਂ ਦਾ ਹੋਣਾ"
        ],
        "likely_causes_hi": [
            "सफेद मक्खी (Whitefly) का प्रकोप जो इस वायरस को तेजी से फैलाती है",
            "खेत की मेड़ों पर खरपतवारों की मौजूदगी"
        ],
        "recommended_steps": [
            "Target the whitefly vector immediately with Pyriproxyfen 10% EC @ 500 ml/acre or Confidor (Imidacloprid) @ 100 ml/acre.",
            "Alternatively spray Flonicamid 50% WG @ 80 g/acre.",
            "Install yellow sticky traps (15 per acre) to monitor whitefly adults."
        ],
        "recommended_steps_pa": [
            "ਚਿੱਟੀ ਮੱਖੀ ਦੀ ਰੋਕਥਾਮ ਲਈ ਕਨਫੀਡੋਰ (Confidor / Imidacloprid) @ 100 ਮਿ.ਲੀ. ਜਾਂ ਫਲੋਨੀਕਾਮਿਡ 50% WG @ 80 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ ਸਪਰੇਅ ਕਰੋ।",
            "ਖੇਤ ਵਿੱਚ ਪੀਲੇ ਚਿਪਚਿਪੇ ਟਰੈਪ (Yellow Sticky Traps, 15 ਪ੍ਰਤੀ ਏਕੜ) ਲਗਾਓ।"
        ],
        "recommended_steps_hi": [
            "सफेद मक्खी नियंत्रण के लिए कॉनफिडोर (इमिडाक्लोप्रिड) 100 मिली अथवा फ्लोनिकामाइड 80 ग्राम प्रति एकड़ स्प्रे करें।",
            "खेत में 15 पीले चिपचिपे ट्रैप प्रति एकड़ लगाएं।"
        ],
        "prevention_tips": [
            "Eradicate weed hosts along field bunds prior to sowing.",
            "Sow CLCuD tolerant Bt-cotton hybrids recommended by PAU / CCS HAU."
        ],
        "prevention_tips_pa": [
            "ਬਿਜਾਈ ਤੋਂ ਪਹਿਲਾਂ ਵੱਟਾਂ ਤੋਂ ਕੰਘੀ ਬੂਟੀ ਤੇ ਪੀਲੀ ਬੂਟੀ ਨਸ਼ਟ ਕਰੋ।",
            "ਪੀ.ਏ.ਯੂ. ਵੱਲੋਂ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਰੋਗ-ਰੋਧਕ ਬੀਜ ਹੀ ਵਰਤੋ।"
        ],
        "prevention_tips_hi": [
            "मेड़ों से खरपतवार नष्ट करें।",
            "विश्वविद्यालय द्वारा प्रमाणित रोगरोधी बीटी कपास संकर ही बोएं।"
        ],
        "treatment_product_ids": ["prod_confidor", "prod_neem", "prod_coragen"],
        "bounding_boxes": [
            {"x": 20, "y": 22, "w": 60, "h": 50, "label": "Upward Leaf Cupping & Vein Enation", "confidence": 0.95}
        ]
    },
    {
        "id": "mustard_white_rust",
        "crop_id": "mustard",
        "name": "White Rust of Mustard",
        "name_hi": "सरसों का सफेद रतुआ (फफोले)",
        "name_pa": "ਸਰ੍ਹੋਂ ਦਾ ਚਿੱਟਾ ਕੁੰਗੀ ਰੋਗ",
        "scientific_name": "Albugo candida",
        "severity": "Moderate",
        "severity_pa": "ਦਰਮਿਆਨੀ (Moderate)",
        "severity_hi": "मध्यम (Moderate)",
        "severity_color": "#D97706",
        "confidence_base": 92.7,
        "sample_image": "/static/img/samples/mustard_white_rust.jpg",
        "symptoms": [
            "Prominent chalky white to creamy-white raised pustules or blisters on leaf undersides",
            "Corresponding upper leaf surface shows pale yellow chlorotic spots",
            "Hypertrophy and floral malformation causing grotesque 'stag-head' deformity where pods fail to set"
        ],
        "symptoms_pa": [
            "ਪੱਤਿਆਂ ਦੇ ਹੇਠਲੇ ਪਾਸੇ ਚਾਕ ਵਰਗੇ ਚਿੱਟੇ ਉੱਭਰੇ ਹੋਏ ਛਾਲੇ ਜਾਂ ਧੱਬੇ",
            "ਪੱਤੇ ਦੇ ਉੱਪਰਲੇ ਪਾਸੇ ਪੀਲੇ ਨਿਸ਼ਾਨ ਪੈਣਾ",
            "ਸਿੱਟਿਆਂ ਦਾ ਵਿਗੜ ਕੇ 'ਕੁੱਤੇ ਦਾ ਸਿਰ' (Stag-head) ਬਣ ਜਾਣਾ ਜਿਸ ਨਾਲ ਫਲੀਆਂ ਨਹੀਂ ਬਣਦੀਆਂ"
        ],
        "symptoms_hi": [
            "पत्तियों की निचली सतह पर सफेद चाक जैसे उभरे हुए छाले",
            "पत्ती की ऊपरी सतह पर हल्के पीले धब्बे",
            "फूलों व बालियों की विकृति जिससे फलियां नहीं बनतीं"
        ],
        "likely_causes": [
            "High relative humidity (>80%) accompanied by cooler temperatures (12-18°C) during flowering",
            "Heavy morning fog lasting several days in December-January"
        ],
        "likely_causes_pa": [
            "ਦਸੰਬਰ-ਜਨਵਰੀ ਵਿੱਚ ਲਗਾਤਾਰ ਸੰਘਣੀ ਧੁੰਦ ਅਤੇ 80% ਤੋਂ ਵੱਧ ਨਮੀ ਰਹਿਣਾ"
        ],
        "likely_causes_hi": [
            "दिसंबर-जनवरी में घना कोहरा व अत्यधिक नमी"
        ],
        "recommended_steps": [
            "Spray Metalaxyl 4% + Mancozeb 64% WP (Ridomil Gold) @ 2.5 g/L (500 g/acre) in 200L water.",
            "Alternatively apply Mancozeb 75% WP @ 600 g/acre at initial pustule sighting.",
            "Clip and destroy severely malformed 'stag heads' to prevent systemic spore shower."
        ],
        "recommended_steps_pa": [
            "ਰਿਡੋਮਿਲ ਗੋਲਡ (Ridomil Gold) @ 500 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ 200 ਲੀਟਰ ਪਾਣੀ ਵਿੱਚ ਮਿਲਾ ਕੇ ਸਪਰੇਅ ਕਰੋ।",
            "ਬਹੁਤ ਜ਼ਿਆਦਾ ਖ਼ਰਾਬ ਹੋ ਚੁੱਕੇ ਸਿੱਟਿਆਂ ਨੂੰ ਕੱਟ ਕੇ ਖੇਤ ਤੋਂ ਦੂਰ ਦੱਬ ਦਿਓ।"
        ],
        "recommended_steps_hi": [
            "रिडोमिल गोल्ड (Ridomil Gold) 500 ग्राम प्रति एकड़ 200 लीटर पानी में मिलाकर छिड़कें।",
            "रोगग्रस्त विकृत बालियों को काटकर नष्ट करें।"
        ],
        "prevention_tips": [
            "Practice crop rotation with non-cruciferous crops.",
            "Seed treatment with Metalaxyl @ 6 g/kg seed.",
            "Sow mustard varieties with tolerance such as Giriraj or RH-0749."
        ],
        "prevention_tips_pa": [
            "ਅੱਗੇ ਤੋਂ ਗਿਰੀਰਾਜ ਜਾਂ RH-0749 ਵਰਗੀਆਂ ਬਿਮਾਰੀ-ਰੋਧਕ ਕਿਸਮਾਂ ਦੀ ਬਿਜਾਈ ਕਰੋ।",
            "ਬੀਜ ਨੂੰ ਬਿਜਾਈ ਤੋਂ ਪਹਿਲਾਂ ਸੋਧੋ।"
        ],
        "prevention_tips_hi": [
            "गिरिराज जैसी सहनशील किस्में लगाएं।",
            "बुवाई से पूर्व बीजोपचार अवश्य करें।"
        ],
        "treatment_product_ids": ["prod_ridomil", "prod_saaf", "prod_npk19"],
        "bounding_boxes": [
            {"x": 22, "y": 28, "w": 44, "h": 42, "label": "Chalky White Pustule", "confidence": 0.94},
            {"x": 55, "y": 40, "w": 28, "h": 34, "label": "Chlorotic Foliar Lesion", "confidence": 0.91}
        ]
    },
    {
        "id": "potato_late_blight",
        "crop_id": "potato",
        "name": "Late Blight of Potato",
        "name_hi": "आलू का पछेती झुलसा (लेट ब्लाइट)",
        "name_pa": "ਆਲੂ ਦਾ ਪਛੇਤਾ ਝੁਲਸ ਰੋਗ",
        "scientific_name": "Phytophthora infestans",
        "severity": "Critical",
        "severity_pa": "ਗੰਭੀਰ (Critical)",
        "severity_hi": "गंभीर (Critical)",
        "severity_color": "#DC2626",
        "confidence_base": 97.4,
        "sample_image": "/static/img/samples/potato_late_blight.jpg",
        "symptoms": [
            "Water-soaked dark brownish-black irregular necrotic lesions on leaf margins and tips",
            "Delicate white cottony mildew growth visible on leaf undersides during moist early mornings",
            "Lesions rapidly turn black and foul-smelling; stems become brittle and collapse",
            "Infected tubers exhibit dry, granular, reddish-brown rot penetrating into the flesh"
        ],
        "symptoms_pa": [
            "ਪੱਤਿਆਂ ਦੇ ਕੰਢਿਆਂ 'ਤੇ ਪਾਣੀ ਵਰਗੇ ਕਾਲੇ-ਭੂਰੇ ਵੱਡੇ ਧੱਬੇ",
            "ਸਵੇਰ ਦੀ ਨਮੀ ਵੇਲੇ ਪੱਤੇ ਦੇ ਹੇਠਾਂ ਚਿੱਟੀ ਰੂੰ ਵਰਗੀ ਉੱਲੀ ਦਾ ਵਿਖਾਈ ਦੇਣਾ",
            "ਬੂਟੇ ਦਾ ਤੇਜ਼ੀ ਨਾਲ ਕਾਲਾ ਪੈ ਕੇ ਗਲਣਾ",
            "ਜ਼ਮੀਨ ਵਿੱਚ ਆਲੂਆਂ ਦੇ ਅੰਦਰ ਭੂਰਾ ਸੜਾਂਧ ਪੈਣਾ"
        ],
        "symptoms_hi": [
            "पत्तियों के किनारों पर जलसिक्त काले-भूरे अनियमित धब्बे",
            "सुबह की नमी में पत्ती के नीचे सफेद रुई जैसी फफूंद का दिखना",
            "पौधों का तेजी से गलकर गिरना",
            "आलू के कंदों में भूरी सड़न लगना"
        ],
        "likely_causes": [
            "Cool temperatures (10-20°C) with persistent humidity >90% and cloudy or drizzly weather",
            "Microclimate trapped within dense, lush potato foliage"
        ],
        "likely_causes_pa": [
            "10-20°C ਤਾਪਮਾਨ ਅਤੇ 90% ਤੋਂ ਵੱਧ ਨਮੀ ਦੇ ਨਾਲ ਬੱਦਲਵਾਈ ਜਾਂ ਬੂੰਦਾ-ਬਾਂਦੀ"
        ],
        "likely_causes_hi": [
            "10-20°C तापमान, 90% से अधिक आर्द्रता और बूंदाबांदी"
        ],
        "recommended_steps": [
            "Immediately apply Ridomil Gold (Metalaxyl + Mancozeb) @ 2.5 g/L (500 g/acre) in 200L water.",
            "Alternatively use Nativo or Saaf Fungicide.",
            "Strictly avoid furrow flooding that touches leaf foliage."
        ],
        "recommended_steps_pa": [
            "ਤੁਰੰਤ ਰਿਡੋਮਿਲ ਗੋਲਡ (Ridomil Gold) @ 500 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ ਛਿੜਕੋ।",
            "ਕਿਆਰੀਆਂ ਵਿੱਚ ਪਾਣੀ ਨੂੰ ਪੱਤਿਆਂ ਤੱਕ ਨਾ ਚੜ੍ਹਨ ਦਿਓ।"
        ],
        "recommended_steps_hi": [
            "तत्काल रिडोमिल गोल्ड 500 ग्राम प्रति एकड़ 200 लीटर पानी में मिलाकर स्प्रे करें।",
            "पत्तियों को छूने वाले अत्यधिक जलभराव से बचें।"
        ],
        "prevention_tips": [
            "Use certified disease-free seed tubers.",
            "Practice proper earthing-up to bury tubers deep."
        ],
        "prevention_tips_pa": [
            "ਪ੍ਰਮਾਣਿਤ ਬੀਜ ਹੀ ਵਰਤੋ ਅਤੇ ਆਲੂਆਂ 'ਤੇ ਮਿੱਟੀ ਚੰਗੀ ਤਰ੍ਹਾਂ ਚੜ੍ਹਾਓ।"
        ],
        "prevention_tips_hi": [
            "प्रमाणित रोगमुक्त बीज लगाएं और कंदों पर अच्छी मिट्टी चढ़ाएं।"
        ],
        "treatment_product_ids": ["prod_ridomil", "prod_saaf", "prod_nativo"],
        "bounding_boxes": [
            {"x": 20, "y": 15, "w": 52, "h": 50, "label": "Water-soaked Necrotic Lesion", "confidence": 0.98},
            {"x": 54, "y": 48, "w": 32, "h": 36, "label": "Sporulating Margin Zone", "confidence": 0.96}
        ]
    },
    {
        "id": "tomato_early_blight",
        "crop_id": "tomato",
        "name": "Early Blight of Tomato",
        "name_hi": "टमाटर का अगेती झुलसा रोग",
        "name_pa": "ਟਮਾਟਰ ਦਾ ਅਗੇਤਾ ਝੁਲਸ ਰੋਗ",
        "scientific_name": "Alternaria solani",
        "severity": "Moderate",
        "severity_pa": "ਦਰਮਿਆਨੀ (Moderate)",
        "severity_hi": "मध्यम (Moderate)",
        "severity_color": "#D97706",
        "confidence_base": 93.8,
        "sample_image": "/static/img/samples/tomato_early_blight.jpg",
        "symptoms": [
            "Dark brown to black circular spots with distinctive concentric rings ('target-board' appearance)",
            "Yellow halo (chlorosis) surrounding the dark target lesions",
            "Lower leaves infect first and drop prematurely, exposing developing tomatoes to sunscald"
        ],
        "symptoms_pa": [
            "ਪੱਤਿਆਂ 'ਤੇ ਗੋਲ ਚੱਕਰਦਾਰ ਕਾਲੇ-ਭੂਰੇ ਧੱਬੇ (ਜਿਵੇਂ ਨਿਸ਼ਾਨੇ ਵਾਲਾ ਬੋਰਡ ਹੋਵੇ)",
            "ਧੱਬਿਆਂ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪੀਲਾ ਘੇਰਾ",
            "ਹੇਠਲੇ ਪੱਤੇ ਸੁੱਕ ਕੇ ਝੜਨਾ"
        ],
        "symptoms_hi": [
            "पत्तियों पर संकेंद्री छल्लों वाले गोल काले-भूरे धब्बे (टारगेट बोर्ड की तरह)",
            "धब्बों के चारों ओर पीला घेरा",
            "निचली पत्तियों का झुलसकर गिरना"
        ],
        "likely_causes": [
            "Warm temperatures (24-29°C) combined with frequent rain or overhead sprinkler watering",
            "Plants experiencing heavy fruit load"
        ],
        "likely_causes_pa": [
            "ਗਰਮ ਮੌਸਮ (24-29°C) ਅਤੇ ਪੱਤਿਆਂ 'ਤੇ ਸਿੱਧਾ ਪਾਣੀ ਪੈਣਾ"
        ],
        "likely_causes_hi": [
            "गर्म तापमान (24-29°C) और पत्तियों पर पानी का ठहराव"
        ],
        "recommended_steps": [
            "Spray Amistar Top (Azoxystrobin + Difenoconazole) @ 1 ml/L (200 ml/acre).",
            "Alternatively use Saaf Fungicide @ 2 g/L.",
            "Prune off severely spotted bottom leaves."
        ],
        "recommended_steps_pa": [
            "ਐਮੀਸਟਾਰ ਟੌਪ (Amistar Top) @ 200 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਏਕੜ ਜਾਂ ਸਾਫ਼ (Saaf) @ 400 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ ਸਪਰੇਅ ਕਰੋ।",
            "ਹੇਠਲੇ ਸੁੱਕੇ ਪੱਤੇ ਕੱਟ ਕੇ ਨਸ਼ਟ ਕਰੋ।"
        ],
        "recommended_steps_hi": [
            "एमिस्टार टॉप @ 200 मिली अथवा साफ (Saaf) @ 400 ग्राम प्रति एकड़ छिड़कें।",
            "अत्यधिक प्रभावित निचली पत्तियों को काटकर हटाएं।"
        ],
        "prevention_tips": [
            "Stake tomato plants and mulch soil with silver-black mulch film.",
            "Water only at the root base with drip lines; keep foliage dry."
        ],
        "prevention_tips_pa": [
            "ਟਮਾਟਰਾਂ ਨੂੰ ਸਹਾਰਾ ਦੇ ਕੇ ਬੰਨ੍ਹੋ ਅਤੇ ਤੁਪਕਾ ਸਿੰਚਾਈ (Drip) ਦੀ ਵਰਤੋਂ ਕਰੋ।"
        ],
        "prevention_tips_hi": [
            "पौधों को सहारा दें और ड्रिप सिंचाई से केवल जड़ों में पानी दें।"
        ],
        "treatment_product_ids": ["prod_amistar", "prod_saaf", "prod_copper"],
        "bounding_boxes": [
            {"x": 24, "y": 26, "w": 46, "h": 44, "label": "Concentric Target Spot", "confidence": 0.95}
        ]
    }
]

PRODUCTS = [
    {
        "id": "prod_tilt",
        "name": "Tilt 25% EC Systemic Fungicide",
        "name_pa": "ਟਿਲਟ 25% EC ਉੱਲੀਨਾਸ਼ਕ",
        "name_hi": "टिल्ट 25% EC फफूंदनाशक",
        "brand": "Syngenta India",
        "category": "Fungicide",
        "category_pa": "ਉੱਲੀਨਾਸ਼ਕ",
        "category_hi": "फफूंदनाशक",
        "active_ingredient": "Propiconazole 25% EC",
        "cibrc_reg": "CIR-14309/92/Propiconazole(EC)-108",
        "suitable_crops": ["Wheat", "Rice", "Groundnut", "Tea", "Soybean"],
        "target_diseases": ["Yellow Rust (Stripe Rust)", "Brown Rust", "Karnal Bunt", "Sheath Blight", "Tikka Leaf Spot"],
        "pack_size": "250 ml",
        "price": 420,
        "mrp": 530,
        "rating": 4.8,
        "reviews_count": 342,
        "seller": "Syngenta Authorised Kisan Kendra, Bathinda",
        "delivery_est": "2-3 business days",
        "image": "/static/img/products/tilt.png",
        "in_stock": True,
        "dosage": "1.0 ml per liter of water (200 ml in 200 liters water per acre)",
        "dosage_pa": "1.0 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (200 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਏਕੜ 200 ਲੀਟਰ ਪਾਣੀ ਵਿੱਚ)",
        "dosage_hi": "1.0 मिली प्रति लीटर पानी (200 मिली प्रति एकड़ 200 लीटर पानी में)",
        "safety_ppe": ["N95 Mask", "Nitrile Gloves", "Safety Goggles", "Long Sleeves"],
        "phi_days": 30,
        "regulatory_notice": "Use agricultural chemicals only according to the approved product label and local agricultural guidance. Pre-Harvest Interval (PHI): 30 days for Wheat."
    },
    {
        "id": "prod_nativo",
        "name": "Nativo 75 WG Broad-Spectrum Fungicide",
        "name_pa": "ਨੈਟਿਵੋ 75 WG ਉੱਲੀਨਾਸ਼ਕ",
        "name_hi": "नेटिवो 75 WG फफूंदनाशक",
        "brand": "Bayer CropScience",
        "category": "Fungicide",
        "category_pa": "ਉੱਲੀਨਾਸ਼ਕ",
        "category_hi": "फफूंदनाशक",
        "active_ingredient": "Tebuconazole 50% + Trifloxystrobin 25% WG",
        "cibrc_reg": "CIR-58902/2008/Tebuconazole+Trifloxystrobin(WG)-314",
        "suitable_crops": ["Rice / Paddy", "Wheat", "Tomato", "Chilli", "Mango", "Grapes"],
        "target_diseases": ["Rice Blast", "Sheath Blight", "Yellow Rust", "Early Blight", "Anthracnose"],
        "pack_size": "100 g",
        "price": 890,
        "mrp": 1050,
        "rating": 4.9,
        "reviews_count": 512,
        "seller": "Bayer Agro Hub, Karnal",
        "delivery_est": "1-2 business days",
        "image": "/static/img/products/nativo.png",
        "in_stock": True,
        "dosage": "0.5 g - 0.7 g per liter of water (100-140 g in 200 liters water per acre)",
        "dosage_pa": "0.5 - 0.7 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (100-140 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ)",
        "dosage_hi": "0.5 - 0.7 ग्राम प्रति लीटर पानी (100-140 ग्राम प्रति एकड़)",
        "safety_ppe": ["Chemical Gloves", "Protective Apron", "Face Shield"],
        "phi_days": 21,
        "regulatory_notice": "Approved by CIBRC for blast and rust control. Wear protective gear while preparing spray tank suspension."
    },
    {
        "id": "prod_amistar",
        "name": "Amistar Top Systemic Fungicide",
        "name_pa": "ਐਮੀਸਟਾਰ ਟੌਪ ਉੱਲੀਨਾਸ਼ਕ",
        "name_hi": "एमिस्टार टॉप फफूंदनाशक",
        "brand": "Syngenta India",
        "category": "Fungicide",
        "category_pa": "ਉੱਲੀਨਾਸ਼ਕ",
        "category_hi": "फफूंदनाशक",
        "active_ingredient": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC",
        "cibrc_reg": "CIR-63211/2010/Azoxystrobin+Difenoconazole(SC)-412",
        "suitable_crops": ["Tomato", "Rice", "Chilli", "Maize", "Cotton"],
        "target_diseases": ["Early Blight", "Late Blight", "Sheath Blight", "Blast", "Dieback", "Turcicum Blight"],
        "pack_size": "200 ml",
        "price": 1150,
        "mrp": 1340,
        "rating": 4.9,
        "reviews_count": 289,
        "seller": "GreenTech Agri Distributorship, Ludhiana",
        "delivery_est": "2-4 business days",
        "image": "/static/img/products/amistar.png",
        "in_stock": True,
        "dosage": "1.0 ml per liter of water (200 ml per acre)",
        "dosage_pa": "1.0 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (200 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਏਕੜ)",
        "dosage_hi": "1.0 मिली प्रति लीटर पानी (200 मिली प्रति एकड़)",
        "safety_ppe": ["Gloves", "Mask", "Boots"],
        "phi_days": 15,
        "regulatory_notice": "Provides dual-action preventive and curative control. Do not apply during extreme midday heat."
    },
    {
        "id": "prod_ridomil",
        "name": "Ridomil Gold MZ 68 WG Fungicide",
        "name_pa": "ਰਿਡੋਮਿਲ ਗੋਲਡ MZ ਉੱਲੀਨਾਸ਼ਕ",
        "name_hi": "रिडोमिल गोल्ड MZ फफूंदनाशक",
        "brand": "Syngenta India",
        "category": "Fungicide",
        "category_pa": "ਉੱਲੀਨਾਸ਼ਕ",
        "category_hi": "फफूंदनाशक",
        "active_ingredient": "Metalaxyl-M 4% + Mancozeb 64% WG",
        "cibrc_reg": "CIR-45120/2004/Metalaxyl-M+Mancozeb(WG)-210",
        "suitable_crops": ["Potato", "Mustard", "Tomato", "Grapes", "Black Pepper"],
        "target_diseases": ["Late Blight of Potato", "White Rust of Mustard", "Downy Mildew", "Damping Off"],
        "pack_size": "500 g",
        "price": 560,
        "mrp": 690,
        "rating": 4.7,
        "reviews_count": 418,
        "seller": "Kisan Seva Kendra, Jalandhar",
        "delivery_est": "2 business days",
        "image": "/static/img/products/ridomil.png",
        "in_stock": True,
        "dosage": "2.0 g to 2.5 g per liter of water (500 g per acre)",
        "dosage_pa": "2.0 - 2.5 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (500 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ)",
        "dosage_hi": "2.0 - 2.5 ग्राम प्रति लीटर पानी (500 ग्राम प्रति एकड़)",
        "safety_ppe": ["Rubber Gloves", "Dust Mask", "Goggles"],
        "phi_days": 40,
        "regulatory_notice": "Follow statutory Pre-Harvest Interval of 40 days for potato tuber consumption safety."
    },
    {
        "id": "prod_saaf",
        "name": "Saaf Dual Contact & Systemic Fungicide",
        "name_pa": "ਸਾਫ਼ ਉੱਲੀਨਾਸ਼ਕ (Saaf)",
        "name_hi": "साफ फफूंदनाशक (Saaf)",
        "brand": "UPL Limited",
        "category": "Fungicide",
        "category_pa": "ਉੱਲੀਨਾਸ਼ਕ",
        "category_hi": "फफूंदनाशक",
        "active_ingredient": "Carbendazim 12% + Mancozeb 63% WP",
        "cibrc_reg": "CIR-22180/96/Carbendazim+Mancozeb(WP)-155",
        "suitable_crops": ["Wheat", "Rice", "Potato", "Groundnut", "Chilli", "Tea"],
        "target_diseases": ["Powdery Mildew", "Blast", "Leaf Spot", "Collar Rot", "Anthracnose", "Rust"],
        "pack_size": "500 g",
        "price": 260,
        "mrp": 330,
        "rating": 4.6,
        "reviews_count": 780,
        "seller": "UPL Crop Protection, Rajpura",
        "delivery_est": "1-3 business days",
        "image": "/static/img/products/saaf.png",
        "in_stock": True,
        "dosage": "2.0 g per liter of water (400-500 g per acre)",
        "dosage_pa": "2.0 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (400-500 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਏਕੜ)",
        "dosage_hi": "2.0 ग्राम प्रति लीटर पानी (400-500 ग्राम प्रति एकड़)",
        "safety_ppe": ["Gloves", "Mask"],
        "phi_days": 30,
        "regulatory_notice": "Trusted combination fungicide. Wash hands thoroughly with soap after handling."
    },
    {
        "id": "prod_confidor",
        "name": "Confidor 17.8% SL Sucking Pest Insecticide",
        "name_pa": "ਕਨਫੀਡੋਰ ਕੀਟਨਾਸ਼ਕ",
        "name_hi": "कॉनफिडोर कीटनाशक",
        "brand": "Bayer CropScience",
        "category": "Insecticide",
        "category_pa": "ਕੀਟਨਾਸ਼ਕ",
        "category_hi": "कीटनाशक",
        "active_ingredient": "Imidacloprid 17.8% SL",
        "cibrc_reg": "CIR-32110/99/Imidacloprid(SL)-121",
        "suitable_crops": ["Cotton", "Paddy", "Chilli", "Tomato", "Sugarcane"],
        "target_diseases": ["Whitefly (Vector for Leaf Curl)", "Aphids", "Jassids", "Thrips", "Brown Plant Hopper"],
        "pack_size": "250 ml",
        "price": 340,
        "mrp": 420,
        "rating": 4.8,
        "reviews_count": 620,
        "seller": "Bayer Authorized Store, Bathinda",
        "delivery_est": "2 business days",
        "image": "/static/img/products/confidor.png",
        "in_stock": True,
        "dosage": "0.3 ml - 0.5 ml per liter of water (60-100 ml per acre)",
        "dosage_pa": "0.3 - 0.5 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (60-100 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਏਕੜ)",
        "dosage_hi": "0.3 - 0.5 मिली प्रति लीटर पानी (60-100 मिली प्रति एकड़)",
        "safety_ppe": ["Rubber Gloves", "Eye Protection", "Face Mask"],
        "phi_days": 21,
        "regulatory_notice": "Toxic to honeybees; avoid spraying during active morning bee foraging."
    },
    {
        "id": "prod_coragen",
        "name": "Coragen 18.5% SC Green Label Insecticide",
        "name_pa": "ਕੋਰਾਜਨ 18.5% SC ਕੀਟਨਾਸ਼ਕ",
        "name_hi": "कोराजन 18.5% SC कीटनाशक",
        "brand": "FMC India",
        "category": "Insecticide",
        "category_pa": "ਕੀਟਨਾਸ਼ਕ",
        "category_hi": "कीटनाशक",
        "active_ingredient": "Chlorantraniliprole 18.5% SC (Rynaxypyr)",
        "cibrc_reg": "CIR-61200/2009/Chlorantraniliprole(SC)-320",
        "suitable_crops": ["Paddy", "Sugarcane", "Cotton", "Maize", "Tomato", "Cabbage"],
        "target_diseases": ["Stem Borer", "Leaf Folder", "Fall Armyworm", "Bollworms", "Fruit Borer"],
        "pack_size": "150 ml",
        "price": 1480,
        "mrp": 1750,
        "rating": 4.9,
        "reviews_count": 890,
        "seller": "FMC Agro Solutions, Karnal",
        "delivery_est": "1-2 business days",
        "image": "/static/img/products/coragen.png",
        "in_stock": True,
        "dosage": "0.4 ml per liter of water (60 ml per acre in paddy / 150 ml in sugarcane)",
        "dosage_pa": "0.4 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (60 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਏਕੜ ਝੋਨੇ ਵਿੱਚ)",
        "dosage_hi": "0.4 मिली प्रति लीटर पानी (60 मिली प्रति एकड़ धान में)",
        "safety_ppe": ["Nitrile Gloves", "Protective Clothing"],
        "phi_days": 14,
        "regulatory_notice": "Green-triangle certified. Safe on natural beneficial predator insects like spiders and ladybugs."
    },
    {
        "id": "prod_neem",
        "name": "Neem Baan 10,000 PPM Organic Bio-Pesticide",
        "name_pa": "ਨੀਮ ਬਾਣ ਜੈਵਿਕ ਕੀਟਨਾਸ਼ਕ",
        "name_hi": "नीम बाण जैविक कीटनाशक",
        "brand": "Multiplex Bio-Tech",
        "category": "Bio-control",
        "category_pa": "ਜੈਵਿਕ ਦਵਾਈਆਂ",
        "category_hi": "जैविक नियंत्रण",
        "active_ingredient": "Azadirachtin 1.0% EC (10,000 PPM)",
        "cibrc_reg": "CIR-48190/2005/Azadirachtin(EC)-190",
        "suitable_crops": ["All Crops", "Vegetables", "Cotton", "Mustard", "Wheat"],
        "target_diseases": ["Whitefly", "Aphids", "Mites", "Caterpillar Ovicide", "Fungal spores"],
        "pack_size": "500 ml",
        "price": 380,
        "mrp": 480,
        "rating": 4.7,
        "reviews_count": 215,
        "seller": "Jaivik Kisan Seva, Chandigarh",
        "delivery_est": "2-3 business days",
        "image": "/static/img/products/neem.png",
        "in_stock": True,
        "dosage": "2.0 - 2.5 ml per liter of water",
        "dosage_pa": "2.0 - 2.5 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ",
        "dosage_hi": "2.0 - 2.5 मिली प्रति लीटर पानी",
        "safety_ppe": ["Standard Cotton Mask"],
        "phi_days": 3,
        "regulatory_notice": "Certified 100% Organic input by NPOP / Jaivik Bharat. No chemical synthetic residues."
    },
    {
        "id": "prod_tricho",
        "name": "Trichoderma Viride 1.5% WP Bio-Fungicide",
        "name_pa": "ਟ੍ਰਾਈਕੋਡਰਮਾ ਵਿਰਿਡੀ ਜੈਵਿਕ ਉੱਲੀਨਾਸ਼ਕ",
        "name_hi": "ट्राइकोडर्मा विरिडी जैविक फफूंदनाशक",
        "brand": "IPL Biologicals",
        "category": "Bio-control",
        "category_pa": "ਜੈਵਿਕ ਦਵਾਈਆਂ",
        "category_hi": "जैविक नियंत्रण",
        "active_ingredient": "Trichoderma viride (CFU 2 x 10^6 per gram min)",
        "cibrc_reg": "CIR-51001/2006/Trichoderma viride(WP)-88",
        "suitable_crops": ["Wheat", "Mustard", "Gram", "Potato", "Paddy", "Sugarcane"],
        "target_diseases": ["Root Rot", "Collar Rot", "Damping Off", "Fusarium Wilt", "Seed-borne pathogens"],
        "pack_size": "1 kg",
        "price": 180,
        "mrp": 240,
        "rating": 4.8,
        "reviews_count": 310,
        "seller": "Jaivik Agro Mart, Indore",
        "delivery_est": "2-3 business days",
        "image": "/static/img/products/tricho.png",
        "in_stock": True,
        "dosage": "Seed treatment: 5-10 g/kg seed; Soil treatment: 1 kg mixed with 50 kg FYM per acre",
        "dosage_pa": "ਬੀਜ ਸੋਧ: 5-10 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਕਿੱਲੋ ਬੀਜ; ਜ਼ਮੀਨ ਲਈ: 1 ਕਿੱਲੋ ਰੂੜੀ ਖਾਦ ਵਿੱਚ ਮਿਲਾ ਕੇ",
        "dosage_hi": "बीजोपचार: 5-10 ग्राम/किग्रा बीज; भूमि उपचार: 1 किग्रा प्रति एकड़ सड़ी गोबर खाद में",
        "safety_ppe": ["Dust Mask"],
        "phi_days": 0,
        "regulatory_notice": "Do not mix with chemical fungicides. Apply during evening or cloudy hours."
    },
    {
        "id": "prod_nanourea",
        "name": "IFFCO Nano Urea (Liquid) - 500ml",
        "name_pa": "ਇਫਕੋ ਨੈਨੋ ਯੂਰੀਆ (ਤਰਲ) 500ml",
        "name_hi": "इफको नैनो यूरिया (तरल) 500ml",
        "brand": "IFFCO",
        "category": "Fertilizer",
        "category_pa": "ਖਾਦਾਂ",
        "category_hi": "खाद व उर्वरक",
        "active_ingredient": "Nanoscale Nitrogen 4.0% w/v (40,000 ppm)",
        "cibrc_reg": "FCO 1985 Approved / Gazette Notification S.O. 884(E)",
        "suitable_crops": ["Wheat", "Paddy", "Mustard", "Cotton", "Maize", "Vegetables"],
        "target_diseases": ["Nitrogen Deficiency", "Stunted Growth", "Leaf Chlorosis"],
        "pack_size": "500 ml bottle (= 1 bag of traditional 45kg urea)",
        "price": 225,
        "mrp": 225,
        "rating": 4.9,
        "reviews_count": 1420,
        "seller": "IFFCO Kisan Seva Kendra, Patiala",
        "delivery_est": "1-2 business days",
        "image": "/static/img/products/nanourea.png",
        "in_stock": True,
        "dosage": "2.0 - 4.0 ml per liter of water (first spray at tillering, second at flag leaf)",
        "dosage_pa": "2.0 - 4.0 ਮਿ.ਲੀ. ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (ਪਹਿਲਾ ਸਪਰੇਅ ਫੁਟਾਰੇ ਵੇਲੇ)",
        "dosage_hi": "2.0 - 4.0 मिली प्रति लीटर पानी (पहला स्प्रे कल्ले फूटते समय)",
        "safety_ppe": ["Gloves", "Mask"],
        "phi_days": 7,
        "regulatory_notice": "Shake well before use. Spray during active vegetative tillering with flat fan nozzle."
    },
    {
        "id": "prod_npk19",
        "name": "Water Soluble NPK 19:19:19 Foliar Fertilizer",
        "name_pa": "NPK 19:19:19 ਪਾਣੀ 'ਚ ਘੁਲਣਸ਼ੀਲ ਖਾਦ",
        "name_hi": "NPK 19:19:19 100% घुलनशील उर्वरक",
        "brand": "Mahadhan",
        "category": "Fertilizer",
        "category_pa": "ਖਾਦਾਂ",
        "category_hi": "खाद व उर्वरक",
        "active_ingredient": "Total N 19%, P2O5 19%, K2O 19% (100% Water Soluble)",
        "cibrc_reg": "FCO Grade 1985 Certified",
        "suitable_crops": ["All Field Crops", "Horticulture", "Vegetables"],
        "target_diseases": ["General Nutrient Deficiency", "Post-Stress Recovery"],
        "pack_size": "1 kg",
        "price": 190,
        "mrp": 240,
        "rating": 4.7,
        "reviews_count": 390,
        "seller": "Kisan Fertilizer Store, Aligarh",
        "delivery_est": "2-3 business days",
        "image": "/static/img/products/npk19.png",
        "in_stock": True,
        "dosage": "5.0 g per liter of water (1 kg in 200 liters water per acre)",
        "dosage_pa": "5.0 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ (1 ਕਿੱਲੋ ਪ੍ਰਤੀ ਏਕੜ 200 ਲੀਟਰ ਪਾਣੀ ਵਿੱਚ)",
        "dosage_hi": "5.0 ग्राम प्रति लीटर पानी (1 किग्रा प्रति एकड़ 200 लीटर पानी में)",
        "safety_ppe": ["None required, keep dry"],
        "phi_days": 0,
        "regulatory_notice": "Promotes balanced vegetative canopy, root elongation and frost tolerance."
    },
    {
        "id": "prod_seed_wheat",
        "name": "PAU Certified PBW-826 Wheat Seeds (Rust Resistant)",
        "name_pa": "ਪੀ.ਏ.ਯੂ. ਪ੍ਰਮਾਣਿਤ PBW-826 ਕਣਕ ਦਾ ਬੀਜ",
        "name_hi": "PAU प्रमाणित PBW-826 गेहूं बीज",
        "brand": "Punjab Agricultural University (PAU)",
        "category": "Seeds",
        "category_pa": "ਪ੍ਰਮਾਣਿਤ ਬੀਜ",
        "category_hi": "प्रमाणित बीज",
        "active_ingredient": "Breeder/Foundation Tagged Certified Seed",
        "cibrc_reg": "Seeds Act 1966 Notification No. 1208",
        "suitable_crops": ["Wheat"],
        "target_diseases": ["Inherently resistant to Yellow Rust & Brown Rust pathotypes"],
        "pack_size": "40 kg bag",
        "price": 1200,
        "mrp": 1400,
        "rating": 4.9,
        "reviews_count": 680,
        "seller": "Punjab State Seeds Corporation (PUNSEED), Ludhiana",
        "delivery_est": "3 business days",
        "image": "/static/img/products/seed_wheat.png",
        "in_stock": True,
        "dosage": "Sowing rate: 40-45 kg per acre using Happy Seeder or Super Seeder",
        "dosage_pa": "ਬਿਜਾਈ ਦਰ: 40-45 ਕਿੱਲੋ ਪ੍ਰਤੀ ਏਕੜ (ਹੈਪੀ ਸੀਡਰ ਜਾਂ ਸੁਪਰ ਸੀਡਰ ਨਾਲ)",
        "dosage_hi": "बुवाई दर: 40-45 किग्रा प्रति एकड़ (सुपर सीडर या हैप्पी सीडर द्वारा)",
        "safety_ppe": ["Pre-treated with fungicide; wash hands"],
        "phi_days": 0,
        "regulatory_notice": "High yielding (average 24.5 quintals/acre), heat-tolerant at terminal grain filling stage."
    }
]

MANDI_PRICES = [
    {
        "mandi": "Khanna",
        "district": "Ludhiana",
        "state": "Punjab",
        "commodity": "Wheat (Dara/PBW)",
        "commodity_hi": "गेहूँ",
        "commodity_pa": "ਕਣਕ",
        "min_price": 2420,
        "max_price": 2530,
        "modal_price": 2485,
        "change": 35,
        "msp": 2425,
        "msp_status": "Above MSP (+₹60)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹60)",
        "msp_status_hi": "MSP से अधिक (+₹60)",
        "volume_qtl": 8400,
        "trend": [2420, 2435, 2450, 2465, 2470, 2485],
        "last_updated": "Today, 11:30 AM"
    },
    {
        "mandi": "Ludhiana",
        "district": "Ludhiana",
        "state": "Punjab",
        "commodity": "Wheat (PBW-826)",
        "commodity_hi": "गेहूँ (PBW-826)",
        "commodity_pa": "ਕਣਕ (PBW-826)",
        "min_price": 2430,
        "max_price": 2550,
        "modal_price": 2510,
        "change": 40,
        "msp": 2425,
        "msp_status": "Above MSP (+₹85)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹85)",
        "msp_status_hi": "MSP से अधिक (+₹85)",
        "volume_qtl": 6200,
        "trend": [2440, 2455, 2470, 2485, 2495, 2510],
        "last_updated": "Today, 11:45 AM"
    },
    {
        "mandi": "Abohar",
        "district": "Fazilka",
        "state": "Punjab",
        "commodity": "Cotton (Narma Long Staple)",
        "commodity_hi": "कपास (नरमा)",
        "commodity_pa": "ਨਰਮਾ (ਲੰਮਾ ਰੇਸ਼ਾ)",
        "min_price": 7250,
        "max_price": 7780,
        "modal_price": 7560,
        "change": 110,
        "msp": 7121,
        "msp_status": "Above MSP (+₹439)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹439)",
        "msp_status_hi": "MSP से अधिक (+₹439)",
        "volume_qtl": 4100,
        "trend": [7350, 7400, 7460, 7490, 7520, 7560],
        "last_updated": "Today, 12:00 PM"
    },
    {
        "mandi": "Bathinda",
        "district": "Bathinda",
        "state": "Punjab",
        "commodity": "Mustard (Sarson 42% Oil)",
        "commodity_hi": "सरसों (42% तेल)",
        "commodity_pa": "ਸਰ੍ਹੋਂ (42% ਤੇਲ)",
        "min_price": 5800,
        "max_price": 6180,
        "modal_price": 6050,
        "change": 85,
        "msp": 5650,
        "msp_status": "Above MSP (+₹400)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹400)",
        "msp_status_hi": "MSP से अधिक (+₹400)",
        "volume_qtl": 3200,
        "trend": [5880, 5920, 5960, 5990, 6020, 6050],
        "last_updated": "Today, 11:15 AM"
    },
    {
        "mandi": "Amritsar",
        "district": "Amritsar",
        "state": "Punjab",
        "commodity": "Basmati 1121 Export Grade",
        "commodity_hi": "बासमती 1121",
        "commodity_pa": "ਬਾਸਮਤੀ 1121 ਐਕਸਪੋਰਟ",
        "min_price": 4200,
        "max_price": 4550,
        "modal_price": 4440,
        "change": 90,
        "msp": 2300,
        "msp_status": "Premium Market (+₹2,140)",
        "msp_status_pa": "ਪ੍ਰੀਮੀਅਮ ਬਾਜ਼ਾਰ (+₹2,140)",
        "msp_status_hi": "प्रीमियम बाजार (+₹2,140)",
        "volume_qtl": 5600,
        "trend": [4250, 4290, 4340, 4380, 4400, 4440],
        "last_updated": "Today, 01:10 PM"
    },
    {
        "mandi": "Jalandhar",
        "district": "Jalandhar",
        "state": "Punjab",
        "commodity": "Potato (Kufri Jyoti / Pukhraj)",
        "commodity_hi": "आलू (कुफरी ज्योति)",
        "commodity_pa": "ਆਲੂ (ਕੁਫ਼ਰੀ ਜੋਤੀ)",
        "min_price": 1200,
        "max_price": 1480,
        "modal_price": 1360,
        "change": 60,
        "msp": 1050,
        "msp_status": "Market Free (+₹310)",
        "msp_status_pa": "ਖੁੱਲ੍ਹਾ ਬਾਜ਼ਾਰ (+₹310)",
        "msp_status_hi": "खुला बाजार (+₹310)",
        "volume_qtl": 9400,
        "trend": [1220, 1260, 1290, 1310, 1330, 1360],
        "last_updated": "Today, 11:00 AM"
    },
    {
        "mandi": "Rajpura",
        "district": "Patiala",
        "state": "Punjab",
        "commodity": "Wheat (Sharbati / PBW)",
        "commodity_hi": "गेहूँ (शरबती)",
        "commodity_pa": "ਕਣਕ (ਸ਼ਰਬਤੀ)",
        "min_price": 2440,
        "max_price": 2560,
        "modal_price": 2515,
        "change": 45,
        "msp": 2425,
        "msp_status": "Above MSP (+₹90)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹90)",
        "msp_status_hi": "MSP से अधिक (+₹90)",
        "volume_qtl": 4800,
        "trend": [2450, 2465, 2480, 2495, 2505, 2515],
        "last_updated": "Today, 10:45 AM"
    },
    {
        "mandi": "Sangrur",
        "district": "Sangrur",
        "state": "Punjab",
        "commodity": "Paddy (PR-126)",
        "commodity_hi": "धान (पी.आर.-126)",
        "commodity_pa": "ਝੋਨਾ (PR-126)",
        "min_price": 2320,
        "max_price": 2380,
        "modal_price": 2360,
        "change": 20,
        "msp": 2300,
        "msp_status": "Above MSP (+₹60)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹60)",
        "msp_status_hi": "MSP से अधिक (+₹60)",
        "volume_qtl": 7100,
        "trend": [2310, 2325, 2335, 2345, 2350, 2360],
        "last_updated": "Today, 12:30 PM"
    },
    {
        "mandi": "Moga",
        "district": "Moga",
        "state": "Punjab",
        "commodity": "Wheat (HD-3086)",
        "commodity_hi": "गेहूँ (HD-3086)",
        "commodity_pa": "ਕਣਕ (HD-3086)",
        "min_price": 2435,
        "max_price": 2540,
        "modal_price": 2495,
        "change": 30,
        "msp": 2425,
        "msp_status": "Above MSP (+₹70)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹70)",
        "msp_status_hi": "MSP से अधिक (+₹70)",
        "volume_qtl": 5200,
        "trend": [2440, 2450, 2465, 2480, 2490, 2495],
        "last_updated": "Today, 11:50 AM"
    },
    {
        "mandi": "Sri Muktsar Sahib",
        "district": "Sri Muktsar Sahib",
        "state": "Punjab",
        "commodity": "Cotton (Narma)",
        "commodity_hi": "कपास (नरमा)",
        "commodity_pa": "ਨਰਮਾ",
        "min_price": 7180,
        "max_price": 7650,
        "modal_price": 7480,
        "change": 75,
        "msp": 7121,
        "msp_status": "Above MSP (+₹359)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹359)",
        "msp_status_hi": "MSP से अधिक (+₹359)",
        "volume_qtl": 2900,
        "trend": [7320, 7360, 7400, 7430, 7450, 7480],
        "last_updated": "Today, 12:15 PM"
    },
    {
        "mandi": "Kotkapura",
        "district": "Faridkot",
        "state": "Punjab",
        "commodity": "Wheat (PBW-725)",
        "commodity_hi": "गेहूँ",
        "commodity_pa": "ਕਣਕ",
        "min_price": 2425,
        "max_price": 2525,
        "modal_price": 2480,
        "change": 25,
        "msp": 2425,
        "msp_status": "Above MSP (+₹55)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹55)",
        "msp_status_hi": "MSP से अधिक (+₹55)",
        "volume_qtl": 3800,
        "trend": [2430, 2445, 2455, 2465, 2470, 2480],
        "last_updated": "Today, 10:30 AM"
    },
    {
        "mandi": "Mansa",
        "district": "Mansa",
        "state": "Punjab",
        "commodity": "Mustard (Sarson)",
        "commodity_hi": "सरसों",
        "commodity_pa": "ਸਰ੍ਹੋਂ",
        "min_price": 5780,
        "max_price": 6120,
        "modal_price": 5990,
        "change": 50,
        "msp": 5650,
        "msp_status": "Above MSP (+₹340)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹340)",
        "msp_status_hi": "MSP से अधिक (+₹340)",
        "volume_qtl": 2100,
        "trend": [5850, 5890, 5920, 5940, 5970, 5990],
        "last_updated": "Today, 11:20 AM"
    },
    {
        "mandi": "Malerkotla",
        "district": "Malerkotla",
        "state": "Punjab",
        "commodity": "Fresh Green Peas (Matar)",
        "commodity_hi": "हरी मटर",
        "commodity_pa": "ਹਰੇ ਮਟਰ",
        "min_price": 3200,
        "max_price": 4100,
        "modal_price": 3750,
        "change": 150,
        "msp": 2800,
        "msp_status": "Vegetable High Demand",
        "msp_status_pa": "ਸਬਜ਼ੀ ਮੰਡੀ ਭਾਰੀ ਮੰਗ",
        "msp_status_hi": "सब्जी मंडी भारी मांग",
        "volume_qtl": 4500,
        "trend": [3400, 3480, 3550, 3620, 3690, 3750],
        "last_updated": "Today, 09:45 AM"
    },
    {
        "mandi": "Fazilka",
        "district": "Fazilka",
        "state": "Punjab",
        "commodity": "Moong (Green Gram)",
        "commodity_hi": "मूंग दाल",
        "commodity_pa": "ਮੂੰਗੀ",
        "min_price": 8200,
        "max_price": 8800,
        "modal_price": 8550,
        "change": 120,
        "msp": 8558,
        "msp_status": "At MSP Benchmark",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਦੇ ਬਰਾਬਰ",
        "msp_status_hi": "MSP के स्तर पर",
        "volume_qtl": 1600,
        "trend": [8300, 8360, 8420, 8470, 8510, 8550],
        "last_updated": "Today, 12:45 PM"
    },
    {
        "mandi": "Hoshiarpur",
        "district": "Hoshiarpur",
        "state": "Punjab",
        "commodity": "Kinnow (Grade A)",
        "commodity_hi": "किन्नू",
        "commodity_pa": "ਕਿੰਨੂ",
        "min_price": 2800,
        "max_price": 3600,
        "modal_price": 3300,
        "change": 80,
        "msp": 2500,
        "msp_status": "Citrus Belt Mandi",
        "msp_status_pa": "ਸਿਟਰਸ ਬਾਗਬਾਨੀ ਭਾਅ",
        "msp_status_hi": "फल मंडी भाव",
        "volume_qtl": 5800,
        "trend": [3100, 3150, 3190, 3230, 3270, 3300],
        "last_updated": "Today, 10:15 AM"
    },
    {
        "mandi": "Karnal",
        "district": "Karnal",
        "state": "Haryana",
        "commodity": "Basmati 1121 Paddy",
        "commodity_hi": "बासमती 1121 धान",
        "commodity_pa": "ਬਾਸਮਤੀ 1121 ਝੋਨਾ",
        "min_price": 4150,
        "max_price": 4480,
        "modal_price": 4390,
        "change": 80,
        "msp": 2300,
        "msp_status": "Above MSP (+₹2,090)",
        "msp_status_pa": "ਸਰਕਾਰੀ MSP ਤੋਂ ਵੱਧ (+₹2,090)",
        "msp_status_hi": "MSP से अधिक (+₹2,090)",
        "volume_qtl": 2800,
        "trend": [4190, 4240, 4300, 4320, 4350, 4390],
        "last_updated": "Today, 12:15 PM"
    }
]

WEATHER_DATA = {
    "location": "Ludhiana, Punjab",
    "district": "Ludhiana",
    "state": "Punjab",
    "temperature": 24,
    "condition": "Partly Sunny",
    "condition_pa": "ਹਲਕੀ ਧੁੱਪ / ਬੱਦਲਵਾਈ",
    "condition_hi": "हल्की धूप / आंशिक बादल",
    "humidity": 68,
    "wind_speed": 8,
    "wind_direction": "NW",
    "rain_chance": 12,
    "soil_temp": 21,
    "dew_point": 15,
    "spray_suitability": {
        "status": "Optimal",
        "status_pa": "ਬਿਲਕੁਲ ਅਨੁਕੂਲ (Optimal)",
        "status_hi": "पूर्णतः उपयुक्त (Optimal)",
        "score": 88,
        "color": "#16A34A",
        "advisory": "Excellent conditions for foliar spray. Wind speed is gentle (8 km/h) and no rainfall is forecast for the next 36 hours. Best spray window: 9:00 AM – 1:00 PM after morning dew evaporates.",
        "advisory_pa": "ਸਪਰੇਅ ਕਰਨ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮੌਸਮ। ਹਵਾ ਦੀ ਗਤੀ ਹਲਕੀ (8 km/h) ਹੈ ਅਤੇ ਅਗਲੇ 36 ਘੰਟਿਆਂ ਵਿੱਚ ਮੀਂਹ ਦੀ ਕੋਈ ਸੰਭਾਵਨਾ ਨਹੀਂ। ਸਭ ਤੋਂ ਢੁਕਵਾਂ ਸਮਾਂ: ਸਵੇਰੇ 9:00 ਤੋਂ ਦੁਪਹਿਰ 1:00 ਵਜੇ ਤੱਕ।",
        "advisory_hi": "पर्ण स्प्रे के लिए सर्वोत्तम मौसम। हवा की गति सामान्य (8 किमी/घंटा) है और अगले 36 घंटे बारिश का कोई पूर्वानुमान नहीं है। उत्तम समय: सुबह 9:00 से दोपहर 1:00 बजे।"
    },
    "irrigation_advice": "Soil moisture is adequate following previous light shower. Delay next irrigation of wheat by 4-5 days to stimulate root proliferation.",
    "irrigation_advice_pa": "ਪਿਛਲੇ ਦਿਨਾਂ ਦੀ ਹਲਕੀ ਬਾਰਿਸ਼ ਕਾਰਨ ਜ਼ਮੀਨ ਵਿੱਚ ਨਮੀ ਕਾਫ਼ੀ ਹੈ। ਕਣਕ ਦੀ ਅਗਲੀ ਸਿੰਚਾਈ 4-5 ਦਿਨ ਅੱਗੇ ਪਾਓ ਤਾਂ ਜੋ ਜੜ੍ਹਾਂ ਡੂੰਘੀਆਂ ਜਾ ਸਕਣ।",
    "irrigation_advice_hi": "पिछली हल्की बारिश से खेत में पर्याप्त नमी है। गेहूं की अगली सिंचाई 4-5 दिन टालें जिससे जड़ें गहरी जा सकें।",
    "forecast": [
        {"day": "Today", "day_pa": "ਅੱਜ", "day_hi": "आज", "date": "14 Oct", "temp_max": 28, "temp_min": 17, "rain_pct": 10, "condition": "Sunny", "wind": 8, "humidity": 65, "icon": "☀️"},
        {"day": "Thu", "day_pa": "ਵੀਰ", "day_hi": "गुरु", "date": "15 Oct", "temp_max": 27, "temp_min": 16, "rain_pct": 15, "condition": "Partly Cloudy", "wind": 10, "humidity": 70, "icon": "⛅"},
        {"day": "Fri", "day_pa": "ਸ਼ੁੱਕਰ", "day_hi": "शुक्र", "date": "16 Oct", "temp_max": 26, "temp_min": 15, "rain_pct": 20, "condition": "Clear", "wind": 9, "humidity": 68, "icon": "☀️"},
        {"day": "Sat", "day_pa": "ਸ਼ਨੀ", "day_hi": "शनि", "date": "17 Oct", "temp_max": 25, "temp_min": 14, "rain_pct": 65, "condition": "Thunder Showers", "wind": 18, "humidity": 84, "icon": "🌧️"},
        {"day": "Sun", "day_pa": "ਐਤ", "day_hi": "रवि", "date": "18 Oct", "temp_max": 24, "temp_min": 14, "rain_pct": 45, "condition": "Scattered Rain", "wind": 14, "humidity": 78, "icon": "🌦️"},
        {"day": "Mon", "day_pa": "ਸੋਮ", "day_hi": "सोम", "date": "19 Oct", "temp_max": 26, "temp_min": 15, "rain_pct": 10, "condition": "Sunny", "wind": 7, "humidity": 62, "icon": "☀️"},
        {"day": "Tue", "day_pa": "ਮੰਗਲ", "day_hi": "मंगल", "date": "20 Oct", "temp_max": 27, "temp_min": 16, "rain_pct": 5, "condition": "Clear", "wind": 8, "humidity": 59, "icon": "☀️"}
    ],
    "agri_alerts": [
        {
            "id": "alrt_rain_weekend",
            "type": "weather",
            "severity": "Amber",
            "title": "Moderate Rain Expected on Saturday (17 Oct)",
            "title_pa": "ਸ਼ਨੀਵਾਰ ਨੂੰ ਮੀਂਹ ਪੈਣ ਦੀ ਸੰਭਾਵਨਾ",
            "title_hi": "शनिवार को बारिश की संभावना",
            "message": "Western disturbance activity will bring light-to-moderate showers. Postpone scheduled urea top-dressing and chemical sprays until Sunday evening.",
            "message_pa": "ਪੱਛਮੀ ਗੜਬੜੀ ਕਾਰਨ ਹਲਕੀ-ਦਰਮਿਆਨੀ ਬਾਰਿਸ਼ ਹੋ ਸਕਦੀ ਹੈ। ਯੂਰੀਆ ਦਾ ਛੱਟਾ ਦੇਣਾ ਅਤੇ ਕੀਟਨਾਸ਼ਕ ਸਪਰੇਅ ਐਤਵਾਰ ਸ਼ਾਮ ਤੱਕ ਟਾਲ ਦਿਓ।",
            "message_hi": "पश्चिमी विक्षोभ के कारण हल्की से मध्यम बारिश हो सकती है। यूरिया छिड़काव व कीटनाशक स्प्रे रविवार तक टालें।"
        },
        {
            "id": "alrt_rust_dew",
            "type": "disease",
            "severity": "Red",
            "title": "Stripe Rust Spore Advisory in Foothill Belts",
            "title_pa": "ਪਹਾੜੀ ਇਲਾਕਿਆਂ ਨੇੜੇ ਪੀਲੀ ਕੁੰਗੀ ਦੀ ਚੇਤਾਵਨੀ",
            "title_hi": "तराई क्षेत्रों में पीला रतुआ बीजाणु चेतावनी",
            "message": "High night humidity (>85%) and temperature drop creates conducive conditions for Yellow Rust in sub-mountainous blocks of Ropar and Hoshiarpur. Inspect wheat fields daily.",
            "message_pa": "ਰਾਤ ਨੂੰ 85% ਤੋਂ ਵੱਧ ਨਮੀ ਅਤੇ ਠੰਢ ਕਾਰਨ ਰੋਪੜ ਤੇ ਹੁਸ਼ਿਆਰਪੁਰ ਜ਼ਿਲ੍ਹਿਆਂ ਵਿੱਚ ਪੀਲੀ ਕੁੰਗੀ ਦੇ ਫੈਲਣ ਦਾ ਖ਼ਤਰਾ ਹੈ। ਕਣਕ ਦੇ ਖੇਤਾਂ ਦਾ ਰੋਜ਼ ਮੁਆਇਨਾ ਕਰੋ।",
            "message_hi": "रात में 85% से अधिक नमी व ठंड के कारण रोपड़ व होशियारपुर में पीला रतुआ फैलने का खतरा है। गेहूं के खेतों का दैनिक निरीक्षण करें।"
        }
    ]
}

DEFAULT_FARM = {
    "farmer_name": "Amritpal Singh Gill",
    "email": "gillamritpal2007-1@gmail.com",
    "phone": "9876543210",
    "village": "Gill Kalan",
    "district": "Ludhiana",
    "state": "Punjab",
    "total_acres": 18.5,
    "tubewells": 2,
    "primary_crop": "Wheat, Paddy & Mustard",
    "plots": [
        {
            "id": "plot_1",
            "name": "Khet 1 - North Tubewell Parcel",
            "name_pa": "ਖੇਤ 1 - ਉੱਤਰੀ ਟਿਊਬਵੈੱਲ ਟੱਕ",
            "name_hi": "खेत 1 - उत्तरी नलकूप चक",
            "acres": 6.5,
            "crop": "Wheat",
            "crop_pa": "ਕਣਕ",
            "crop_hi": "गेहूँ",
            "variety": "PBW-826 (Rust Tolerant)",
            "sowing_date": "12 Nov 2025",
            "stage": "Tillering & Jointing",
            "irrigation_type": "Laser Levelled Furrow",
            "health_score": 92,
            "status": "Healthy",
            "status_pa": "ਤੰਦਰੁਸਤ",
            "status_hi": "स्वस्थ"
        },
        {
            "id": "plot_2",
            "name": "Khet 2 - Roadside Canal Plot",
            "name_pa": "ਖੇਤ 2 - ਸੂਏ ਵਾਲਾ ਟੱਕ",
            "name_hi": "खेत 2 - नहर किनारा चक",
            "acres": 4.5,
            "crop": "Mustard",
            "crop_pa": "ਸਰ੍ਹੋਂ",
            "crop_hi": "सरसों",
            "variety": "Giriraj (High Oil 42%)",
            "sowing_date": "28 Oct 2025",
            "stage": "Pod / Siliqua Formation",
            "irrigation_type": "Sprinkler Irrigation",
            "health_score": 88,
            "status": "Monitored",
            "status_pa": "ਨਿਗਰਾਨੀ ਹੇਠ",
            "status_hi": "निगरानी में"
        },
        {
            "id": "plot_3",
            "name": "Khet 3 - Homestead Vegetable Patch",
            "name_pa": "ਖੇਤ 3 - ਘਰ ਵਾਲਾ ਆਲੂ ਟੱਕ",
            "name_hi": "खेत 3 - आलू चक",
            "acres": 3.5,
            "crop": "Potato",
            "crop_pa": "ਆਲੂ",
            "crop_hi": "आलू",
            "variety": "Kufri Pukhraj",
            "sowing_date": "18 Oct 2025",
            "stage": "Tuber Bulking",
            "irrigation_type": "Drip System",
            "health_score": 85,
            "status": "Treatment Applied",
            "status_pa": "ਇਲਾਜ ਕੀਤਾ ਗਿਆ",
            "status_hi": "उपचार किया गया"
        }
    ],
    "soil_health": {
        "ph": 7.3,
        "ph_status": "Optimal Neutral",
        "ph_status_pa": "ਬਿਲਕੁਲ ਸਹੀ (Neutral)",
        "ph_status_hi": "सर्वोत्तम उदासीन (Neutral)",
        "ec": 0.34,
        "ec_status": "Normal (< 1.0 dS/m)",
        "organic_carbon": 0.58,
        "oc_status": "Medium (0.50 - 0.75%)",
        "nitrogen": 218,
        "nitrogen_status": "Low (< 280 kg/ha)",
        "phosphorus": 24.5,
        "phosphorus_status": "Medium (23 - 56 kg/ha)",
        "potassium": 295,
        "potassium_status": "High (> 280 kg/ha)",
        "zinc": 0.62,
        "zinc_status": "Deficient (< 0.8 ppm - Add Zinc 21%)",
        "last_tested": "15 Sep 2025 by Soil Testing Lab, PAU Ludhiana"
    },
    "diagnosis_history": [
        {
            "id": "diag_01",
            "date": "10 Oct 2026",
            "crop": "Wheat",
            "disease": "Yellow Rust (Early Inception)",
            "severity": "Moderate",
            "confidence": 94.2,
            "treatment_taken": "Sprayed Propiconazole 25% EC (Tilt)",
            "status": "Resolved"
        },
        {
            "id": "diag_02",
            "date": "28 Sep 2026",
            "crop": "Potato",
            "disease": "Early Blight",
            "severity": "Low",
            "confidence": 91.8,
            "treatment_taken": "Applied Mancozeb 75% WP @ 2.5g/L",
            "status": "Resolved"
        }
    ]
}

FARM_PROFILES_MAP = {
    "farmer_gill": {
        "farmer_name": "Amritpal Singh Gill",
        "email": "gillamritpal2007-1@gmail.com",
        "phone": "9876543210",
        "village": "Gill Kalan",
        "district": "Ludhiana",
        "state": "Punjab",
        "kisan_id": "PB-LDH-2026-0701",
        "shc_id": "PAU-SHC-2007",
        "total_acres": 18.5,
        "tubewells": 2,
        "primary_crop": "Wheat, Paddy & Mustard",
        "plots": [
            {
                "id": "plot_g1",
                "name": "Khet 1 - North Tubewell Parcel",
                "name_pa": "ਖੇਤ 1 - ਉੱਤਰੀ ਟਿਊਬਵੈੱਲ ਟੱਕ",
                "name_hi": "खेत 1 - उत्तरी नलकूप चक",
                "acres": 6.5,
                "crop": "Wheat",
                "crop_pa": "ਕਣਕ",
                "crop_hi": "गेहूँ",
                "variety": "PBW-826 (Rust Tolerant)",
                "sowing_date": "12 Nov 2025",
                "stage": "Tillering & Jointing",
                "irrigation_type": "Laser Levelled Furrow",
                "health_score": 92,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            },
            {
                "id": "plot_g2",
                "name": "Khet 2 - Roadside Canal Plot",
                "name_pa": "ਖੇਤ 2 - ਸੂਏ ਵਾਲਾ ਟੱਕ",
                "name_hi": "खेत 2 - नहर किनारा चक",
                "acres": 4.5,
                "crop": "Mustard",
                "crop_pa": "ਸਰ੍ਹੋਂ",
                "crop_hi": "सरसों",
                "variety": "Giriraj (High Oil 42%)",
                "sowing_date": "28 Oct 2025",
                "stage": "Pod / Siliqua Formation",
                "irrigation_type": "Sprinkler Irrigation",
                "health_score": 88,
                "status": "Monitored",
                "status_pa": "ਨਿਗਰਾਨੀ ਹੇਠ",
                "status_hi": "निगरानी में"
            },
            {
                "id": "plot_g3",
                "name": "Khet 3 - Homestead Vegetable Patch",
                "name_pa": "ਖੇਤ 3 - ਘਰ ਵਾਲਾ ਆਲੂ ਟੱਕ",
                "name_hi": "खेत 3 - आलू चक",
                "acres": 3.5,
                "crop": "Potato",
                "crop_pa": "ਆਲੂ",
                "crop_hi": "आलू",
                "variety": "Kufri Pukhraj",
                "sowing_date": "18 Oct 2025",
                "stage": "Tuber Bulking",
                "irrigation_type": "Drip System",
                "health_score": 85,
                "status": "Treatment Applied",
                "status_pa": "ਇਲਾਜ ਕੀਤਾ ਗਿਆ",
                "status_hi": "उपचार किया गया"
            },
            {
                "id": "plot_g4",
                "name": "Khet 4 - Solar Borewell Fodder Parcel",
                "name_pa": "ਖੇਤ 4 - ਸੋਲਰ ਬੋਰਵੈੱਲ ਚਾਰਾ ਟੱਕ",
                "name_hi": "खेत 4 - सोलर बोरवेल चारा चक",
                "acres": 4.0,
                "crop": "Berseem",
                "crop_pa": "ਬਰਸੀਮ",
                "crop_hi": "बरसीम",
                "variety": "BL-42 Multi-Cut",
                "sowing_date": "02 Nov 2025",
                "stage": "Second Vegetative Cutting",
                "irrigation_type": "Solar Submersible Flooding",
                "health_score": 95,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            }
        ],
        "soil_health": {
            "ph": 7.3,
            "ph_status": "Optimal Neutral",
            "ph_status_pa": "ਬਿਲਕੁਲ ਸਹੀ (Neutral)",
            "ph_status_hi": "सर्वोत्तम उदासीन (Neutral)",
            "ec": 0.34,
            "ec_status": "Normal (< 1.0 dS/m)",
            "organic_carbon": 0.58,
            "oc_status": "Medium (0.50 - 0.75%)",
            "nitrogen": 218,
            "nitrogen_status": "Low (< 280 kg/ha)",
            "phosphorus": 24.5,
            "phosphorus_status": "Medium (23 - 56 kg/ha)",
            "potassium": 295,
            "potassium_status": "High (> 280 kg/ha)",
            "zinc": 0.62,
            "zinc_status": "Deficient (< 0.8 ppm - Add Zinc 21%)",
            "last_tested": "15 Sep 2025 by Soil Testing Lab, PAU Ludhiana",
            "advice": "Nitrogen and Zinc are below optimal thresholds. Apply 21% Zinc Sulphate spray (1kg/acre) with first irrigation and supplement basal urea with IFFCO Nano Urea foliar spray."
        },
        "diagnosis_history": [
            {
                "id": "diag_g1",
                "date": "10 Oct 2026",
                "crop": "Wheat",
                "disease": "Yellow Rust (Early Inception)",
                "severity": "Moderate",
                "confidence": 94.2,
                "treatment_taken": "Sprayed Propiconazole 25% EC (Tilt)",
                "status": "Resolved"
            },
            {
                "id": "diag_g2",
                "date": "28 Sep 2026",
                "crop": "Potato",
                "disease": "Early Blight",
                "severity": "Low",
                "confidence": 91.8,
                "treatment_taken": "Applied Mancozeb 75% WP @ 2.5g/L",
                "status": "Resolved"
            }
        ]
    },
    "farmer_1": {
        "farmer_name": "Sardar Gurpreet Singh",
        "email": "gurpreet.singh@gmail.com",
        "phone": "9876543211",
        "village": "Bhamian Kalan",
        "district": "Ludhiana",
        "state": "Punjab",
        "kisan_id": "PB-LU-2026-8812",
        "shc_id": "PAU-SHC-9042",
        "total_acres": 14.5,
        "tubewells": 2,
        "primary_crop": "Wheat & Mustard",
        "plots": [
            {
                "id": "plot_1_1",
                "name": "Khet 1 - Main Dera Khet",
                "name_pa": "ਖੇਤ 1 - ਡੇਰੇ ਵਾਲਾ ਮੁੱਖ ਟੱਕ",
                "name_hi": "खेत 1 - मुख्य डेरा चक",
                "acres": 7.0,
                "crop": "Wheat",
                "crop_pa": "ਕਣਕ",
                "crop_hi": "गेहूँ",
                "variety": "HD-3086 Pusa Gautami",
                "sowing_date": "08 Nov 2025",
                "stage": "Booting & Heading",
                "irrigation_type": "Underground Pipeline Furrow",
                "health_score": 94,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            },
            {
                "id": "plot_1_2",
                "name": "Khet 2 - Canal Road Block",
                "name_pa": "ਖੇਤ 2 - ਨਹਿਰੀ ਸੜਕ ਟੱਕ",
                "name_hi": "खेत 2 - नहर सड़क चक",
                "acres": 4.5,
                "crop": "Mustard",
                "crop_pa": "ਸਰ੍ਹੋਂ",
                "crop_hi": "सरसों",
                "variety": "Pusa Bold (Certified)",
                "sowing_date": "22 Oct 2025",
                "stage": "Siliqua Ripening",
                "irrigation_type": "Sprinkler Irrigation",
                "health_score": 89,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            },
            {
                "id": "plot_1_3",
                "name": "Khet 3 - East Garden Orchard",
                "name_pa": "ਖੇਤ 3 - ਪੂਰਬੀ ਕਿੰਨੂ ਬਾਗ਼",
                "name_hi": "खेत 3 - पूर्वी किन्नू बाग",
                "acres": 3.0,
                "crop": "Kinnow Citrus",
                "crop_pa": "ਕਿੰਨੂ ਬਾਗ਼",
                "crop_hi": "किन्नू बाग",
                "variety": "Daisy Mandarin Hybrid",
                "sowing_date": "Perennial Orchard (4th Year)",
                "stage": "Fruit Maturation & Color Break",
                "irrigation_type": "Automated Drip Fertigation",
                "health_score": 96,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            }
        ],
        "soil_health": {
            "ph": 7.1,
            "ph_status": "Optimal Neutral",
            "ph_status_pa": "ਬਿਲਕੁਲ ਸਹੀ (Neutral)",
            "ph_status_hi": "सर्वोत्तम उदासीन (Neutral)",
            "ec": 0.28,
            "ec_status": "Normal (< 1.0 dS/m)",
            "organic_carbon": 0.64,
            "oc_status": "Medium-High (0.60 - 0.75%)",
            "nitrogen": 240,
            "nitrogen_status": "Medium (240 - 280 kg/ha)",
            "phosphorus": 28.5,
            "phosphorus_status": "Optimal (25 - 50 kg/ha)",
            "potassium": 315,
            "potassium_status": "High (> 280 kg/ha)",
            "zinc": 0.78,
            "zinc_status": "Optimal (> 0.75 ppm)",
            "last_tested": "22 Aug 2025 by KVK Samrala, Ludhiana",
            "advice": "Soil pH is in optimal neutral range (7.1). Nitrogen and micronutrient balance is healthy. Incorporate Dhaincha green manure in summer gap."
        },
        "diagnosis_history": [
            {
                "id": "diag_1_1",
                "date": "04 Oct 2026",
                "crop": "Kinnow Citrus",
                "disease": "Citrus Canker Inspection",
                "severity": "Low",
                "confidence": 96.0,
                "treatment_taken": "Foliar Copper Oxychloride 50 WP",
                "status": "Prevented & Clean"
            }
        ]
    },
    "farmer_2": {
        "farmer_name": "Ramesh Patel",
        "email": "ramesh.patel@gmail.com",
        "phone": "9812345678",
        "village": "Mogar",
        "district": "Anand",
        "state": "Gujarat",
        "kisan_id": "GJ-AN-2026-4421",
        "shc_id": "AAU-SHC-3120",
        "total_acres": 9.0,
        "tubewells": 1,
        "primary_crop": "Cotton & Groundnut",
        "plots": [
            {
                "id": "plot_2_1",
                "name": "Khet 1 - Narmada Canal Field",
                "name_pa": "ਖੇਤ 1 - ਨਰਮਦਾ ਨਹਿਰ ਟੱਕ",
                "name_hi": "खेत 1 - नर्मदा नहर चक",
                "acres": 5.0,
                "crop": "BT Cotton",
                "crop_pa": "ਨਰਮਾ ਕਪਾਹ",
                "crop_hi": "कपास (BT Cotton)",
                "variety": "RCH-659 BG-II",
                "sowing_date": "15 Jun 2025",
                "stage": "Boll Bursting & First Picking",
                "irrigation_type": "Drip Irrigation",
                "health_score": 90,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            },
            {
                "id": "plot_2_2",
                "name": "Khet 2 - Well-side Black Soil Plot",
                "name_pa": "ਖੇਤ 2 - ਖੂਹ ਵਾਲੀ ਕਾਲੀ ਮਿੱਟੀ ਟੱਕ",
                "name_hi": "खेत 2 - कुआं काली मिट्टी चक",
                "acres": 4.0,
                "crop": "Groundnut",
                "crop_pa": "ਮੂੰਗਫਲੀ",
                "crop_hi": "मूंगफली",
                "variety": "GG-20 Semi-Spreading",
                "sowing_date": "04 Jul 2025",
                "stage": "Pod Maturity & Harvesting",
                "irrigation_type": "Micro-Sprinklers",
                "health_score": 87,
                "status": "Monitored",
                "status_pa": "ਨਿਗਰਾਨੀ ਹੇਠ",
                "status_hi": "निगरानी में"
            }
        ],
        "soil_health": {
            "ph": 7.8,
            "ph_status": "Slightly Alkaline",
            "ph_status_pa": "ਹਲਕਾ ਖਾਰਾ (Alkaline)",
            "ph_status_hi": "हल्का क्षारीय (Alkaline)",
            "ec": 0.45,
            "ec_status": "Normal (< 1.0 dS/m)",
            "organic_carbon": 0.49,
            "oc_status": "Low-Medium (< 0.50%)",
            "nitrogen": 195,
            "nitrogen_status": "Deficient (< 200 kg/ha)",
            "phosphorus": 19.2,
            "phosphorus_status": "Low (< 20 kg/ha)",
            "potassium": 340,
            "potassium_status": "Rich (> 300 kg/ha)",
            "zinc": 0.55,
            "zinc_status": "Deficient (< 0.60 ppm)",
            "last_tested": "10 Jul 2025 by Soil Lab, AAU Anand",
            "advice": "Alkaline tendencies observed (pH 7.8). Apply gypsum @ 100 kg/acre and spray Zinc EDTA (12%) to treat yellowing in cotton bolls."
        },
        "diagnosis_history": [
            {
                "id": "diag_2_1",
                "date": "15 Sep 2026",
                "crop": "Cotton",
                "disease": "Whitefly & Leaf Curl Virus Check",
                "severity": "Mild",
                "confidence": 92.5,
                "treatment_taken": "Yellow Sticky Traps + Neem Oil 10,000 ppm",
                "status": "Managed"
            }
        ]
    },
    "farmer_3": {
        "farmer_name": "Chaudhary Rajendra Sharma",
        "email": "rajendra.sharma@gmail.com",
        "phone": "9923456789",
        "village": "Daurala",
        "district": "Meerut",
        "state": "Uttar Pradesh",
        "kisan_id": "UP-ME-2026-9034",
        "shc_id": "SVPU-SHC-8819",
        "total_acres": 18.0,
        "tubewells": 3,
        "primary_crop": "Sugarcane & Wheat",
        "plots": [
            {
                "id": "plot_3_1",
                "name": "Khet 1 - Ganga Canal Sugarcane Block",
                "name_pa": "ਖੇਤ 1 - ਗੰਗਾ ਨਹਿਰ ਗੰਨਾ ਟੱਕ",
                "name_hi": "खेत 1 - गंगा नहर गन्ना चक",
                "acres": 10.0,
                "crop": "Sugarcane",
                "crop_pa": "ਗੰਨਾ",
                "crop_hi": "गन्ना (Sugarcane)",
                "variety": "Co-0238 (Karan-4)",
                "sowing_date": "18 Mar 2025",
                "stage": "Cane Grand Growth & Sugar Accumulation",
                "irrigation_type": "Furrow Flooding",
                "health_score": 93,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            },
            {
                "id": "plot_3_2",
                "name": "Khet 2 - Chajju Tubewell Khet",
                "name_pa": "ਖੇਤ 2 - ਛੱਜੂ ਟਿਊਬਵੈੱਲ ਟੱਕ",
                "name_hi": "खेत 2 - छज्जू नलकूप चक",
                "acres": 5.0,
                "crop": "Wheat",
                "crop_pa": "ਕਣਕ",
                "crop_hi": "गेहूँ",
                "variety": "DBW-187 (Karan Vandana)",
                "sowing_date": "14 Nov 2025",
                "stage": "Tillering Stage",
                "irrigation_type": "Laser Levelled Furrow",
                "health_score": 95,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            },
            {
                "id": "plot_3_3",
                "name": "Khet 3 - Village Road Plot",
                "name_pa": "ਖੇਤ 3 - ਪਿੰਡ ਵਾਲੀ ਸੜਕ ਟੱਕ",
                "name_hi": "खेत 3 - गाँव सड़क चक",
                "acres": 3.0,
                "crop": "Mustard",
                "crop_pa": "ਸਰ੍ਹੋਂ",
                "crop_hi": "सरसों",
                "variety": "Varuna (T-59)",
                "sowing_date": "25 Oct 2025",
                "stage": "Pod Formation",
                "irrigation_type": "Tubewell Furrow",
                "health_score": 91,
                "status": "Healthy",
                "status_pa": "ਤੰਦਰੁਸਤ",
                "status_hi": "स्वस्थ"
            }
        ],
        "soil_health": {
            "ph": 7.4,
            "ph_status": "Optimal Neutral",
            "ph_status_pa": "ਬਿਲਕੁਲ ਸਹੀ (Neutral)",
            "ph_status_hi": "सर्वोत्तम उदासीन (Neutral)",
            "ec": 0.32,
            "ec_status": "Normal (< 1.0 dS/m)",
            "organic_carbon": 0.55,
            "oc_status": "Medium (0.50 - 0.75%)",
            "nitrogen": 215,
            "nitrogen_status": "Low-Medium (200 - 250 kg/ha)",
            "phosphorus": 22.0,
            "phosphorus_status": "Medium (20 - 45 kg/ha)",
            "potassium": 280,
            "potassium_status": "Optimal (250 - 300 kg/ha)",
            "zinc": 0.68,
            "zinc_status": "Medium (0.6 - 1.0 ppm)",
            "last_tested": "05 Jun 2025 by Soil Testing Lab, SVPU Meerut",
            "advice": "Soil condition is well-buffered. Use bio-fertilizer Azotobacter for sugarcane ratoon and apply potash after first earthing up."
        },
        "diagnosis_history": [
            {
                "id": "diag_3_1",
                "date": "18 Aug 2026",
                "crop": "Sugarcane",
                "disease": "Top Borer & Red Rot Surveillance",
                "severity": "Low",
                "confidence": 95.5,
                "treatment_taken": "Trichoderma harzianum soil drenching",
                "status": "Healthy & Clean"
            }
        ]
    }
}

CONFIGURABLE_STATS = {
    "crops_supported": 34,
    "languages_supported": 3,
    "diagnoses_completed": "184,520+",
    "markets_tracked": 128,
    "accuracy_rate": "96.4%",
    "farmers_served": "52,000+"
}
