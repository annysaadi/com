import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'id="contato".*?class="final-inner fade-up">.*?(<p class="sec-tag[^>]*>.*?não entendeu algo\?.*?</p>)', html, re.DOTALL | re.IGNORECASE)
if match:
    print(match.group(0))
else:
    print("Section not found.")
