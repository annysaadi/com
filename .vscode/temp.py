import re

with open('c:\\Users\\loany\\Documents\\annysaadi.github.io\\annysaadi.github.io\\training.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see the contato section
match = re.search(r'(<!-- CONTATO -->.*?<div class="final-inner fade-up">)(.*?)A gente tǭ aqui', content, re.DOTALL | re.IGNORECASE)
if match:
    print(match.group(1))
    print("---")
    print(match.group(2))
else:
    print("Not found")
