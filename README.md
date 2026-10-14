# 🌾 FIELDAI — Precision Agriculture & Crop Intelligence Platform

> **“Smarter Farming. Healthier Crops. Better Decisions.”**  
> A premium, full-stack Indian agritech platform combining modern fintech/SaaS cleanliness with agricultural warmth. Built specifically for Indian farmers with native support for **English**, **ਪੰਜਾਬੀ (Punjabi)**, and **हिन्दी (Hindi)**.

---

## 🚀 Live Access

The application server is actively running on:
**[http://127.0.0.1:5050](http://127.0.0.1:5050)**

To run or restart manually at any time:
```powershell
cd C:\Users\sherr\.gemini\antigravity\scratch\fieldai
.\run.bat
# or
$env:PORT="5050"; python server.py
```

---

## 🎨 Visual Identity & Design System

FIELDAI avoids generic AI stock templates and neon gradients in favor of an **Apple-grade, fintech-inspired agricultural UI**:

| Token | Hex | Role |
| :--- | :--- | :--- |
| **Forest Green (Primary)** | `#133E2B` | Brand identity, primary buttons, headers |
| **Leaf Green (Positive)** | `#16A34A` / `#22C55E` | Optimal weather, above-MSP prices, healthy states |
| **Warm Off-White / Cream** | `#FBFBF7` | Platform background for reduced eye fatigue in outdoor sunlight |
| **Dark Charcoal** | `#1C1E1B` | High-contrast readable typography |
| **Earthy Beige (Surfaces)** | `#F2EFE9` / `#EDE8DC` | Secondary cards, pill filters, badges |
| **Amber (Highlights)** | `#D97706` | Alerts, weather warnings, commodity highlights |
| **Red (Severe State)** | `#DC2626` | High-severity pathology, crop disease warnings |

- **Typography:** *Plus Jakarta Sans* & *Inter*
- **Corner Radii:** Consistent 12–18px (`rounded-xl` / `rounded-2xl`)
- **Spacing:** Generous whitespace, subtle borders (`border-[#E4E0D5]`), and soft micro-elevations (`shadow-sm`)
- **Mobile First Adaptation:** Native Android bottom navigation bar (`Home / Diagnose / AI / Market / Profile`)

---

## 🌟 Key Modules & Features

### 1. 🔬 Crop Doctor — AI Disease Detection
- **Multi-source image capture:**
  - Phone Camera capture (`capture="environment"`)
  - Gallery upload (JPG/PNG drag & drop)
  - Quick sample crop leaves for instant testing (*Wheat Yellow Rust*, *Rice Blast*, *Cotton Leaf Curl*, *Mustard White Rust*, *Potato Late Blight*, *Tomato Early Blight*)
- **Pre-Analysis Context Questionnaire:**
  - Crop selection (34+ supported crops)
  - Crop Growth Stage (e.g. Crown Root Initiation, Tillering, Heading)
  - Farm location (District/State)
  - Observed visual symptoms
- **Interactive Vision Scanning HUD:**
  - Laser sweep overlay with animated pathology inspection
- **Comprehensive Diagnosis Panel:**
  - Scientific pathogen name & severity score
  - Confidence calculation (e.g., 94.8% – 97.4%)
  - **Dynamic `<canvas>` Bounding Boxes:** Highlights pathological lesions and uredinia stripes directly on the leaf with confidence tags
  - Visible symptoms breakdown, likely environmental triggers, recommended next steps, and long-term prevention
  - **Statutory Warning:** *"AI assessment — verify severe cases with an agricultural expert."*
  - **1-Click Connected Actions:**
    - *"Ask AI about this diagnosis"* (injects context into AI assistant)
    - *"Save to My Farm Log"* (persists to digital records)
    - *"Find Suitable Treatment"* (pre-filters marketplace to approved remedies)

---

### 2. 🛡️ Treatment & Pesticide Marketplace
- **CIBRC Regulatory Compliance:** All chemical and bio-inputs reflect authentic Central Insecticides Board & Registration Committee labels.
- **Product Layout:** Amazon/fintech-style card grid with active formulations (*Propiconazole 25% EC, Tebuconazole + Trifloxystrobin, Azoxystrobin, Chlorantraniliprole, Nano Urea, etc.*)
- **Filters:** Fungicides, Insecticides, Bio-controls, Fertilizers, Certified Seeds.
- **Detailed Safety Modal:**
  - Pre-Harvest Interval (PHI in days)
  - Mandatory PPE icons (Nitrile Gloves, N95 Mask, Eye Shields)
  - Dilution & knapsack tank mixing ratios
  - Clear statutory disclaimer: *"Use agricultural chemicals only according to the approved product label and local agricultural guidance."*
- **Cart & Kisan Checkout Drawer:**
  - Item increment/decrement
  - Government / Kisan subsidy discount code (`KISAN2026`)
  - Doorstep delivery simulation with Kisan Credit Card / UPI payment options.

---

### 3. 🤖 Multilingual AI Farming Assistant
- **ChatGPT-Style Natural Agronomist Chat:**
  - Full conversational fluency in **ਪੰਜਾਬੀ (Punjabi)**, **हिन्दी (Hindi)**, and **English**
  - Instant prompt chips:
    - *"ਮੇਰੀ ਕਣਕ ਦੇ ਪੱਤੇ ਪੀਲੇ ਕਿਉਂ ਹੋ ਰਹੇ ਹਨ?"*
    - *"Should I irrigate my wheat tomorrow?"*
    - *"What fertilizer should be used at this growth stage?"*
    - *"आज बारिश होने वाली है, मुझे क्या करना चाहिए?"*
- **Speech Recognition & Audio Playback:**
  - Microphone button via Web Speech API
  - Audio text-to-speech speaker button on AI responses
- **Context-Aware Reasoning:** Aware of the user's current farm location (*Ludhiana, Punjab*), current weather, and recently diagnosed crop disease.

---

### 4. 📈 Live Mandi Prices (APMC Benchmark)
- Real-time modal prices, minimum/maximum trading ranges, and volume (quintals/day) across major Indian mandis (*Khanna, Karnal, Rajpura, Sri Ganganagar, Bathinda, Indore, Bareilly, Lasalgaon, Jalandhar, Kota*).
- **MSP Comparison Badge:** Compares prices against official Government Minimum Support Price benchmarks (e.g. *Above MSP (+₹55)*).
- Search & state filtering with 7-day modal price trend sparklines.

---

### 5. 🌦️ Smart Weather & Foliar Spray Advisory
- Field-level temperature, humidity, wind velocity, and rainfall radar.
- **Foliar Spray Suitability Index:** Real-time percentage score calculating whether wind speed, rain probability, and dew allow safe, drift-free chemical spraying.
- 7-Day agricultural risk forecast with Western Disturbance and frost advisories.

---

### 6. 📋 My Farm (Digital Land Parcels & Soil Health Card)
- **Field Parcel Tracker:** Add and monitor distinct plots (*Khet 1, Khet 2, Khet 3*) with variety, sowing date, and irrigation methods.
- **Soil Health Card:** pH, EC, Organic Carbon, Nitrogen, Phosphorus, Potassium, and Zinc status with PAU lab-aligned recommendations.
- **Diagnosis Logbook:** History of previous scans and interventions.

---

## 🛠️ Architecture & Technology Stack

- **Backend:** Python 3.11, Flask 3.1, Flask-CORS, RESTful JSON API
- **Frontend:** Vanilla ES6+, Tailwind CSS CDN, Google Fonts (Plus Jakarta Sans & Inter), Canvas API, Web Speech API (Voice Input & TTS)
- **Assets:** High-fidelity generated agricultural pathology leaf textures and authentic agrochemical product packaging
- **Localization:** 164 multilingual keys per language with live zero-reload translation switching.

---

© 2026 FIELDAI Technologies Pvt. Ltd. Dedicated to the Prosperity of Indian Farmers.
