/**
 * FIELDAI - Core Application Logic
 * Premium Fintech/SaaS Agricultural Platform for Indian Farmers
 * Full-Stack Client with Multilingual Engine, Vision Diagnostics,
 * Farmer OTP Authentication, Direct Multi-Option Payment Gateway,
 * and Agritech Developer Debug & Diagnostics HUD.
 */

// Global Debug Log and API Fetch Interceptor
const debugLogs = [];
function logDebugEvent(action, status, ms, type = 'info', detail = '') {
  const timestamp = new Date().toLocaleTimeString();
  const entry = { action, status, ms, type, detail, timestamp };
  debugLogs.unshift(entry);
  if (debugLogs.length > 50) debugLogs.pop();
  
  const container = document.getElementById('dbg-logs-container');
  if (container) {
    const row = document.createElement('div');
    row.className = `flex justify-between items-center py-1 border-b border-gray-800 ${type === 'error' ? 'text-rose-400' : type === 'success' ? 'text-emerald-400' : 'text-gray-300'}`;
    row.innerHTML = `
      <div>
        <span class="text-gray-500 font-mono text-[10px] mr-1.5">[${timestamp}]</span>
        <strong>${action}</strong>
      </div>
      <div class="flex items-center space-x-2">
        <span class="text-[10px] px-1.5 py-0.5 rounded ${status === 200 || status === 'OK' ? 'bg-emerald-950 text-emerald-400' : 'bg-rose-950 text-rose-400'}">${status}</span>
        <span class="text-gray-500 text-[10px]">${ms}ms</span>
      </div>
    `;
    container.insertBefore(row, container.firstChild);
  }
}

// Intercept window.fetch for real-time Debug HUD logging
const originalFetch = window.fetch;
window.fetch = async function(...args) {
  const startTime = performance.now();
  const rawUrl = typeof args[0] === 'string' ? args[0] : (args[0]?.url || 'API');
  const url = rawUrl.replace(window.location.origin, '');
  const method = args[1]?.method || 'GET';
  try {
    const res = await originalFetch.apply(this, args);
    const duration = Math.round(performance.now() - startTime);
    logDebugEvent(`${method} ${url}`, res.status, duration, res.ok ? 'success' : 'error');
    return res;
  } catch (err) {
    const duration = Math.round(performance.now() - startTime);
    logDebugEvent(`${method} ${url}`, 'ERR', duration, 'error', err.message);
    throw err;
  }
};

// Application State
const state = {
  currentLang: localStorage.getItem('fieldai_lang') || 'en',
  currentTab: 'home',
  translations: {},
  crops: [],
  stats: {},
  weather: null,
  products: [],
  activeFilter: 'All',
  mandiList: [],
  mandiFilter: { q: '', state: 'all' },
  activeDiagnosis: null,
  farmData: null,
  activeFarmer: null,
  demoFarmers: [],
  cart: [],
  farmerOrders: [],
  chatHistory: [],
  speechRecognizer: null,
  isListening: false,
  activeOrder: null,
  activePayMethod: 'upi',
  configuredUpiId: localStorage.getItem('fieldai_upi_id') || 'gillamritpal2007-1@okicici'
};

// DOM Content Loaded Initializer
document.addEventListener('DOMContentLoaded', () => {
  setupSpeechRecognition();

  // 1. Synchronously bind all DOM event listeners immediately
  bindNavigation();
  bindDiagnosisEvents();
  bindShopEvents();
  bindChatEvents();
  bindMandiEvents();
  bindWeatherEvents();
  bindFarmEvents();
  bindCartEvents();
  bindAuthEvents();
  bindUpiPaymentEvents();
  bindLanguageSelector();
  bindModalToggles();
  bindDebugHudEvents();

  // 2. Handle URL hash navigation if present
  const hash = window.location.hash.replace('#', '');
  if (hash && ['home', 'diagnose', 'assistant', 'weather', 'mandi', 'shop', 'farm'].includes(hash)) {
    switchTab(hash);
  } else {
    switchTab('home');
  }

  // 3. Immediately render initial cart UI & badge
  updateCartUI();

  // 4. Hydrate data in background without blocking user interactions
  loadInitialData().catch(err => {
    console.error("Initialization error:", err);
  });
});

// 1. Initial Data Fetching & Hydration
async function loadInitialData() {
  try {
    const res = await fetch(`/api/init?lang=${state.currentLang}`);
    const data = await res.json();
    if (data.status === 'success') {
      state.translations = data.translations;
      state.crops = data.crops;
      state.stats = data.stats;
      state.weather = data.weather_summary;
      state.activeFarmer = data.active_farmer;
      state.demoFarmers = data.demo_farmers;
      
      // Load saved farmer from localStorage if available
      const savedFarmer = localStorage.getItem('fieldai_farmer');
      if (savedFarmer) {
        try { state.activeFarmer = JSON.parse(savedFarmer); } catch(e) {}
      }

      initWelcomeChat();
      renderLanguageTokens();
      updateAuthHeaderUI();
      populateCropDropdowns();

      // Parallelize child data fetching
      await Promise.allSettled([
        fetchProducts(),
        fetchMandiData(),
        fetchWeatherData(),
        fetchFarmData(),
        fetchFarmerOrders()
      ]);
    }
  } catch (err) {
    console.error("Initialization error:", err);
  }
}

function initWelcomeChat() {
  let welcome = "Sat Sri Akal / Namaste! I am your FIELDAI Assistant. How can I help with your crops, spray timing, or mandi rates today? You can type or use voice in English, ਪੰਜਾਬੀ, or हिन्दी.";
  if (state.currentLang === 'pa') {
    welcome = "ਸਤਿ ਸ਼੍ਰੀ ਅਕਾਲ ਕਿਸਾਨ ਵੀਰ ਜੀ! ਮੈਂ ਤੁਹਾਡਾ FIELDAI ਖੇਤੀ ਸਹਾਇਕ ਹਾਂ। ਤੁਸੀਂ ਆਪਣੀ ਫ਼ਸਲ, ਮੌਸਮ, ਖਾਦ ਜਾਂ ਮੰਡੀ ਭਾਅ ਬਾਰੇ ਪੰਜਾਬੀ ਵਿੱਚ ਬੋਲ ਕੇ ਜਾਂ ਲਿਖ ਕੇ ਪੁੱਛ ਸਕਦੇ ਹੋ।";
  } else if (state.currentLang === 'hi') {
    welcome = "नमस्ते किसान भाई! मैं आपका FIELDAI कृषि सहायक हूँ। अपनी फसल, मौसम, खाद या मंडी भाव के बारे में हिंदी में बोलकर या लिखकर सवाल पूछ सकते हैं।";
  }
  state.chatHistory = [{ sender: 'ai', text: welcome, timestamp: "Just now" }];
  renderChatMessages();
}

// 2. Multilingual Translations Engine (Comprehensive Zero-Omission)
function renderLanguageTokens() {
  // 1. Static HTML elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (state.translations[key]) {
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = state.translations[key];
      } else {
        el.innerText = state.translations[key];
      }
    }
  });

  // 2. Update language selector active label
  const langNames = { en: 'English', pa: 'ਪੰਜਾਬੀ (Punjabi)', hi: 'हिन्दी (Hindi)' };
  const currentLangLabel = document.getElementById('current-lang-label');
  if (currentLangLabel) {
    currentLangLabel.innerText = langNames[state.currentLang] || 'English';
  }

  // 3. Re-render dynamic components in new language
  populateCropDropdowns();
  renderProductsGrid();
  renderMandiTable();
  if (state.activeDiagnosis) {
    renderDiagnosisResult(state.activeDiagnosis);
  }
  if (state.farmData) {
    renderFarmView();
  }
  updateAuthHeaderUI();
}

async function setLanguage(lang) {
  if (state.currentLang === lang) return;
  state.currentLang = lang;
  localStorage.setItem('fieldai_lang', lang);

  try {
    const res = await fetch(`/api/translations?lang=${lang}`);
    const data = await res.json();
    if (data.status === 'success') {
      state.translations = data.translations;
      initWelcomeChat();
      renderLanguageTokens();
      showToast(lang === 'pa' ? "ਭਾਸ਼ਾ ਬਦਲ ਗਈ: ਪੰਜਾਬੀ" : (lang === 'hi' ? "भाषा बदली: हिन्दी" : "Language set: English"));
    }
  } catch (err) {
    console.error("Failed to change language:", err);
  }
}

function bindLanguageSelector() {
  const dropdownBtn = document.getElementById('lang-dropdown-btn');
  const dropdownMenu = document.getElementById('lang-dropdown-menu');
  if (dropdownBtn && dropdownMenu) {
    dropdownBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      dropdownMenu.classList.toggle('hidden');
    });

    document.addEventListener('click', () => {
      dropdownMenu.classList.add('hidden');
    });

    dropdownMenu.querySelectorAll('[data-lang]').forEach(btn => {
      btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        setLanguage(lang);
        dropdownMenu.classList.add('hidden');
      });
    });
  }
}

// 3. Navigation Management (Desktop & Mobile)
function bindNavigation() {
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      switchTab(link.getAttribute('data-tab'));
    });
  });

  document.querySelectorAll('.mobile-nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      switchTab(link.getAttribute('data-tab'));
    });
  });

  document.querySelectorAll('[data-cta-tab]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      switchTab(btn.getAttribute('data-cta-tab'));
    });
  });
}

function switchTab(tabName) {
  state.currentTab = tabName;
  window.location.hash = tabName;

  document.querySelectorAll('.app-section').forEach(sec => sec.classList.add('hidden'));
  const activeSec = document.getElementById(`section-${tabName}`);
  if (activeSec) activeSec.classList.remove('hidden');

  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('data-tab') === tabName) {
      link.classList.add('text-[#133E2B]', 'font-semibold', 'border-b-2', 'border-[#133E2B]');
      link.classList.remove('text-[#575E54]', 'border-transparent');
    } else {
      link.classList.remove('text-[#133E2B]', 'font-semibold', 'border-b-2', 'border-[#133E2B]');
      link.classList.add('text-[#575E54]', 'border-transparent');
    }
  });

  document.querySelectorAll('.mobile-nav-link').forEach(link => {
    const label = link.querySelector('span');
    if (link.getAttribute('data-tab') === tabName) {
      link.classList.add('text-[#133E2B]');
      link.classList.remove('text-[#858D82]');
      if (label) label.classList.add('font-bold');
    } else {
      link.classList.remove('text-[#133E2B]');
      link.classList.add('text-[#858D82]');
      if (label) label.classList.remove('font-bold');
    }
  });

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 4. Crop Doctor & Disease Diagnostics
function populateCropDropdowns() {
  const cropSelect = document.getElementById('diag-crop-select');
  if (!cropSelect) return;

  const currentVal = cropSelect.value;
  cropSelect.innerHTML = '';
  state.crops.forEach(crop => {
    const opt = document.createElement('option');
    opt.value = crop.id;
    let label = crop.name;
    if (state.currentLang === 'pa' && crop.name_pa) label = `${crop.name_pa} (${crop.name})`;
    else if (state.currentLang === 'hi' && crop.name_hi) label = `${crop.name_hi} (${crop.name})`;
    opt.innerText = `${crop.icon} ${label}`;
    cropSelect.appendChild(opt);
  });

  if (currentVal) cropSelect.value = currentVal;
  updateGrowthStages(cropSelect.value);
}

function updateGrowthStages(cropId) {
  const stageSelect = document.getElementById('diag-stage-select');
  if (!stageSelect) return;
  const cropObj = state.crops.find(c => c.id === cropId);
  stageSelect.innerHTML = '';
  if (cropObj) {
    let stages = cropObj.stages;
    if (state.currentLang === 'pa' && cropObj.stages_pa) stages = cropObj.stages_pa;
    else if (state.currentLang === 'hi' && cropObj.stages_hi) stages = cropObj.stages_hi;

    stages.forEach(st => {
      const opt = document.createElement('option');
      opt.value = st;
      opt.innerText = st;
      stageSelect.appendChild(opt);
    });
  }
}

