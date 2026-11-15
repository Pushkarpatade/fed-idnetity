import os
import glob
import re

dist = os.path.abspath('frontend/dist')
html_path = os.path.join(dist, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

css_files = glob.glob(os.path.join(dist, 'assets', '*.css'))
js_files = glob.glob(os.path.join(dist, 'assets', '*.js'))

css_content = ''
for c in css_files:
    with open(c, 'r', encoding='utf-8') as f:
        css_content += f.read() + '\n'

js_content = ''
for j in js_files:
    with open(j, 'r', encoding='utf-8') as f:
        js_content += f.read() + '\n'

# Inline CSS
html = re.sub(r'<link[^>]*rel=["\']stylesheet["\'][^>]*>', '', html)
html = html.replace('</head>', f'<style>\n{css_content}\n</style></head>')

# Inline JS
html = re.sub(r'<script[^>]*type=["\']module["\'][^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = html.replace('</body>', f'<script type="module">\n{js_content}\n</script></body>')

standalone_path = os.path.join(dist, 'standalone.html')
with open(standalone_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated standalone.html successfully! Size: {len(html)} bytes")
