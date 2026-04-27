import sys

file_path = r'c:\Users\loany\Documents\annysaadi.github.io\annysaadi.github.io\training.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''<div class="final-inner fade-up">
          <p class="sec-tag sec-tag-dark" style="display: block; margin-bottom: 12px">
            não entendeu algo?
          </p>'''

replacement = '''<div class="final-inner fade-up">
          <div class="guide-head" style="margin-bottom: 16px"><span class="guide-tag" style="background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.1); color: white;">suporte</span></div>
          <p class="sec-tag sec-tag-dark" style="display: block; margin-bottom: 12px">
            não entendeu algo?
          </p>'''

if target in content:
    content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replace successful!")
else:
    print("Target not found. Looking for alternatives...")
    idx = content.find('não entendeu algo?')
    if idx != -1:
        start = max(0, idx - 100)
        end = min(len(content), idx + 100)
        print("Found here:")
        print(content[start:end])
    else:
        print("Text 'não entendeu algo?' not found at all.")