function bindDiagnosisEvents() {
  const cropSelect = document.getElementById('diag-crop-select');
  if (cropSelect) {
    cropSelect.addEventListener('change', (e) => updateGrowthStages(e.target.value));
  }

  // Sample leaf cards
  document.querySelectorAll('.sample-leaf-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const sampleId = chip.getAttribute('data-sample');
      const cropId = chip.getAttribute('data-crop');
      const imgPath = chip.getAttribute('data-img');

      if (cropSelect) cropSelect.value = cropId;
      updateGrowthStages(cropId);

      const previewImg = document.getElementById('diag-preview-image');
      const dropZone = document.getElementById('diag-drop-zone');
      const previewWrapper = document.getElementById('diag-preview-wrapper');

      if (previewImg && dropZone && previewWrapper) {
        previewImg.src = imgPath;
        previewImg.setAttribute('data-sample-id', sampleId);
        dropZone.classList.add('hidden');
        previewWrapper.classList.remove('hidden');
      }

      document.querySelectorAll('.sample-leaf-chip').forEach(c => c.classList.remove('ring-2', 'ring-[#133E2B]'));
      chip.classList.add('ring-2', 'ring-[#133E2B]');
    });
  });

  // Image Upload / Camera
  const fileInput = document.getElementById('diag-file-input');
  const uploadBtn = document.getElementById('diag-upload-btn');
  const cameraBtn = document.getElementById('diag-camera-btn');
  const dropZone = document.getElementById('diag-drop-zone');
  const previewImg = document.getElementById('diag-preview-image');
  const previewWrapper = document.getElementById('diag-preview-wrapper');
  const resetBtn = document.getElementById('diag-reset-image-btn');

  if (uploadBtn && fileInput) uploadBtn.addEventListener('click', () => fileInput.click());
  if (cameraBtn && fileInput) {
    cameraBtn.addEventListener('click', () => {
      fileInput.setAttribute('capture', 'environment');
      fileInput.click();
    });
  }

  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          previewImg.src = event.target.result;
          previewImg.removeAttribute('data-sample-id');
          dropZone.classList.add('hidden');
          previewWrapper.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
      }
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      previewImg.src = '';
      previewImg.removeAttribute('data-sample-id');
      previewWrapper.classList.add('hidden');
      dropZone.classList.remove('hidden');
      if (fileInput) fileInput.value = '';
      const canvas = document.getElementById('diag-bounding-canvas');
      if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    });
  }

  // Run Diagnosis Button
  const analyzeBtn = document.getElementById('diag-run-analyze-btn');
  if (analyzeBtn) {
    analyzeBtn.addEventListener('click', async () => {
      const previewImg = document.getElementById('diag-preview-image');
      if (!previewImg.src || previewImg.src === window.location.href) {
        alert(state.currentLang === 'pa' ? "ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਫ਼ਸਲ ਦੇ ਪੱਤੇ ਦੀ ਫੋਟੋ ਲਵੋ।" : (state.currentLang === 'hi' ? "कृपया पहले फसल की पत्ती की फोटो चुनें।" : "Please upload a leaf photo or pick a sample leaf first."));
        return;
      }

      const cropVal = document.getElementById('diag-crop-select').value;
      const stageVal = document.getElementById('diag-stage-select').value;
      const locationVal = document.getElementById('diag-location-input').value;
      const symptomsVal = document.getElementById('diag-symptoms-input').value;
      const sampleId = previewImg.getAttribute('data-sample-id');

      const scanOverlay = document.getElementById('diag-scanning-overlay');
      const resultsPanel = document.getElementById('diag-results-panel');
      if (scanOverlay) scanOverlay.classList.remove('hidden');
      analyzeBtn.disabled = true;

      try {
        const payload = {
          crop: cropVal,
          growth_stage: stageVal,
          location: locationVal,
          symptoms: symptomsVal,
          sample_id: sampleId || null,
          image_url: previewImg.src.startsWith('data:') ? '' : previewImg.src,
          lang: state.currentLang
        };

        const res = await fetch('/api/diagnose', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const resultData = await res.json();

        setTimeout(() => {
          if (scanOverlay) scanOverlay.classList.add('hidden');
          analyzeBtn.disabled = false;
          if (resultData.status === 'success') {
            state.activeDiagnosis = resultData;
            renderDiagnosisResult(resultData);
            if (resultsPanel) {
              resultsPanel.classList.remove('hidden');
              resultsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
          }
        }, 1200);

      } catch (err) {
        if (scanOverlay) scanOverlay.classList.add('hidden');
        analyzeBtn.disabled = false;
        alert("Diagnosis failed. Check connection.");
      }
    });
  }
}

function renderDiagnosisResult(data) {
  let title = data.disease_name;
  document.getElementById('res-disease-title').innerText = title;
  document.getElementById('res-scientific-name').innerText = data.scientific_name;
  document.getElementById('res-confidence-badge').innerText = `${data.confidence}% ${state.translations['diag_confidence'] || 'Confidence'}`;
  
  const severityEl = document.getElementById('res-severity-badge');
  severityEl.innerText = data.severity;
  severityEl.style.backgroundColor = data.severity_color || '#DC2626';

  const sympList = document.getElementById('res-symptoms-list');
  sympList.innerHTML = '';
  data.symptoms.forEach(s => {
    const li = document.createElement('li');
    li.className = 'flex items-start text-sm text-[#3A3F36]';
    li.innerHTML = `<span class="text-[#133E2B] mr-2 font-bold">•</span> <span>${s}</span>`;
    sympList.appendChild(li);
  });

  const causesList = document.getElementById('res-causes-list');
  causesList.innerHTML = '';
  data.likely_causes.forEach(c => {
    const li = document.createElement('li');
    li.className = 'flex items-start text-sm text-[#3A3F36]';
    li.innerHTML = `<span class="text-[#D97706] mr-2 font-bold">•</span> <span>${c}</span>`;
    causesList.appendChild(li);
  });

  const stepsList = document.getElementById('res-steps-list');
  stepsList.innerHTML = '';
  data.recommended_steps.forEach(st => {
    const li = document.createElement('li');
    li.className = 'flex items-start text-sm text-[#3A3F36] font-medium';
    li.innerHTML = `<span class="text-[#16A34A] mr-2">✓</span> <span>${st}</span>`;
    stepsList.appendChild(li);
  });

  const prevList = document.getElementById('res-prevention-list');
  prevList.innerHTML = '';
  data.prevention_tips.forEach(pt => {
    const li = document.createElement('li');
    li.className = 'flex items-start text-sm text-[#3A3F36]';
    li.innerHTML = `<span class="text-[#133E2B] mr-2">✦</span> <span>${pt}</span>`;
    prevList.appendChild(li);
  });

  renderDiagnosisTreatments(data.recommended_products);
  drawBoundingBoxesOnCanvas(data.bounding_boxes);

  // Quick Action: Ask AI
  const askAiBtn = document.getElementById('res-ask-ai-btn');
  if (askAiBtn) {
    askAiBtn.onclick = () => {
      switchTab('assistant');
      let promptMsg = `I just ran a Crop Doctor scan for my ${data.crop_id}. It detected ${data.disease_name} with ${data.confidence}% confidence. What immediate spray dosages should I follow?`;
      if (state.currentLang === 'pa') {
        promptMsg = `ਮੈਂ ਫ਼ਸਲ ਡਾਕਟਰ ਵਿੱਚ ਜਾਂਚ ਕੀਤੀ ਹੈ, ਜਿਸ ਵਿੱਚ ${title} ਪਾਇਆ ਗਿਆ ਹੈ (${data.confidence}% ਭਰੋਸੇਯੋਗਤਾ)। ਮੈਨੂੰ ਤੁਰੰਤ ਕੀ ਇਲਾਜ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ?`;
      } else if (state.currentLang === 'hi') {
        promptMsg = `मैंने फसल डॉक्टर में जांच की है जिसमें ${title} पाया गया है। मुझे कौन सा कीटनाशक और क्या सावधानी बरतनी चाहिए?`;
      }
      sendUserChatMessage(promptMsg);
    };
  }

  // Quick Action: Save to Farm
  const saveFarmBtn = document.getElementById('res-save-farm-btn');
  if (saveFarmBtn) {
    saveFarmBtn.onclick = async () => {
      try {
        const payload = {
          crop: data.crop_id,
          disease: data.disease_name,
          severity: data.severity,
          confidence: data.confidence,
          treatment_taken: data.recommended_products[0]?.name || "Tilt 25% EC"
        };
        const res = await fetch('/api/farm/save_diagnosis', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        const saved = await res.json();
        if (saved.status === 'success') {
          showToast(state.translations['diag_saved_toast'] || "Diagnosis saved to your farm records!");
          fetchFarmData();
        }
      } catch (err) {
        showToast("Saved to farm log.");
      }
    };
  }

  // Quick Action: Find Treatment
  const findTreatBtn = document.getElementById('res-find-treatment-btn');
  if (findTreatBtn) {
    findTreatBtn.onclick = () => {
      switchTab('shop');
      const categoryName = data.recommended_products[0]?.category || 'Fungicide';
      const filterBtn = document.querySelector(`[data-shop-filter="${categoryName}"]`);
      if (filterBtn) filterBtn.click();
    };
  }
}

function drawBoundingBoxesOnCanvas(boxes) {
  const previewImg = document.getElementById('diag-preview-image');
  const canvas = document.getElementById('diag-bounding-canvas');
  if (!canvas || !previewImg || !boxes) return;

  const renderBoxes = () => {
    const width = previewImg.clientWidth || previewImg.parentElement?.clientWidth || 600;
    const height = previewImg.clientHeight || previewImg.parentElement?.clientHeight || 400;
    canvas.width = width;
    canvas.height = height;

    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    boxes.forEach((box) => {
      const x = (box.x / 100) * canvas.width;
      const y = (box.y / 100) * canvas.height;
      const w = (box.w / 100) * canvas.width;
      const h = (box.h / 100) * canvas.height;

      ctx.lineWidth = 3;
      ctx.strokeStyle = '#DC2626';
      ctx.strokeRect(x, y, w, h);

      ctx.fillStyle = 'rgba(220, 38, 38, 0.16)';
      ctx.fillRect(x, y, w, h);

      ctx.fillStyle = '#DC2626';
      const tagText = `${box.label} (${Math.round(box.confidence * 100)}%)`;
      ctx.font = '600 12px "Plus Jakarta Sans", sans-serif';
      const textWidth = ctx.measureText(tagText).width;
      const labelY = Math.max(22, y);
      ctx.fillRect(x, labelY - 22, textWidth + 14, 22);

      ctx.fillStyle = '#FFFFFF';
      ctx.fillText(tagText, x + 7, labelY - 6);
    });
  };

  if (previewImg.complete && previewImg.clientWidth > 0) {
    renderBoxes();
  } else {
    previewImg.onload = renderBoxes;
    setTimeout(renderBoxes, 150);
  }
}

function renderDiagnosisTreatments(products) {
  const container = document.getElementById('res-treatments-container');
  if (!container) return;
  container.innerHTML = '';

  products.forEach(p => {
    let prodName = p.name;
    let prodCat = p.category;
    let dosage = p.dosage;
    if (state.currentLang === 'pa') {
      if (p.name_pa) prodName = p.name_pa;
      if (p.category_pa) prodCat = p.category_pa;
      if (p.dosage_pa) dosage = p.dosage_pa;
    } else if (state.currentLang === 'hi') {
      if (p.name_hi) prodName = p.name_hi;
      if (p.category_hi) prodCat = p.category_hi;
      if (p.dosage_hi) dosage = p.dosage_hi;
    }

    const card = document.createElement('div');
    card.className = 'farm-card p-4 flex flex-col justify-between';
    card.innerHTML = `
      <div>
        <div class="flex items-center space-x-3 mb-3">
          <img src="${p.image}" alt="${prodName}" onerror="this.onerror=null; this.src='/static/img/products/tilt.png';" class="w-16 h-16 object-contain rounded-lg bg-[#FAF9F5] p-1 border border-[#E8E5DC] drop-shadow-sm">
          <div>
            <span class="inline-block text-[11px] font-semibold text-[#16A34A] bg-[#E8F5E9] px-2 py-0.5 rounded">${prodCat}</span>
            <h4 class="font-bold text-[#1C1E1B] text-sm leading-tight mt-1 hover:text-[#133E2B] cursor-pointer" onclick="openProductModal('${p.id}')">${prodName}</h4>
            <p class="text-[12px] text-[#575E54]">${p.brand}</p>
          </div>
        </div>
        <p class="text-xs text-[#575E54] mb-2"><strong class="text-[#1C1E1B]">${state.translations['shop_active_ing'] || 'Formula:'}</strong> ${p.active_ingredient}</p>
        <p class="text-xs text-[#575E54] mb-3"><strong class="text-[#1C1E1B]">${state.translations['shop_safety_dosage'] || 'Dosage:'}</strong> ${dosage}</p>
      </div>
      <div class="pt-3 border-t border-[#F0ECE1] flex items-center justify-between">
        <div>
          <span class="text-base font-bold text-[#133E2B]">₹${p.price}</span>
          <span class="text-xs text-[#858D82] line-through ml-1">₹${p.mrp}</span>
        </div>
        <div class="flex space-x-1.5">
          <button onclick="openProductModal('${p.id}')" class="px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-[#F2EFE9] text-[#1C1E1B] hover:bg-[#E5E0D5] transition">${state.translations['shop_btn_details'] || 'Safety'}</button>
          <button onclick="addToCart('${p.id}')" class="px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-[#133E2B] text-white hover:bg-[#1A523A] transition">${state.translations['shop_btn_add_cart'] || 'Add'}</button>
          <button onclick="quickBuyNow('${p.id}')" class="px-2.5 py-1.5 text-xs font-bold rounded-lg bg-[#16A34A] text-white hover:bg-[#15803D] transition shadow-sm flex items-center space-x-1">
            <span>⚡</span>
            <span>Buy</span>
          </button>
        </div>
      </div>
    `;
    container.appendChild(card);
  });
}

// 5. Treatment Products & Farm Inputs Marketplace
async function fetchProducts() {
  try {
    const res = await fetch(`/api/products?category=${state.activeFilter}`);
    const data = await res.json();
    if (data.status === 'success') {
      state.products = data.data;
      renderProductsGrid();
    }
  } catch (err) {
    console.error("Products fetch error:", err);
  }
}

function renderProductsGrid() {
  const grid = document.getElementById('shop-products-grid');
  if (!grid) return;
  grid.innerHTML = '';

  state.products.forEach(p => {
    let prodName = p.name;
    let prodCat = p.category;
    if (state.currentLang === 'pa') {
      if (p.name_pa) prodName = p.name_pa;
      if (p.category_pa) prodCat = p.category_pa;
    } else if (state.currentLang === 'hi') {
      if (p.name_hi) prodName = p.name_hi;
      if (p.category_hi) prodCat = p.category_hi;
    }

    const card = document.createElement('div');
    card.className = 'farm-card p-5 flex flex-col justify-between group';
    card.innerHTML = `
      <div>
        <div class="relative w-full h-48 bg-[#F8F7F2] rounded-xl flex items-center justify-center p-3 mb-4 overflow-hidden border border-[#EDE8DC]">
          <img src="${p.image}" alt="${prodName}" onerror="this.onerror=null; this.src='/static/img/products/tilt.png';" class="h-40 w-auto object-contain hover:scale-105 transition-transform duration-300 drop-shadow-md">
          <span class="absolute top-2.5 left-2.5 text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-white/95 shadow-sm text-[#133E2B] border border-[#E4E0D5]">${prodCat}</span>
          <span class="absolute bottom-2.5 right-2.5 text-[11px] font-semibold text-[#575E54] bg-white/95 px-2 py-0.5 rounded shadow-sm">${p.pack_size}</span>
        </div>
        
        <div class="flex items-center space-x-1.5 mb-1 text-xs">
          <span class="text-[#D97706] font-bold">★ ${p.rating}</span>
          <span class="text-[#858D82]">(${p.reviews_count} reviews)</span>
        </div>

        <h3 class="font-bold text-[#1C1E1B] text-base leading-snug mb-1 hover:text-[#133E2B] cursor-pointer" onclick="openProductModal('${p.id}')">${prodName}</h3>
        <p class="text-xs text-[#575E54] mb-2 font-medium">${p.brand}</p>
        
        <div class="bg-[#F8F7F2] p-2.5 rounded-lg border border-[#EDE8DC] mb-3 text-xs">
          <p class="text-[#3A3F36]"><strong class="text-[#1C1E1B]">${state.translations['shop_active_ing'] || 'Active:'}</strong> ${p.active_ingredient}</p>
          <p class="text-[#575E54] mt-1"><strong class="text-[#1C1E1B]">${state.translations['shop_target'] || 'Targets:'}</strong> ${p.target_diseases.slice(0, 2).join(', ')}</p>
        </div>

        <div class="flex items-center space-x-2 text-[11px] text-[#575E54] mb-4">
          <svg class="w-3.5 h-3.5 text-[#16A34A]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          <span>${state.translations['shop_delivery'] || 'Est. Delivery:'} ${p.delivery_est}</span>
        </div>
      </div>

      <div class="pt-3 border-t border-[#F0ECE1]">
        <div class="flex items-baseline justify-between mb-3">
          <div>
            <span class="text-xl font-bold text-[#133E2B]">₹${p.price}</span>
            <span class="text-xs text-[#858D82] line-through ml-1.5">₹${p.mrp}</span>
          </div>
          <span class="text-[11px] font-bold text-[#16A34A] bg-[#DCFCE7] px-2 py-0.5 rounded">Save ${Math.round(((p.mrp - p.price) / p.mrp) * 100)}%</span>
        </div>
        
        <div class="grid grid-cols-2 gap-2 mb-2">
          <button onclick="openProductModal('${p.id}')" class="w-full py-2 px-2 text-xs font-semibold rounded-xl bg-[#F2EFE9] text-[#1C1E1B] hover:bg-[#E4E0D5] transition flex items-center justify-center">
            ${state.translations['shop_btn_details'] || 'Details & Safety'}
          </button>
          <button onclick="addToCart('${p.id}')" class="w-full py-2 px-2 text-xs font-semibold rounded-xl bg-[#133E2B] text-white hover:bg-[#1A523A] transition shadow-sm flex items-center justify-center">
            + ${state.translations['shop_btn_add_cart'] || 'Add to Cart'}
          </button>
        </div>
        <button onclick="quickBuyNow('${p.id}')" class="w-full py-2 px-3 text-xs font-bold rounded-xl bg-[#16A34A] text-white hover:bg-[#15803D] transition shadow-sm flex items-center justify-center space-x-1.5">
          <span>⚡</span>
          <span>Buy Now (Instant UPI/KCC)</span>
        </button>
      </div>
    `;
    grid.appendChild(card);
  });
}

function bindShopEvents() {
  document.querySelectorAll('[data-shop-filter]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('[data-shop-filter]').forEach(b => {
        b.classList.remove('bg-[#133E2B]', 'text-white');
        b.classList.add('bg-white', 'text-[#575E54]');
      });
      btn.classList.add('bg-[#133E2B]', 'text-white');
      btn.classList.remove('bg-white', 'text-[#575E54]');

      state.activeFilter = btn.getAttribute('data-shop-filter');
      fetchProducts();
    });
  });

  const searchInput = document.getElementById('shop-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase();
      const filtered = state.products.filter(p => 
        p.name.toLowerCase().includes(q) ||
        p.active_ingredient.toLowerCase().includes(q) ||
        p.brand.toLowerCase().includes(q)
      );
      // Re-render filtered
      const grid = document.getElementById('shop-products-grid');
      if (grid) {
        grid.innerHTML = '';
        filtered.forEach(p => {
          // reuse render
          renderSingleProduct(grid, p);
        });
      }
    });
  }
}

