import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re
from data.translations import TRANSLATIONS

with open('templates/index.html', encoding='utf-8') as f:
    html_code = f.read()

with open('static/js/app.js', encoding='utf-8') as f:
    js_code = f.read()

html_keys = set(re.findall(r'data-i18n=["\']([^"\']+)["\']', html_code))
js_keys = set(re.findall(r'state\.translations\[["\']([^"\']+)["\']\]', js_code))
all_needed_keys = html_keys | js_keys

for lang in ['en', 'pa', 'hi']:
    provided = set(TRANSLATIONS[lang].keys())
    missing = all_needed_keys - provided
    print(f"Language {lang}: {len(provided)} translations defined.")
    if missing:
        print(f"  Missing in {lang}: {sorted(list(missing))}")
    else:
        print(f"  All {len(all_needed_keys)} needed keys are present in {lang}!")
