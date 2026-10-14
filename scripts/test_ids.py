import re

with open('static/js/app.js', encoding='utf-8') as f:
    js_code = f.read()

with open('templates/index.html', encoding='utf-8') as f:
    html_code = f.read()

js_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js_code))
html_ids = set(re.findall(r"id=['\"]([^'\"]+)['\"]", html_code))

missing = js_ids - html_ids
print("Total IDs referenced in JS:", len(js_ids))
print("Total IDs present in HTML:", len(html_ids))
print("Missing IDs:", sorted(list(missing)))