function renderSingleProduct(grid, p) {
  let prodName = p.name;
  let prodCat = p.category;
  if (state.currentLang === 'pa') {
    if (p.name_pa) prodName = p.name_pa;
    if (p.category_pa) prodCat = p.category_pa;
  } else if (state.currentLang === 'hi') {
    if (p.name_hi) prodName = p.name_hi;
    if (p.category_hi) prodCat = p.category_hi;
  }

  const card = document.createElement('div');
  card.className = 'farm-card p-5 flex flex-col justify-between group';
  card.innerHTML = `
    <div>
      <div class="relative w-full h-48 bg-[#F8F7F2] rounded-xl flex items-center justify-center p-3 mb-4 overflow-hidden border border-[#EDE8DC]">
        <img src="${p.image}" alt="${prodName}" onerror="this.onerror=null; this.src='/static/img/products/tilt.png';" class="h-40 w-auto object-contain hover:scale-105 transition-transform duration-300 drop-shadow-md">
        <span class="absolute top-2.5 left-2.5 text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-white/95 shadow-sm text-[#133E2B] border border-[#E4E0D5]">${prodCat}</span>
        <span class="absolute bottom-2.5 right-2.5 text-[11px] font-semibold text-[#575E54] bg-white/95 px-2 py-0.5 rounded shadow-sm">${p.pack_size || '1 L'}</span>
      </div>
      
      <div class="flex items-center space-x-1.5 mb-1 text-xs">
        <span class="text-[#D97706] font-bold">★ ${p.rating || '4.8'}</span>
        <span class="text-[#858D82]">(${p.reviews_count || 120} reviews)</span>
      </div>

      <h3 class="font-bold text-[#1C1E1B] text-base leading-snug mb-1 hover:text-[#133E2B] cursor-pointer" onclick="openProductModal('${p.id}')">${prodName}</h3>
      <p class="text-xs text-[#575E54] mb-2 font-medium">${p.brand}</p>
      
      <div class="bg-[#F8F7F2] p-2.5 rounded-lg border border-[#EDE8DC] mb-3 text-xs">
        <p class="text-[#3A3F36]"><strong class="text-[#1C1E1B]">${state.translations['shop_active_ing'] || 'Active:'}</strong> ${p.active_ingredient}</p>
        <p class="text-[#575E54] mt-1"><strong class="text-[#1C1E1B]">${state.translations['shop_target'] || 'Targets:'}</strong> ${(p.target_diseases || []).slice(0, 2).join(', ')}</p>
      </div>

      <div class="flex items-center space-x-2 text-[11px] text-[#575E54] mb-4">
        <svg class="w-3.5 h-3.5 text-[#16A34A]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
        <span>${state.translations['shop_delivery'] || 'Est. Delivery:'} ${p.delivery_est || '1-2 Days'}</span>
      </div>
    </div>

    <div class="pt-3 border-t border-[#F0ECE1]">
      <div class="flex items-baseline justify-between mb-3">
        <div>
          <span class="text-xl font-bold text-[#133E2B]">₹${p.price}</span>
          <span class="text-xs text-[#858D82] line-through ml-1.5">₹${p.mrp}</span>
        </div>
        <span class="text-[11px] font-bold text-[#16A34A] bg-[#DCFCE7] px-2 py-0.5 rounded">Save ${Math.round(((p.mrp - p.price) / p.mrp) * 100)}%</span>
      </div>
      
      <div class="grid grid-cols-2 gap-2 mb-2">
        <button onclick="openProductModal('${p.id}')" class="w-full py-2 px-2 text-xs font-semibold rounded-xl bg-[#F2EFE9] text-[#1C1E1B] hover:bg-[#E4E0D5] transition flex items-center justify-center">
          ${state.translations['shop_btn_details'] || 'Details & Safety'}
        </button>
        <button onclick="addToCart('${p.id}')" class="w-full py-2 px-2 text-xs font-semibold rounded-xl bg-[#133E2B] text-white hover:bg-[#1A523A] transition shadow-sm flex items-center justify-center">
          + ${state.translations['shop_btn_add_cart'] || 'Add to Cart'}
        </button>
      </div>
      <button onclick="quickBuyNow('${p.id}')" class="w-full py-2 px-3 text-xs font-bold rounded-xl bg-[#16A34A] text-white hover:bg-[#15803D] transition shadow-sm flex items-center justify-center space-x-1.5">
        <span>⚡</span>
        <span>Buy Now (Instant UPI/KCC)</span>
      </button>
    </div>
  `;
  grid.appendChild(card);
}

async function openProductModal(prodId) {
  if (!state.products || state.products.length === 0) {
    await fetchProducts();
  }
  const p = (state.products || []).find(item => item.id === prodId) || 
            state.activeDiagnosis?.recommended_products?.find(item => item.id === prodId);
  if (!p) {
    console.warn("Product not found:", prodId);
    return;
  }

  const modal = document.getElementById('product-details-modal');
  if (!modal) return;

  let prodName = p.name;
  let dosage = p.dosage || 'Follow label instructions';
  if (state.currentLang === 'pa') {
    if (p.name_pa) prodName = p.name_pa;
    if (p.dosage_pa) dosage = p.dosage_pa;
  } else if (state.currentLang === 'hi') {
    if (p.name_hi) prodName = p.name_hi;
    if (p.dosage_hi) dosage = p.dosage_hi;
  }

  const modalImg = document.getElementById('modal-prod-img');
  if (modalImg) {
    modalImg.src = p.image || '/static/img/products/tilt.png';
    modalImg.onerror = () => { modalImg.src = '/static/img/products/tilt.png'; };
  }

  const titleEl = document.getElementById('modal-prod-title');
  if (titleEl) titleEl.innerText = prodName;

  const brandEl = document.getElementById('modal-prod-brand');
  if (brandEl) brandEl.innerText = `${p.brand || 'Verified Agri-Brand'} • CIBRC Reg: ${p.cibrc_reg || 'CIR-Reg-2026'}`;

  const activeEl = document.getElementById('modal-prod-active');
  if (activeEl) activeEl.innerText = p.active_ingredient || 'Standard Active Formulation';

  const dosageEl = document.getElementById('modal-prod-dosage');
  if (dosageEl) dosageEl.innerText = dosage;

  const phiEl = document.getElementById('modal-prod-phi');
  if (phiEl) phiEl.innerText = `${p.phi_days != null ? p.phi_days : 14} Days Pre-Harvest Interval (PHI)`;

  const cropsEl = document.getElementById('modal-prod-crops');
  if (cropsEl) cropsEl.innerText = Array.isArray(p.suitable_crops) ? p.suitable_crops.join(', ') : 'All Major Indian Crops';

  const targetsEl = document.getElementById('modal-prod-targets');
  if (targetsEl) targetsEl.innerText = Array.isArray(p.target_diseases) ? p.target_diseases.join(', ') : 'Broad Spectrum Crop Diseases';

  const sellerEl = document.getElementById('modal-prod-seller');
  if (sellerEl) sellerEl.innerText = p.seller || 'Authorized IFFCO / PAU Kisan Kendra';

  const priceEl = document.getElementById('modal-prod-price');
  if (priceEl) priceEl.innerText = `₹${p.price || 0}`;

  const mrpEl = document.getElementById('modal-prod-mrp');
  if (mrpEl) mrpEl.innerText = `₹${p.mrp || 0}`;

  const noticeEl = document.getElementById('modal-prod-notice');
  if (noticeEl) noticeEl.innerText = p.regulatory_notice || 'Use agricultural chemicals only according to the approved product label and local agricultural guidance.';

  const ppeContainer = document.getElementById('modal-prod-ppe-list');
  if (ppeContainer) {
    ppeContainer.innerHTML = '';
    const ppeList = Array.isArray(p.safety_ppe) && p.safety_ppe.length > 0 ? p.safety_ppe : ['Chemical Mask', 'Nitrile Gloves', 'Long Sleeves'];
    ppeList.forEach(ppe => {
      const span = document.createElement('span');
      span.className = 'inline-flex items-center text-xs px-2.5 py-1 rounded-full bg-[#FEF3C7] text-[#92400E] border border-[#FDE68A] font-medium';
      span.innerHTML = `🛡️ ${ppe}`;
      ppeContainer.appendChild(span);
    });
  }

  const modalAddBtn = document.getElementById('modal-add-cart-btn');
  if (modalAddBtn) {
    modalAddBtn.onclick = () => {
      addToCart(p.id);
      modal.classList.add('hidden');
    };
  }

  const modalBuyNowBtn = document.getElementById('modal-buy-now-btn');
  if (modalBuyNowBtn) {
    modalBuyNowBtn.onclick = () => {
      modal.classList.add('hidden');
      quickBuyNow(p.id);
    };
  }

  modal.classList.remove('hidden');
}
window.openProductModal = openProductModal;

// 6. AI Assistant Chat & Voice
function bindChatEvents() {
  const chatInput = document.getElementById('ai-chat-input');
  const sendBtn = document.getElementById('ai-chat-send-btn');
  const micBtn = document.getElementById('ai-chat-mic-btn');

  if (sendBtn && chatInput) {
    sendBtn.addEventListener('click', () => {
      const text = chatInput.value.trim();
      if (text) {
        sendUserChatMessage(text);
        chatInput.value = '';
      }
    });

    chatInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        const text = chatInput.value.trim();
        if (text) {
          sendUserChatMessage(text);
          chatInput.value = '';
        }
      }
    });
  }

  document.querySelectorAll('.ai-suggested-chip').forEach(chip => {
    chip.addEventListener('click', () => sendUserChatMessage(chip.innerText.trim()));
  });

  if (micBtn) {
    micBtn.addEventListener('click', () => toggleVoiceRecognition());
  }
}

function setupSpeechRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    state.speechRecognizer = new SpeechRecognition();
    state.speechRecognizer.continuous = false;
    state.speechRecognizer.interimResults = false;

    state.speechRecognizer.onstart = () => {
      state.isListening = true;
      const micBtn = document.getElementById('ai-chat-mic-btn');
      if (micBtn) micBtn.classList.add('bg-red-500', 'text-white', 'animate-pulse');
      showToast(state.translations['ai_voice_listening'] || "Listening... speak now");
    };

    state.speechRecognizer.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      const chatInput = document.getElementById('ai-chat-input');
      if (chatInput) chatInput.value = transcript;
      sendUserChatMessage(transcript);
    };

    state.speechRecognizer.onerror = () => stopVoiceRecognition();
    state.speechRecognizer.onend = () => stopVoiceRecognition();
  }
}

function toggleVoiceRecognition() {
  if (!state.speechRecognizer) {
    alert("Speech recognition is not supported in this browser. Please use Chrome/Edge on desktop or Android.");
    return;
  }
  if (state.isListening) {
    state.speechRecognizer.stop();
  } else {
    let langCode = 'en-IN';
    if (state.currentLang === 'pa') langCode = 'pa-IN';
    else if (state.currentLang === 'hi') langCode = 'hi-IN';
    state.speechRecognizer.lang = langCode;
    try { state.speechRecognizer.start(); } catch (e) {}
  }
}

function stopVoiceRecognition() {
  state.isListening = false;
  const micBtn = document.getElementById('ai-chat-mic-btn');
  if (micBtn) micBtn.classList.remove('bg-red-500', 'text-white', 'animate-pulse');
}

async function sendUserChatMessage(message) {
  const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  state.chatHistory.push({ sender: 'user', text: message, timestamp: now });
  renderChatMessages();

  const typingIndicator = document.getElementById('ai-typing-indicator');
  if (typingIndicator) typingIndicator.classList.remove('hidden');

  try {
    const payload = {
      message: message,
      language: state.currentLang,
      context: {
        crop: state.activeDiagnosis?.crop_id || 'Wheat',
        disease: state.activeDiagnosis?.disease_name || 'None',
        location: state.weather?.location || 'Ludhiana, Punjab'
      }
    };

    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const replyData = await res.json();
    if (typingIndicator) typingIndicator.classList.add('hidden');

    if (replyData.status === 'success') {
      state.chatHistory.push({
        sender: 'ai',
        text: replyData.reply,
        timestamp: replyData.timestamp || now,
        suggestedActions: replyData.suggested_actions
      });
      renderChatMessages();
    }
  } catch (err) {
    if (typingIndicator) typingIndicator.classList.add('hidden');
    state.chatHistory.push({
      sender: 'ai',
      text: "Unable to reach server. Please check internet connection.",
      timestamp: now
    });
    renderChatMessages();
  }
}

function renderChatMessages() {
  const container = document.getElementById('ai-chat-history');
  if (!container) return;
  container.innerHTML = '';

  state.chatHistory.forEach((msg) => {
    const wrapper = document.createElement('div');
    wrapper.className = `flex flex-col ${msg.sender === 'user' ? 'items-end' : 'items-start'} mb-4`;

    const bubble = document.createElement('div');
    bubble.className = `max-w-[85%] md:max-w-[75%] p-4 text-sm leading-relaxed ${
      msg.sender === 'user' ? 'chat-bubble-farmer' : 'chat-bubble-ai'
    }`;

    let formattedText = msg.text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n\n/g, '<br><br>')
      .replace(/\n/g, '<br>');

    bubble.innerHTML = formattedText;

    if (msg.sender === 'ai') {
      const actionsBar = document.createElement('div');
      actionsBar.className = 'flex items-center justify-between mt-3 pt-2 border-t border-[#F0ECE1] text-[11px] text-[#858D82]';
      actionsBar.innerHTML = `
        <span>FIELDAI Agronomist • ${msg.timestamp}</span>
        <button onclick="speakText('${encodeURIComponent(msg.text)}')" class="hover:text-[#133E2B] flex items-center space-x-1 p-1 rounded" title="Listen Audio">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>
          <span>Listen</span>
        </button>
      `;
      bubble.appendChild(actionsBar);
    } else {
      const timeTag = document.createElement('span');
      timeTag.className = 'text-[10px] text-white/70 mt-1 self-end';
      timeTag.innerText = msg.timestamp;
      bubble.appendChild(timeTag);
    }

    wrapper.appendChild(bubble);

    if (msg.suggestedActions && msg.suggestedActions.length > 0) {
      const pillRow = document.createElement('div');
      pillRow.className = 'flex flex-wrap gap-2 mt-2';
      msg.suggestedActions.forEach(actionText => {
        const btn = document.createElement('button');
        btn.className = 'text-xs px-3 py-1 rounded-full bg-white border border-[#D5D0C2] text-[#133E2B] font-medium hover:bg-[#F2EFE9] transition';
        btn.innerText = actionText;
        btn.onclick = () => {
          if (actionText.includes('ਡਾਕਟਰ') || actionText.includes('Doctor') || actionText.includes('स्कैन')) switchTab('diagnose');
          else if (actionText.includes('ਮੰਡੀ') || actionText.includes('Mandi')) switchTab('mandi');
          else if (actionText.includes('ਮੌਸਮ') || actionText.includes('Weather')) switchTab('weather');
          else sendUserChatMessage(actionText);
        };
        pillRow.appendChild(btn);
      });
      wrapper.appendChild(pillRow);
    }

    container.appendChild(wrapper);
  });

  container.scrollTop = container.scrollHeight;
}

function speakText(encodedStr) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const text = decodeURIComponent(encodedStr).replace(/[*_#]/g, '');
  const utterance = new SpeechSynthesisUtterance(text);

  if (state.currentLang === 'hi') utterance.lang = 'hi-IN';
  else if (state.currentLang === 'pa') utterance.lang = 'pa-IN';
  else utterance.lang = 'en-IN';

  utterance.rate = 0.95;
  window.speechSynthesis.speak(utterance);
}

// 7. Live Mandi APMC Prices
async function fetchMandiData() {
  try {
    const res = await fetch(`/api/mandi?state=${state.mandiFilter.state}&q=${encodeURIComponent(state.mandiFilter.q)}`);
    const data = await res.json();
    if (data.status === 'success') {
      state.mandiList = data.data;
      renderMandiTable();
      renderFeaturedMandiHero();
    }
  } catch (err) {
    console.error("Mandi fetch error:", err);
  }
}

function renderMandiTable() {
  const tbody = document.getElementById('mandi-table-body');
  if (!tbody) return;
  tbody.innerHTML = '';

  state.mandiList.forEach(m => {
    const tr = document.createElement('tr');
    tr.className = 'border-b border-[#F0ECE1] hover:bg-[#FAF9F5] transition text-sm';

    let commName = m.commodity;
    let mspStatus = m.msp_status;
    if (state.currentLang === 'pa') {
      if (m.commodity_pa) commName = `${m.commodity_pa} (${m.commodity})`;
      if (m.msp_status_pa) mspStatus = m.msp_status_pa;
    } else if (state.currentLang === 'hi') {
      if (m.commodity_hi) commName = `${m.commodity_hi} (${m.commodity})`;
      if (m.msp_status_hi) mspStatus = m.msp_status_hi;
    }

    const changePositive = m.change >= 0;

    tr.innerHTML = `
      <td class="py-3.5 px-4 font-semibold text-[#1C1E1B]">
        <div>${m.mandi}</div>
        <div class="text-[11px] text-[#858D82] font-normal">${m.district}, ${m.state}</div>
      </td>
      <td class="py-3.5 px-4 text-[#3A3F36] font-medium">${commName}</td>
      <td class="py-3.5 px-4 text-base font-bold text-[#133E2B]">₹${m.modal_price.toLocaleString()} <span class="text-xs font-normal text-[#858D82]">/ Qtl</span></td>
      <td class="py-3.5 px-4 text-xs text-[#575E54]">₹${m.min_price} – ₹${m.max_price}</td>
      <td class="py-3.5 px-4">
        <span class="inline-flex items-center text-xs font-bold px-2 py-0.5 rounded ${changePositive ? 'text-[#16A34A] bg-[#DCFCE7]' : 'text-[#DC2626] bg-[#FEE2E2]'}">
          ${changePositive ? '+' : ''}₹${m.change}
        </span>
      </td>
      <td class="py-3.5 px-4">
        <span class="inline-block text-[11px] font-semibold text-[#133E2B] bg-[#E8EFEA] px-2 py-0.5 rounded border border-[#D1DFD6]">
          ${mspStatus}
        </span>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function renderFeaturedMandiHero() {
  const container = document.getElementById('hero-mandi-cards');
  if (!container) return;
  container.innerHTML = '';

  state.mandiList.slice(0, 3).forEach(m => {
    let commName = m.commodity;
    if (state.currentLang === 'pa' && m.commodity_pa) commName = m.commodity_pa;
    else if (state.currentLang === 'hi' && m.commodity_hi) commName = m.commodity_hi;

    const card = document.createElement('div');
    card.className = 'bg-white/90 p-3.5 rounded-xl border border-[#E8E5DC] shadow-sm flex items-center justify-between';
    card.innerHTML = `
      <div>
        <div class="text-xs text-[#858D82] font-medium">${m.mandi} (${m.state})</div>
        <div class="text-sm font-bold text-[#1C1E1B]">${commName}</div>
      </div>
      <div class="text-right">
        <div class="text-base font-bold text-[#133E2B]">₹${m.modal_price}</div>
        <div class="text-[11px] font-semibold ${m.change >= 0 ? 'text-[#16A34A]' : 'text-[#DC2626]'}">${m.change >= 0 ? '+' : ''}₹${m.change}</div>
      </div>
    `;
    container.appendChild(card);
  });
}

function bindMandiEvents() {
  const searchInput = document.getElementById('mandi-search-input');
  const stateSelect = document.getElementById('mandi-state-select');

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.mandiFilter.q = e.target.value;
      fetchMandiData();
    });
  }
  if (stateSelect) {
    stateSelect.addEventListener('change', (e) => {
      state.mandiFilter.state = e.target.value;
      fetchMandiData();
    });
  }
}

// 8. Smart Weather & Foliar Spray Advisory
async function fetchWeatherData(loc = 'Ludhiana') {
  try {
    const res = await fetch(`/api/weather?location=${encodeURIComponent(loc)}`);
    const data = await res.json();
    if (data.status === 'success') renderWeatherView(data.data);
  } catch (err) {
    console.error("Weather fetch error:", err);
  }
}

function renderWeatherView(w) {
  const locEl = document.getElementById('weather-location-title');
  if (locEl) locEl.innerText = w.location;

  document.getElementById('weather-temp-main').innerText = `${w.temperature}°C`;
  
  let cond = w.condition;
  let sprayStatus = w.spray_suitability.status;
  let sprayAdvisory = w.spray_suitability.advisory;
  let irrigAdvice = w.irrigation_advice;

  if (state.currentLang === 'pa') {
    if (w.condition_pa) cond = w.condition_pa;
    if (w.spray_suitability.status_pa) sprayStatus = w.spray_suitability.status_pa;
    if (w.spray_suitability.advisory_pa) sprayAdvisory = w.spray_suitability.advisory_pa;
    if (w.irrigation_advice_pa) irrigAdvice = w.irrigation_advice_pa;
  } else if (state.currentLang === 'hi') {
    if (w.condition_hi) cond = w.condition_hi;
    if (w.spray_suitability.status_hi) sprayStatus = w.spray_suitability.status_hi;
    if (w.spray_suitability.advisory_hi) sprayAdvisory = w.spray_suitability.advisory_hi;
    if (w.irrigation_advice_hi) irrigAdvice = w.irrigation_advice_hi;
  }

  document.getElementById('weather-cond-main').innerText = cond;
  document.getElementById('weather-humidity-main').innerText = `${w.humidity}%`;
  document.getElementById('weather-wind-main').innerText = `${w.wind_speed} km/h ${w.wind_direction}`;
  document.getElementById('weather-rain-main').innerText = `${w.rain_chance}%`;

  document.getElementById('weather-spray-score').innerText = `${w.spray_suitability.score}%`;
  document.getElementById('weather-spray-status').innerText = sprayStatus;
  document.getElementById('weather-spray-advisory').innerText = sprayAdvisory;
  document.getElementById('weather-irrigation-text').innerText = irrigAdvice;

  // 7-day forecast cards
  const forecastRow = document.getElementById('weather-forecast-row');
  if (forecastRow && w.forecast) {
    forecastRow.innerHTML = '';
    w.forecast.forEach(f => {
      let dayName = f.day;
      if (state.currentLang === 'pa' && f.day_pa) dayName = f.day_pa;
      else if (state.currentLang === 'hi' && f.day_hi) dayName = f.day_hi;

      const col = document.createElement('div');
      col.className = 'farm-card p-4 text-center flex flex-col justify-between';
      col.innerHTML = `
        <div class="text-xs font-bold text-[#1C1E1B]">${dayName}</div>
        <div class="text-[11px] text-[#858D82]">${f.date}</div>
        <div class="text-2xl my-2">${f.icon}</div>
        <div class="text-sm font-bold text-[#133E2B]">${f.temp_max}° <span class="text-xs text-[#858D82] font-normal">${f.temp_min}°</span></div>
        <div class="text-[11px] text-[#2563EB] font-medium mt-1">💧 ${f.rain_pct}%</div>
      `;
      forecastRow.appendChild(col);
    });
  }

  // Active Alerts
  const alertsContainer = document.getElementById('weather-alerts-container');
  if (alertsContainer && w.agri_alerts) {
    alertsContainer.innerHTML = '';
    w.agri_alerts.forEach(al => {
      let alTitle = al.title;
      let alMsg = al.message;
      if (state.currentLang === 'pa') {
        if (al.title_pa) alTitle = al.title_pa;
        if (al.message_pa) alMsg = al.message_pa;
      } else if (state.currentLang === 'hi') {
        if (al.title_hi) alTitle = al.title_hi;
        if (al.message_hi) alMsg = al.message_hi;
      }

      const div = document.createElement('div');
      const isAmber = al.severity === 'Amber';
      div.className = `p-4 rounded-xl border flex items-start space-x-3 ${
        isAmber ? 'bg-[#FFFBEB] border-[#FDE68A] text-[#92400E]' : 'bg-[#FEF2F2] border-[#FECACA] text-[#991B1B]'
      }`;
      div.innerHTML = `
        <span class="text-xl">${isAmber ? '⚠️' : '🚨'}</span>
        <div>
          <h4 class="font-bold text-sm mb-1">${alTitle}</h4>
          <p class="text-xs leading-relaxed">${alMsg}</p>
        </div>
      `;
      alertsContainer.appendChild(div);
    });
  }
}

function bindWeatherEvents() {
  const locSelect = document.getElementById('weather-location-select');
  if (locSelect) {
    locSelect.addEventListener('change', (e) => fetchWeatherData(e.target.value));
  }
}

// 9. My Farm Management & Diagnostic Logs
async function fetchFarmData() {
  try {
    const res = await fetch('/api/farm');
    const data = await res.json();
    if (data.status === 'success') {
      state.farmData = data.data;
      renderFarmView();
    }
  } catch (err) {
    console.error("Farm fetch error:", err);
  }
}

function renderFarmView() {
  if (!state.farmData) return;
  const d = state.farmData;

  const farmerName = state.activeFarmer?.name || d.farmer_name;
  const village = state.activeFarmer?.village || d.village;
  const district = state.activeFarmer?.district || d.district;
  const st = state.activeFarmer?.state || d.state;
  const acres = state.activeFarmer?.total_acres || d.total_acres;
  const kisanId = state.activeFarmer?.kisan_id || d.kisan_id || 'PB-LU-2026-8812';
  const tubewells = state.activeFarmer?.tubewells || d.tubewells || 2;
  const shcId = state.activeFarmer?.shc_id || d.shc_id || 'PAU-SHC-9042';

  const nameEl = document.getElementById('farm-header-name');
  if (nameEl) nameEl.innerText = farmerName;

  const metaEl = document.getElementById('farm-header-meta');
  if (metaEl) metaEl.innerText = `${village}, ${district}, ${st} • Total Land: ${acres} Acres`;

  const kisanEl = document.getElementById('farm-kisan-id');
  if (kisanEl) kisanEl.innerText = kisanId;

  const holdingEl = document.getElementById('farm-holding-acres');
  if (holdingEl) holdingEl.innerText = `${acres} Acres`;

  const tubeEl = document.getElementById('farm-tubewells-count');
  if (tubeEl) tubeEl.innerText = `${tubewells} Submersible`;

  const shcEl = document.getElementById('farm-shc-badge-id');
  if (shcEl) shcEl.innerText = `${shcId} ✓`;

  const parcelsGrid = document.getElementById('farm-parcels-grid');
  if (parcelsGrid) {
    parcelsGrid.innerHTML = '';
    const plots = d.plots || [];
    plots.forEach(p => {
      let plotName = p.name;
      let cropName = p.crop;
      let statusName = p.status;
      if (state.currentLang === 'pa') {
        if (p.name_pa) plotName = p.name_pa;
        if (p.crop_pa) cropName = p.crop_pa;
        if (p.status_pa) statusName = p.status_pa;
      } else if (state.currentLang === 'hi') {
        if (p.name_hi) plotName = p.name_hi;
        if (p.crop_hi) cropName = p.crop_hi;
        if (p.status_hi) statusName = p.status_hi;
      }

      const card = document.createElement('div');
      card.className = 'farm-card p-5';
      card.innerHTML = `
        <div class="flex items-start justify-between mb-3">
          <div>
            <h4 class="font-bold text-[#1C1E1B] text-base">${plotName}</h4>
            <span class="text-xs text-[#575E54]">${p.acres} Acres • ${cropName} (${p.variety})</span>
          </div>
          <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full ${
            p.status === 'Healthy' ? 'bg-[#DCFCE7] text-[#16A34A]' : 'bg-[#FEF3C7] text-[#D97706]'
          }">${statusName}</span>
        </div>
        <div class="space-y-1.5 text-xs text-[#575E54] bg-[#F8F7F2] p-3 rounded-lg border border-[#EDE8DC] mb-3">
          <div><strong class="text-[#1C1E1B]">Stage:</strong> ${p.stage}</div>
          <div><strong class="text-[#1C1E1B]">Sown:</strong> ${p.sowing_date}</div>
          <div><strong class="text-[#1C1E1B]">Irrigation:</strong> ${p.irrigation_type}</div>
        </div>
        <div class="flex items-center justify-between text-xs pt-2">
          <span class="text-[#858D82]">Parcel Health: <strong class="text-[#133E2B]">${p.health_score}/100</strong></span>
          <button onclick="switchTab('diagnose')" class="text-[#133E2B] font-bold hover:underline">Inspect Leaf →</button>
        </div>
      `;
      parcelsGrid.appendChild(card);
    });
  }

  // Soil health card
  const soil = d.soil_health;
  if (soil) {
    let phStatus = soil.ph_status;
    if (state.currentLang === 'pa' && soil.ph_status_pa) phStatus = soil.ph_status_pa;
    else if (state.currentLang === 'hi' && soil.ph_status_hi) phStatus = soil.ph_status_hi;

    const setEl = (id, val) => { const el = document.getElementById(id); if (el) el.innerText = val; };
    setEl('soil-ph-val', `${soil.ph} (${phStatus})`);
    setEl('soil-oc-val', `${soil.organic_carbon}% (${soil.oc_status})`);
    setEl('soil-n-val', `${soil.nitrogen} kg/ha (${soil.nitrogen_status})`);
    setEl('soil-p-val', `${soil.phosphorus} kg/ha (${soil.phosphorus_status})`);
    setEl('soil-k-val', `${soil.potassium} kg/ha (${soil.potassium_status})`);
    setEl('soil-zn-val', `${soil.zinc} ppm (${soil.zinc_status})`);
    setEl('soil-lab-meta', `Tested on: ${soil.last_tested}`);
    if (soil.advice) setEl('farm-soil-advice', soil.advice);
  }

  // Diagnosis History Log
  const logTable = document.getElementById('farm-history-table-body');
  if (logTable && d.diagnosis_history) {
    logTable.innerHTML = '';
    d.diagnosis_history.forEach(log => {
      const tr = document.createElement('tr');
      tr.className = 'border-b border-[#F0ECE1] text-xs';
      tr.innerHTML = `
        <td class="py-3 px-3 font-medium text-[#1C1E1B]">${log.date}</td>
        <td class="py-3 px-3 font-semibold text-[#133E2B]">${log.crop}</td>
        <td class="py-3 px-3 font-bold text-[#DC2626]">${log.disease}</td>
        <td class="py-3 px-3">${log.confidence}%</td>
        <td class="py-3 px-3 text-[#575E54]">${log.treatment_taken}</td>
        <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-[#E8F5E9] text-[#16A34A]">${log.status}</span></td>
      `;
      logTable.appendChild(tr);
    });
  }
}

function bindFarmEvents() {
  const addParcelBtn = document.getElementById('farm-add-parcel-btn');
  const modal = document.getElementById('add-parcel-modal');
  const closeBtn = document.getElementById('close-parcel-modal-btn');
  const form = document.getElementById('add-parcel-form');

  if (addParcelBtn && modal) addParcelBtn.addEventListener('click', () => modal.classList.remove('hidden'));
  if (closeBtn && modal) closeBtn.addEventListener('click', () => modal.classList.add('hidden'));

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const name = document.getElementById('new-parcel-name').value;
      const acres = parseFloat(document.getElementById('new-parcel-acres').value);
      const crop = document.getElementById('new-parcel-crop').value;
      const variety = document.getElementById('new-parcel-variety').value;

      try {
        const res = await fetch('/api/farm/parcel', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, acres, crop, variety })
        });
        const result = await res.json();
        if (result.status === 'success') {
          showToast("New field parcel added successfully!");
          modal.classList.add('hidden');
          form.reset();
          fetchFarmData();
        }
      } catch (err) {
        showToast("Error adding parcel.");
      }
    });
  }
}

// 10. FARMER AUTHENTICATION & LOGIN FLOW
function updateAuthHeaderUI() {
  const userProfileBtn = document.getElementById('user-profile-btn');
  const userAvatar = document.getElementById('user-avatar-initial');
  const userNameEl = document.getElementById('user-profile-name');

  if (state.activeFarmer) {
    let name = state.activeFarmer.name;
    if (state.currentLang === 'pa' && state.activeFarmer.name_pa) name = state.activeFarmer.name_pa;
    else if (state.currentLang === 'hi' && state.activeFarmer.name_hi) name = state.activeFarmer.name_hi;

    if (userNameEl) userNameEl.innerText = name.split(' ')[0] || name;
    if (userAvatar) userAvatar.innerText = name.charAt(0);
    if (userProfileBtn) userProfileBtn.title = `Logged in as ${name}`;
  } else {
    if (userNameEl) userNameEl.innerText = state.translations['nav_btn_login'] || 'Login';
    if (userAvatar) userAvatar.innerText = '👤';
  }
}

function bindAuthEvents() {
  const profileBtn = document.getElementById('user-profile-btn');
  const authModal = document.getElementById('farmer-auth-modal');
  const closeAuthBtn = document.getElementById('close-auth-modal-btn');

  if (profileBtn && authModal) {
    profileBtn.addEventListener('click', () => {
      if (state.activeFarmer) {
        openFarmerProfileDrawer();
      } else {
        openAuthLoginModal();
      }
    });
  }
  if (closeAuthBtn && authModal) {
    closeAuthBtn.addEventListener('click', () => authModal.classList.add('hidden'));
  }
  if (authModal) {
    authModal.addEventListener('click', (e) => {
      if (e.target === authModal) authModal.classList.add('hidden');
    });
  }

  // Auth tabs (Password vs OTP vs Demo)
  const tabPasswordBtn = document.getElementById('auth-tab-password');
  const tabOtpBtn = document.getElementById('auth-tab-otp');
  const tabDemoBtn = document.getElementById('auth-tab-demo');
  const panelPassword = document.getElementById('auth-panel-password');
  const panelOtp = document.getElementById('auth-panel-otp');
  const panelDemo = document.getElementById('auth-panel-demo');

  const switchAuthTab = (activeTab) => {
    [
      { btn: tabPasswordBtn, panel: panelPassword },
      { btn: tabOtpBtn, panel: panelOtp },
      { btn: tabDemoBtn, panel: panelDemo }
    ].forEach(item => {
      if (!item.btn || !item.panel) return;
      if (item.btn === activeTab) {
        item.btn.classList.add('border-b-2', 'border-[#133E2B]', 'text-[#133E2B]', 'font-bold');
        item.btn.classList.remove('text-[#858D82]');
        item.panel.classList.remove('hidden');
      } else {
        item.btn.classList.remove('border-b-2', 'border-[#133E2B]', 'text-[#133E2B]', 'font-bold');
        item.btn.classList.add('text-[#858D82]');
        item.panel.classList.add('hidden');
      }
    });
  };

  if (tabPasswordBtn) tabPasswordBtn.addEventListener('click', () => switchAuthTab(tabPasswordBtn));
  if (tabOtpBtn) tabOtpBtn.addEventListener('click', () => switchAuthTab(tabOtpBtn));
  if (tabDemoBtn) {
    tabDemoBtn.addEventListener('click', () => {
      switchAuthTab(tabDemoBtn);
      renderDemoProfilesList();
    });
  }

  // Password visibility toggle
  const togglePassBtn = document.getElementById('toggle-password-visibility-btn');
  const passInput = document.getElementById('auth-password-input');
  if (togglePassBtn && passInput) {
    togglePassBtn.addEventListener('click', () => {
      const isPass = passInput.type === 'password';
      passInput.type = isPass ? 'text' : 'password';
      togglePassBtn.innerText = isPass ? 'Hide Password' : 'Show Password';
    });
  }

  // Quick Credential Chips
  document.querySelectorAll('.quick-cred-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const u = chip.getAttribute('data-user');
      const p = chip.getAttribute('data-pass');
      const uInput = document.getElementById('auth-username-input');
      const pInput = document.getElementById('auth-password-input');
      if (uInput) uInput.value = u;
      if (pInput) pInput.value = p;
    });
  });

  // Password Login Submit
  const passLoginBtn = document.getElementById('auth-password-login-btn');
  const passErrorBox = document.getElementById('auth-password-error');
  if (passLoginBtn) {
    passLoginBtn.addEventListener('click', async () => {
      const usernameInput = document.getElementById('auth-username-input');
      const username = usernameInput ? usernameInput.value.trim() : '';
      const password = passInput ? passInput.value.trim() : '';

      if (!username) {
        if (passErrorBox) {
          passErrorBox.classList.remove('hidden');
          passErrorBox.innerText = 'Please enter your username, email, or mobile number.';
        }
        return;
      }
      if (!password) {
        if (passErrorBox) {
          passErrorBox.classList.remove('hidden');
          passErrorBox.innerText = 'Please enter your account password.';
        }
        return;
      }

      if (passErrorBox) passErrorBox.classList.add('hidden');
      passLoginBtn.disabled = true;
      const originalText = passLoginBtn.innerHTML;
      passLoginBtn.innerHTML = `<span>⏳</span><span>Verifying Credentials...</span>`;

      try {
        const res = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, password })
        });
        const d = await res.json();
        passLoginBtn.disabled = false;
        passLoginBtn.innerHTML = originalText;

        if (d.status === 'success') {
          state.activeFarmer = d.farmer;
          localStorage.setItem('fieldai_farmer', JSON.stringify(d.farmer));
          updateAuthHeaderUI();
          authModal.classList.add('hidden');
          showToast(`Welcome, ${d.farmer.name}! Farm data updated.`);
          await fetchFarmData();
          await fetchFarmerOrders();
        } else {
          if (passErrorBox) {
            passErrorBox.classList.remove('hidden');
            passErrorBox.innerText = d.message || 'Invalid login credentials.';
          } else {
            alert(d.message || 'Invalid login credentials.');
          }
        }
      } catch (err) {
        passLoginBtn.disabled = false;
        passLoginBtn.innerHTML = originalText;
        if (passErrorBox) {
          passErrorBox.classList.remove('hidden');
          passErrorBox.innerText = 'Connection error. Please try again.';
        }
      }
    });
  }

  // OTP Send button
  const sendOtpBtn = document.getElementById('auth-send-otp-btn');
  const otpInputGroup = document.getElementById('auth-otp-input-group');
  const phoneInput = document.getElementById('auth-phone-input');
  const otpNotice = document.getElementById('auth-otp-notice');

  if (sendOtpBtn) {
    sendOtpBtn.addEventListener('click', async () => {
      const phone = phoneInput ? phoneInput.value.trim() : '';
      if (phone.length < 10) {
        alert("Please enter a valid 10-digit mobile number");
        return;
      }

      sendOtpBtn.disabled = true;
      sendOtpBtn.innerText = "Sending...";

      try {
        const res = await fetch('/api/auth/send_otp', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ phone })
        });
        const d = await res.json();
        sendOtpBtn.disabled = false;
        sendOtpBtn.innerText = "OTP Sent ✓";

        if (d.status === 'success') {
          if (otpInputGroup) otpInputGroup.classList.remove('hidden');
          if (otpNotice) {
            otpNotice.classList.remove('hidden');
            otpNotice.innerText = `📲 OTP sent to +91 ${phone}. For instant testing, use OTP: ${d.demo_otp}`;
          }
          const otpCodeInput = document.getElementById('auth-otp-code-input');
          if (otpCodeInput) otpCodeInput.value = d.demo_otp;
        }
      } catch (err) {
        sendOtpBtn.disabled = false;
        sendOtpBtn.innerText = "Send OTP";
        alert("Failed to send OTP.");
      }
    });
  }

  // OTP Verify button
  const verifyOtpBtn = document.getElementById('auth-verify-otp-btn');
  if (verifyOtpBtn) {
    verifyOtpBtn.addEventListener('click', async () => {
      const phone = phoneInput ? phoneInput.value.trim() : '';
      const otpCodeInput = document.getElementById('auth-otp-code-input');
      const otp = otpCodeInput ? otpCodeInput.value.trim() : '';

      try {
        const res = await fetch('/api/auth/verify_otp', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ phone, otp })
        });
        const d = await res.json();
        if (d.status === 'success') {
          state.activeFarmer = d.farmer;
          localStorage.setItem('fieldai_farmer', JSON.stringify(d.farmer));
          updateAuthHeaderUI();
          authModal.classList.add('hidden');
          showToast(`Welcome back, ${d.farmer.name}!`);
          await fetchFarmData();
          await fetchFarmerOrders();
        } else {
          alert(d.message || "Invalid OTP");
        }
      } catch (err) {
        alert("Error verifying OTP.");
      }
    });
  }

  // Logout button in Profile Drawer
  const logoutBtn = document.getElementById('auth-logout-btn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', async () => {
      await fetch('/api/auth/logout', { method: 'POST' });
      state.activeFarmer = null;
      localStorage.removeItem('fieldai_farmer');
      updateAuthHeaderUI();
      const drawer = document.getElementById('farmer-profile-drawer');
      if (drawer) drawer.classList.add('hidden');
      showToast("Logged out successfully.");
      await fetchFarmData();
      await fetchFarmerOrders();
    });
  }
}

function openAuthLoginModal() {
  const modal = document.getElementById('farmer-auth-modal');
  if (modal) modal.classList.remove('hidden');
}

function openFarmerProfileDrawer() {
  const drawer = document.getElementById('farmer-profile-drawer');
  if (!drawer || !state.activeFarmer) return;

  const f = state.activeFarmer;
  const setEl = (id, val) => { const el = document.getElementById(id); if (el) el.innerText = val; };
  setEl('drawer-farmer-name', f.name);
  setEl('drawer-farmer-village', `${f.village}, ${f.district}, ${f.state}`);
  setEl('drawer-farmer-kisan-id', f.kisan_id);
  setEl('drawer-farmer-acres', `${f.total_acres} Acres`);
  setEl('drawer-farmer-tubewells', `${f.tubewells || 2} Submersible`);
  setEl('drawer-farmer-shc', f.shc_id || 'PAU-SHC-9042');

  drawer.classList.remove('hidden');
}

function renderDemoProfilesList() {
  const container = document.getElementById('auth-demo-profiles-list');
  if (!container || !state.demoFarmers) return;
  container.innerHTML = '';

  state.demoFarmers.forEach(df => {
    let name = df.name;
    if (state.currentLang === 'pa' && df.name_pa) name = df.name_pa;
    else if (state.currentLang === 'hi' && df.name_hi) name = df.name_hi;

    const btn = document.createElement('div');
    btn.className = 'p-3.5 rounded-xl border border-[#EDE8DC] bg-[#FAF9F5] hover:bg-[#F2EFE9] cursor-pointer transition flex items-center justify-between';
    btn.innerHTML = `
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-full bg-[#133E2B] text-white flex items-center justify-center font-bold text-sm">
          ${name.charAt(0)}
        </div>
        <div>
          <h4 class="font-bold text-sm text-[#1C1E1B]">${name}</h4>
          <span class="text-xs text-[#575E54]">${df.district}, ${df.state} • ${df.total_acres} Acres</span>
        </div>
      </div>
      <span class="text-xs font-bold text-[#16A34A]">Select →</span>
    `;
    btn.onclick = async () => {
      const res = await fetch('/api/auth/demo_login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ farmer_id: df.id })
      });
      const d = await res.json();
      if (d.status === 'success') {
        state.activeFarmer = d.farmer;
        localStorage.setItem('fieldai_farmer', JSON.stringify(d.farmer));
        updateAuthHeaderUI();
        document.getElementById('farmer-auth-modal').classList.add('hidden');
        showToast(`Logged in as ${d.farmer.name}`);
        await fetchFarmData();
        await fetchFarmerOrders();
      }
    };
    container.appendChild(btn);
  });
}

// 11. MULTI-OPTION PAYMENT GATEWAY & QR SYSTEM
function bindUpiPaymentEvents() {
  const checkoutBtn = document.getElementById('cart-checkout-btn');
  const upiModal = document.getElementById('upi-payment-modal');
  const closeUpiBtn = document.getElementById('close-upi-modal-btn');
  const updateUpiIdBtn = document.getElementById('update-upi-id-btn');
  const verifyUtrBtn = document.getElementById('verify-utr-btn');
  const instantVerifyBtn = document.getElementById('instant-verify-upi-btn');
  const autofillUtrBtn = document.getElementById('autofill-demo-utr-btn');
  const downloadQrBtn = document.getElementById('download-qr-btn');
  const copyUpiIdBtn = document.getElementById('copy-upi-id-btn');
  const copyUpiLinkBtn = document.getElementById('copy-upi-link-btn');
  const kccPayBtn = document.getElementById('kcc-pay-btn');
  const codPayBtn = document.getElementById('cod-pay-btn');
  const netbankingPayBtn = document.getElementById('netbanking-pay-btn');

  // Checkout open
  if (checkoutBtn) {
    checkoutBtn.addEventListener('click', () => {
      if (state.cart.length === 0) {
        alert(state.translations['cart_empty'] || "Your cart is empty. Add inputs first.");
        return;
      }
      openUpiPaymentModal();
    });
  }

  // Close modal
  if (closeUpiBtn && upiModal) {
    closeUpiBtn.addEventListener('click', () => upiModal.classList.add('hidden'));
  }

  // Payment Method Tab Switcher
  document.querySelectorAll('.pay-method-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      const method = tab.getAttribute('data-pay-method');
      state.activePayMethod = method;

      document.querySelectorAll('.pay-method-tab').forEach(t => {
        t.classList.remove('border-[#133E2B]', 'text-[#133E2B]');
        t.classList.add('border-transparent', 'text-[#858D82]');
      });
      tab.classList.add('border-[#133E2B]', 'text-[#133E2B]');
      tab.classList.remove('border-transparent', 'text-[#858D82]');

      ['upi', 'kcc', 'cod', 'netbanking'].forEach(m => {
        const panel = document.getElementById(`pay-panel-${m}`);
        if (panel) panel.classList.toggle('hidden', m !== method);
      });
    });
  });

  // Update receiver UPI ID
  if (updateUpiIdBtn) {
    updateUpiIdBtn.addEventListener('click', async () => {
      const customId = document.getElementById('custom-upi-id-input').value.trim();
      if (!customId || !customId.includes('@')) {
        alert("Please enter a valid UPI ID (e.g., yourname@okaxis, farmer@upi)");
        return;
      }
      state.configuredUpiId = customId;
      localStorage.setItem('fieldai_upi_id', customId);
      await generateGatewaySession();
      refreshUpiDisplay();
      showToast(`UPI Receiver set to: ${customId}`);
    });
  }

  // Download QR Code image
  if (downloadQrBtn) {
    downloadQrBtn.addEventListener('click', () => {
      const qrImg = document.getElementById('upi-qr-image');
      if (qrImg && qrImg.src) {
        const a = document.createElement('a');
        a.href = qrImg.src;
        a.download = `FIELDAI-UPI-${state.activeOrder?.order_id || 'QR'}.png`;
        a.click();
        showToast("QR Code downloaded!");
      }
    });
  }

  // Copy UPI ID
  if (copyUpiIdBtn) {
    copyUpiIdBtn.addEventListener('click', () => {
      const upiId = state.configuredUpiId || 'gillamritpal2007-1@okicici';
      if (window.QRCodeDrawer) {
        window.QRCodeDrawer.copyToClipboard(upiId, `Copied UPI ID: ${upiId}`);
      }
    });
  }

  // Copy UPI Payment Link
  if (copyUpiLinkBtn) {
    copyUpiLinkBtn.addEventListener('click', () => {
      const upiUri = state.activeOrder?.upi_uri || document.getElementById('upi-link-display').innerText;
      if (window.QRCodeDrawer) {
        window.QRCodeDrawer.copyToClipboard(upiUri, "Copied UPI Payment Link!");
      }
    });
  }

  // Demo UTR autofill
  if (autofillUtrBtn) {
    autofillUtrBtn.addEventListener('click', () => {
      const randomUtr = `4291${Math.floor(10000000 + Math.random() * 90000000)}`;
      document.getElementById('upi-utr-input').value = randomUtr;
    });
  }

  // Instant 1-Click Sandbox Pay & Verify
  if (instantVerifyBtn) {
    instantVerifyBtn.addEventListener('click', async () => {
      instantVerifyBtn.disabled = true;
      instantVerifyBtn.innerText = "Verifying with NPCI...";
      await processOrderPayment({
        is_sandbox: true,
        payment_method: "UPI Instant Settlement (NPCI)"
      });
      instantVerifyBtn.disabled = false;
      instantVerifyBtn.innerText = state.translations['pay_instant_test_btn'] || "⚡ Instant 1-Click Pay & Verify (Sandbox Mode)";
    });
  }

  // Standard UTR Verification
  if (verifyUtrBtn) {
    verifyUtrBtn.addEventListener('click', async () => {
      const utr = document.getElementById('upi-utr-input').value.trim();
      if (utr.length < 6) {
        alert("Please enter your 12-digit UPI Reference Number (UTR) from your payment app.");
        return;
      }
      verifyUtrBtn.disabled = true;
      verifyUtrBtn.innerText = "Verifying with NPCI...";
      await processOrderPayment({
        utr: utr,
        payment_method: "UPI Instant Settlement (NPCI)"
      });
      verifyUtrBtn.disabled = false;
      verifyUtrBtn.innerText = state.translations['pay_btn_verify_utr'] || "Verify UTR & Complete Order";
    });
  }

  // KCC Payment
  if (kccPayBtn) {
    kccPayBtn.addEventListener('click', async () => {
      kccPayBtn.disabled = true;
      kccPayBtn.innerText = "Authorizing KCC...";
      await processOrderPayment({
        payment_method: "Kisan Credit Card (PM-KISAN RuPay)",
        utr: `KCC-${Math.floor(100000000 + Math.random() * 900000000)}`
      });
      kccPayBtn.disabled = false;
      kccPayBtn.innerText = state.translations['pay_kcc_btn'] || "Pay with Kisan Credit Card";
    });
  }

  // Cash on Delivery Payment
  if (codPayBtn) {
    codPayBtn.addEventListener('click', async () => {
      codPayBtn.disabled = true;
      codPayBtn.innerText = "Confirming COD...";
      await processOrderPayment({
        payment_method: "Cash on Delivery (Kisan Kendra Express)",
        utr: `COD-${Math.floor(100000000 + Math.random() * 900000000)}`
      });
      codPayBtn.disabled = false;
      codPayBtn.innerText = state.translations['pay_cod_btn'] || "Confirm Order (Pay on Delivery)";
    });
  }

  // Net Banking Payment
  if (netbankingPayBtn) {
    netbankingPayBtn.addEventListener('click', async () => {
      const selectedBank = document.querySelector('input[name="netbank"]:checked')?.parentElement?.innerText?.trim() || "State Bank of India";
      netbankingPayBtn.disabled = true;
      netbankingPayBtn.innerText = "Connecting to Bank...";
      await processOrderPayment({
        payment_method: `Net Banking (${selectedBank})`,
        utr: `NET-${Math.floor(100000000 + Math.random() * 900000000)}`
      });
      netbankingPayBtn.disabled = false;
      netbankingPayBtn.innerText = state.translations['pay_netbanking_btn'] || "Authorize via Net Banking";
    });
  }
}

async function generateGatewaySession() {
  const subtotal = state.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  const subsidy = subtotal > 1000 ? 200 : 0;
  const total = Math.max(0, subtotal - subsidy);

  try {
    const res = await fetch('/api/payment/generate_upi', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: total, custom_upi_id: state.configuredUpiId })
    });
    const d = await res.json();
    if (d.status === 'success') {
      state.activeOrder = d;
      return d;
    }
  } catch (e) {
    console.error("Could not initialize UPI Gateway:", e);
  }
  return null;
}

async function openUpiPaymentModal() {
  if (!state.cart || state.cart.length === 0) {
    showToast(state.translations['cart_empty'] || "Your cart is empty. Please add a product first!");
    return;
  }
  const modal = document.getElementById('upi-payment-modal');
  if (!modal) return;

  closeCartDrawer();

  const upiInput = document.getElementById('custom-upi-id-input');
  if (upiInput) upiInput.value = state.configuredUpiId;

  const session = await generateGatewaySession();
  if (session) {
    refreshUpiDisplay();
    modal.classList.remove('hidden');
  } else {
    alert("Could not initialize payment gateway. Please check network connection.");
  }
}

function refreshUpiDisplay() {
  if (!state.activeOrder) return;
  const d = state.activeOrder;

  const subtotal = state.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  const subsidy = subtotal > 1000 ? 200 : 0;
  const total = Math.max(0, subtotal - subsidy);
  const upiId = state.configuredUpiId || 'gillamritpal2007-1@okicici';

  // Format headers
  document.getElementById('upi-amount-display').innerText = `₹${total.toLocaleString()}`;
  document.getElementById('upi-receiver-display').innerText = upiId;
  document.getElementById('upi-order-id-display').innerText = d.order_id;
  document.getElementById('upi-link-display').innerText = d.upi_uri;

  // Real Scannable QR image from Python qrcode
  const qrImg = document.getElementById('upi-qr-image');
  if (qrImg && d.qr_image_url) {
    qrImg.src = d.qr_image_url;
  }

  // Direct 1-Click Launch buttons for mobile UPI apps
  const gpayBtn = document.getElementById('gpay-app-btn');
  if (gpayBtn) gpayBtn.href = d.gpay_url || d.upi_uri;

  const phonepeBtn = document.getElementById('phonepe-app-btn');
  if (phonepeBtn) phonepeBtn.href = d.phonepe_url || d.upi_uri;

  const paytmBtn = document.getElementById('paytm-app-btn');
  if (paytmBtn) paytmBtn.href = d.paytm_url || d.upi_uri;

  const bhimBtn = document.getElementById('bhim-app-btn');
  if (bhimBtn) bhimBtn.href = d.bhim_url || d.upi_uri;

  const directBtn = document.getElementById('upi-direct-app-btn');
  if (directBtn) directBtn.href = d.upi_uri;

  // Draw on Canvas via QRCodeDrawer
  const qrCanvas = document.getElementById('upi-qr-canvas');
  if (qrCanvas && window.QRCodeDrawer) {
    window.QRCodeDrawer.drawUPI(qrCanvas, d.upi_uri, 220, d.qr_image_url);
  }

  // Update KCC & COD details
  const kccName = document.getElementById('kcc-cardholder-name');
  if (kccName) kccName.innerText = state.activeFarmer?.name || "Amritpal Singh Gill";

  const codAddr = document.getElementById('cod-delivery-address');
  if (codAddr && state.activeFarmer) {
    codAddr.innerText = `${state.activeFarmer.village || 'Gill Kalan'}, ${state.activeFarmer.district || 'Ludhiana'}, ${state.activeFarmer.state || 'Punjab'}`;
  }
}

async function processOrderPayment(extraPayload = {}) {
  const modal = document.getElementById('upi-payment-modal');
  const subtotal = state.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  const subsidy = subtotal > 1000 ? 200 : 0;
  const total = Math.max(0, subtotal - subsidy);

  const payload = {
    order_id: state.activeOrder?.order_id || `KMP-${Math.floor(100000 + Math.random() * 900000)}`,
    upi_id: state.configuredUpiId,
    amount: total,
    items: state.cart,
    farmer_name: state.activeFarmer?.name || "Amritpal Singh Gill",
    ...extraPayload
  };

  try {
    const res = await fetch('/api/payment/verify_upi', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const d = await res.json();
    if (d.status === 'success') {
      if (modal) modal.classList.add('hidden');
      state.cart = [];
      updateCartUI();
      const cartDrawer = document.getElementById('cart-drawer');
      if (cartDrawer) cartDrawer.classList.add('hidden');
      
      openOrderInvoiceModal(d.invoice);
      await fetchFarmerOrders();
      showToast(`Order ${d.invoice.order_id} Confirmed!`);
    } else {
      alert(d.message || "Payment verification failed.");
    }
  } catch (e) {
    alert("Error completing payment. Please try again.");
  }
}

async function quickBuyNow(prodId) {
  if (!state.products || state.products.length === 0) {
    await fetchProducts();
  }
  const p = (state.products || []).find(item => item.id === prodId) || 
            state.activeDiagnosis?.recommended_products?.find(item => item.id === prodId);
  if (!p) {
    console.warn("Product not found for quick buy:", prodId);
    return;
  }

  // Ensure item is in cart with at least qty 1
  const existing = state.cart.find(item => item.id === prodId);
  if (!existing) {
    state.cart.push({ ...p, qty: 1 });
  }
  updateCartUI();
  closeCartDrawer();
  await openUpiPaymentModal();
}

function openOrderInvoiceModal(inv) {
  const modal = document.getElementById('kisan-invoice-modal');
  if (!modal) return;

  document.getElementById('inv-no').innerText = inv.invoice_no;
  document.getElementById('inv-order-id').innerText = inv.order_id;
  document.getElementById('inv-utr').innerText = inv.utr_ref;
  document.getElementById('inv-date').innerText = inv.paid_at;
  document.getElementById('inv-amount').innerText = `₹${Number(inv.amount_paid).toLocaleString()}`;
  document.getElementById('inv-farmer').innerText = inv.farmer_name;
  document.getElementById('inv-address').innerText = inv.delivery_address;
  document.getElementById('inv-gstin').innerText = inv.gstin;

  const itemsTable = document.getElementById('inv-items-table');
  if (itemsTable && inv.items) {
    itemsTable.innerHTML = '';
    inv.items.forEach(item => {
      const tr = document.createElement('tr');
      tr.className = 'border-b border-[#F0ECE1] text-xs';
      tr.innerHTML = `
        <td class="py-2 text-[#1C1E1B] font-semibold">${item.name} (${item.pack_size})</td>
        <td class="py-2 text-center text-[#575E54]">${item.qty}</td>
        <td class="py-2 text-right font-bold text-[#133E2B]">₹${item.price * item.qty}</td>
      `;
      itemsTable.appendChild(tr);
    });
  }

  modal.classList.remove('hidden');
}

// Fetch & Render Orders in My Farm Tab
async function fetchFarmerOrders() {
  try {
    const res = await fetch('/api/orders');
    const data = await res.json();
    if (data.status === 'success') {
      state.farmerOrders = data.orders;
      renderFarmOrders();
    }
  } catch (err) {
    console.error("Orders fetch error:", err);
  }
}

function renderFarmOrders() {
  const tbody = document.getElementById('farm-orders-table-body');
  const badge = document.getElementById('farm-orders-badge');
  if (!tbody) return;

  tbody.innerHTML = '';
  const orders = state.farmerOrders || [];

  if (badge) {
    badge.innerText = `${orders.length} Confirmed Order${orders.length !== 1 ? 's' : ''}`;
  }

  if (orders.length === 0) {
    tbody.innerHTML = `<tr><td colspan="7" class="py-6 text-center text-[#858D82]">No agricultural purchases recorded yet. Items bought in the marketplace will appear here.</td></tr>`;
    return;
  }

  orders.forEach(ord => {
    const tr = document.createElement('tr');
    tr.className = 'border-b border-[#E8E5DC] hover:bg-[#FAF9F5] transition';
    
    const itemsSummary = (ord.items || []).map(i => `${i.name} (x${i.qty})`).join(', ') || 'Agricultural Input Pack';
    
    tr.innerHTML = `
      <td class="py-3 px-3 text-[#575E54] whitespace-nowrap">${ord.paid_at || 'Today'}</td>
      <td class="py-3 px-3 font-mono font-bold text-[#133E2B] whitespace-nowrap">${ord.order_id}</td>
      <td class="py-3 px-3 text-[#1C1E1B] max-w-xs truncate" title="${itemsSummary}">${itemsSummary}</td>
      <td class="py-3 px-3 text-[#575E54] whitespace-nowrap">${ord.payment_method || 'UPI Settlement'}</td>
      <td class="py-3 px-3 text-right font-bold text-[#133E2B] whitespace-nowrap">₹${Number(ord.amount_paid).toLocaleString()}</td>
      <td class="py-3 px-3 whitespace-nowrap">
        <span class="inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-[#DCFCE7] text-[#16A34A] border border-[#BBF7D0]">
          ${ord.status || 'PAID'}
        </span>
      </td>
      <td class="py-3 px-3 text-center whitespace-nowrap">
        <button class="px-2.5 py-1 rounded-lg bg-[#F2EFE9] text-[#133E2B] hover:bg-[#E4E0D5] font-bold text-[11px] transition">
          View
        </button>
      </td>
    `;
    
    const viewBtn = tr.querySelector('button');
    if (viewBtn) {
      viewBtn.addEventListener('click', () => openOrderInvoiceModal(ord));
    }
    
    tbody.appendChild(tr);
  });
}

// 12. DEVELOPER & AGRITECH DEBUG HUD
function bindDebugHudEvents() {
  const toggleBtn = document.getElementById('debug-hud-toggle-btn');
  const modal = document.getElementById('debug-hud-modal');
  const closeBtn = document.getElementById('close-debug-hud-btn');

  if (toggleBtn && modal) {
    toggleBtn.addEventListener('click', () => {
      refreshDebugHudData();
      modal.classList.remove('hidden');
    });
  }

  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => modal.classList.add('hidden'));
  }

  // Debug Tabs
  document.querySelectorAll('.dbg-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tabName = btn.getAttribute('data-dbg-tab');
      document.querySelectorAll('.dbg-tab-btn').forEach(b => {
        b.classList.remove('border-emerald-400', 'text-emerald-400');
        b.classList.add('border-transparent', 'text-gray-400');
      });
      btn.classList.add('border-emerald-400', 'text-emerald-400');
      btn.classList.remove('border-transparent', 'text-gray-400');

      ['gateway', 'session', 'system', 'logs'].forEach(t => {
        const p = document.getElementById(`dbg-panel-${t}`);
        if (p) p.classList.toggle('hidden', t !== tabName);
      });
    });
  });

  // Action: Seed Test Cart
  const seedCartBtn = document.getElementById('dbg-seed-cart-btn');
  if (seedCartBtn) {
    seedCartBtn.addEventListener('click', () => {
      const p1 = state.products[0] || { id: 'tilt_25_ec', name: 'Tilt 25% EC', price: 420, pack_size: '500 ml' };
      const p2 = state.products[1] || { id: 'nano_urea', name: 'IFFCO Nano Urea', price: 225, pack_size: '500 ml' };
      state.cart = [{ ...p1, qty: 2 }, { ...p2, qty: 1 }];
      updateCartUI();
      const cartDrawer = document.getElementById('cart-drawer');
      if (cartDrawer) cartDrawer.classList.remove('hidden');
      if (modal) modal.classList.add('hidden');
      showToast("Test products added to cart!");
    });
  }

  // Action: Instant Test Order
  const instantOrderBtn = document.getElementById('dbg-instant-order-btn');
  if (instantOrderBtn) {
    instantOrderBtn.addEventListener('click', async () => {
      try {
        const res = await fetch('/api/orders/simulate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ qty: 2 }) });
        const d = await res.json();
        if (d.status === 'success') {
          if (modal) modal.classList.add('hidden');
          openOrderInvoiceModal(d.invoice);
          await fetchFarmerOrders();
          showToast(`Simulated Order ${d.invoice.order_id} Created!`);
        }
      } catch (err) {
        alert("Failed to simulate order");
      }
    });
  }

  // Action: Sim Disease Diagnosis
  const simDiseaseBtn = document.getElementById('dbg-sim-disease-btn');
  if (simDiseaseBtn) {
    simDiseaseBtn.addEventListener('click', async () => {
      switchTab('diagnose');
      if (modal) modal.classList.add('hidden');
      const cropSel = document.getElementById('diag-crop-select');
      if (cropSel) cropSel.value = 'wheat';
      const sampleChip = document.querySelector('[data-sample-id="wheat_yellow_rust"]');
      if (sampleChip) sampleChip.click();
      const scanBtn = document.getElementById('diag-run-analyze-btn');
      if (scanBtn) scanBtn.click();
    });
  }

  // Action: Ping Health
  const pingHealthBtn = document.getElementById('dbg-ping-health-btn');
  if (pingHealthBtn) {
    pingHealthBtn.addEventListener('click', async () => {
      const t0 = performance.now();
      try {
        const res = await fetch('/api/health');
        const ms = Math.round(performance.now() - t0);
        const d = await res.json();
        document.getElementById('dbg-api-latency').innerText = `${ms} ms (${d.server})`;
        showToast(`Health OK (${ms}ms)`);
      } catch (e) {
        document.getElementById('dbg-api-latency').innerText = 'Unreachable';
      }
    });
  }

  // Clear Logs
  const clearLogsBtn = document.getElementById('dbg-clear-logs-btn');
  if (clearLogsBtn) {
    clearLogsBtn.addEventListener('click', () => {
      debugLogs.length = 0;
      const c = document.getElementById('dbg-logs-container');
      if (c) c.innerHTML = '<div class="text-gray-500 py-2">Logs cleared.</div>';
    });
  }
}

function refreshDebugHudData() {
  const vpa = document.getElementById('dbg-upi-vpa');
  if (vpa) vpa.innerText = state.configuredUpiId || 'gillamritpal2007-1@okicici';

  const cartCount = document.getElementById('dbg-cart-count');
  const cartTotal = document.getElementById('dbg-cart-total');
  const totalItems = state.cart.reduce((sum, item) => sum + item.qty, 0);
  const totalVal = state.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  if (cartCount) cartCount.innerText = `${totalItems} items`;
  if (cartTotal) cartTotal.innerText = `₹${totalVal}`;

  const ordersCount = document.getElementById('dbg-orders-count');
  if (ordersCount) ordersCount.innerText = `${state.farmerOrders.length} orders`;

  const sessionJson = document.getElementById('dbg-session-json');
  if (sessionJson) {
    sessionJson.innerText = JSON.stringify({
      active_farmer: state.activeFarmer,
      current_lang: state.currentLang,
      cart_items_count: state.cart.length,
      orders_count: state.farmerOrders.length,
      configured_upi: state.configuredUpiId
    }, null, 2);
  }

  // Trigger health probe
  const pingBtn = document.getElementById('dbg-ping-health-btn');
  if (pingBtn) pingBtn.click();
}

// 12. Shopping Cart Logic
async function addToCart(prodId) {
  if (!state.products || state.products.length === 0) {
    await fetchProducts();
  }
  const p = (state.products || []).find(item => item.id === prodId) || 
            state.activeDiagnosis?.recommended_products?.find(item => item.id === prodId);
  if (!p) {
    console.warn("Product not found:", prodId);
    return;
  }

  const existing = state.cart.find(item => item.id === prodId);
  if (existing) {
    existing.qty += 1;
  } else {
    state.cart.push({ ...p, qty: 1 });
  }

  updateCartUI();
  let prodName = p.name;
  if (state.currentLang === 'pa' && p.name_pa) prodName = p.name_pa;
  else if (state.currentLang === 'hi' && p.name_hi) prodName = p.name_hi;
  showToast(`Added ${prodName} to cart!`);
}

function updateCartUI() {
  const badge = document.getElementById('cart-count-badge');
  const totalItems = state.cart.reduce((sum, item) => sum + item.qty, 0);
  if (badge) {
    badge.innerText = totalItems;
    badge.classList.toggle('hidden', totalItems === 0);
  }

  const drawerList = document.getElementById('cart-drawer-items');
  if (!drawerList) return;
  drawerList.innerHTML = '';

  if (state.cart.length === 0) {
    drawerList.innerHTML = `<div class="p-8 text-center text-sm text-[#858D82]">${state.translations['cart_empty'] || "Your cart is currently empty."}</div>`;
  } else {
    state.cart.forEach(item => {
      let prodName = item.name;
      if (state.currentLang === 'pa' && item.name_pa) prodName = item.name_pa;
      else if (state.currentLang === 'hi' && item.name_hi) prodName = item.name_hi;

      const row = document.createElement('div');
      row.className = 'flex items-center justify-between p-3 bg-white rounded-xl border border-[#EDE8DC] mb-2';
      row.innerHTML = `
        <div class="flex items-center space-x-3">
          <img src="${item.image}" alt="${prodName}" onerror="this.onerror=null; this.src='/static/img/products/tilt.png';" class="w-12 h-12 object-contain bg-[#FAF9F5] p-1 rounded-lg">
          <div>
            <h5 class="text-xs font-bold text-[#1C1E1B] leading-tight">${prodName}</h5>
            <span class="text-[11px] text-[#133E2B] font-semibold">₹${item.price} each</span>
          </div>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="changeCartQty('${item.id}', -1)" class="w-6 h-6 rounded bg-[#F2EFE9] text-xs font-bold flex items-center justify-center hover:bg-[#E4E0D5] cursor-pointer">-</button>
          <span class="text-xs font-bold w-4 text-center">${item.qty}</span>
          <button onclick="changeCartQty('${item.id}', 1)" class="w-6 h-6 rounded bg-[#F2EFE9] text-xs font-bold flex items-center justify-center hover:bg-[#E4E0D5] cursor-pointer">+</button>
        </div>
      `;
      drawerList.appendChild(row);
    });
  }

  const subtotal = state.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  const subsidyDiscount = subtotal > 1000 ? 200 : 0;
  const grandTotal = Math.max(0, subtotal - subsidyDiscount);

  const subEl = document.getElementById('cart-subtotal-val');
  if (subEl) subEl.innerText = `₹${subtotal.toLocaleString()}`;
  const subDiscEl = document.getElementById('cart-subsidy-val');
  if (subDiscEl) subDiscEl.innerText = `-₹${subsidyDiscount.toLocaleString()}`;
  const totEl = document.getElementById('cart-total-val');
  if (totEl) totEl.innerText = `₹${grandTotal.toLocaleString()}`;
}

function changeCartQty(prodId, delta) {
  const item = state.cart.find(i => i.id === prodId);
  if (!item) return;
  item.qty += delta;
  if (item.qty <= 0) {
    state.cart = state.cart.filter(i => i.id !== prodId);
  }
  updateCartUI();
}

function openCartDrawer() {
  updateCartUI();
  const cartDrawer = document.getElementById('cart-drawer');
  if (cartDrawer) {
    cartDrawer.classList.remove('hidden');
  }
}

function closeCartDrawer() {
  const cartDrawer = document.getElementById('cart-drawer');
  if (cartDrawer) {
    cartDrawer.classList.add('hidden');
  }
}

function toggleNotifDrawer() {
  const notifDrawer = document.getElementById('notif-drawer');
  if (notifDrawer) {
    notifDrawer.classList.toggle('hidden');
  }
}

function bindCartEvents() {
  const openCartBtn = document.getElementById('open-cart-btn');
  const closeCartBtn = document.getElementById('close-cart-btn');
  const cartDrawer = document.getElementById('cart-drawer');
  const checkoutBtn = document.getElementById('cart-checkout-btn');

  if (openCartBtn) {
    openCartBtn.onclick = (e) => {
      e.preventDefault();
      openCartDrawer();
    };
  }
  if (closeCartBtn) {
    closeCartBtn.onclick = (e) => {
      e.preventDefault();
      closeCartDrawer();
    };
  }
  if (checkoutBtn) {
    checkoutBtn.onclick = (e) => {
      e.preventDefault();
      openUpiPaymentModal();
    };
  }
}

// 13. Modals & Notifications Toggles
function bindModalToggles() {
  const notifBtn = document.getElementById('notif-bell-btn');
  const notifDrawer = document.getElementById('notif-drawer');
  const notifClose = document.getElementById('close-notif-btn');

  if (notifBtn) {
    notifBtn.onclick = (e) => {
      e.preventDefault();
      toggleNotifDrawer();
    };
  }
  if (notifClose && notifDrawer) {
    notifClose.onclick = (e) => {
      e.preventDefault();
      notifDrawer.classList.add('hidden');
    };
  }

  const closeDrawerBtn = document.getElementById('close-profile-drawer-btn');
  const drawer = document.getElementById('farmer-profile-drawer');
  if (closeDrawerBtn && drawer) closeDrawerBtn.addEventListener('click', () => drawer.classList.add('hidden'));

  const prodModal = document.getElementById('product-details-modal');
  const prodClose = document.getElementById('close-product-modal-btn');
  if (prodClose && prodModal) prodClose.addEventListener('click', () => prodModal.classList.add('hidden'));

  const invModal = document.getElementById('kisan-invoice-modal');
  const invClose = document.getElementById('close-invoice-modal-btn');
  if (invClose && invModal) invClose.addEventListener('click', () => invModal.classList.add('hidden'));
}

function showToast(msg) {
  const toast = document.getElementById('app-toast');
  if (!toast) return;
  toast.innerText = msg;
  toast.classList.remove('opacity-0', 'pointer-events-none');
  toast.classList.add('opacity-100');
  setTimeout(() => {
    toast.classList.add('opacity-0', 'pointer-events-none');
    toast.classList.remove('opacity-100');
  }, 3200);
}

// Expose functions globally for inline HTML attributes and outside access
window.switchTab = switchTab;
window.openCartDrawer = openCartDrawer;
window.closeCartDrawer = closeCartDrawer;
window.toggleNotifDrawer = toggleNotifDrawer;
window.addToCart = addToCart;
window.quickBuyNow = quickBuyNow;
window.changeCartQty = changeCartQty;
window.openProductModal = openProductModal;
window.openUpiPaymentModal = openUpiPaymentModal;
window.processOrderPayment = processOrderPayment;
window.openOrderInvoiceModal = openOrderInvoiceModal;
window.openAuthLoginModal = openAuthLoginModal;
window.openFarmerProfileDrawer = openFarmerProfileDrawer;
window.showToast = showToast;
