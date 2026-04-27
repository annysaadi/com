import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Garantir que a .hero-content esteja perfeitamente centralizada e o texto nela não estoure.
if 'margin: 0 auto' not in re.search(r'\.hero-content\s*\{([^}]*)\}', content).group(1):
    content = re.sub(r'(\.hero-content\s*\{[^}]*)', r'\g<1>  margin: 0 auto;\n  width: 100%;\n', content)

# Garantir que as seções principais também alinhem seus blocos no centro
if 'margin: 0 auto;' not in re.search(r'\.section\s*\{([^}]*)\}', content).group(1):
    content = re.sub(r'(\.section\s*\{[^}]*)', r'\g<1>  max-width: 900px;\n  margin: 0 auto;\n', content)

# Ajuste fino na leitura de parágrafos principais
content = re.sub(r'(\.sec-body\s*\{[^}]*line-height:\s*)[0-9\.]+', r'\g<1>1.65', content)
content = re.sub(r'(\.sec-body\s*\{[^}]*font-size:\s*)[0-9]+px', r'\g<1>16px', content)
content = re.sub(r'(\.sec-body\s*\{[^}]*color:\s*)var\(--ink-2\)', r'\g<1>var(--ink)', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Alinhamentos centralizados e ajustes de legibilidade concluídos.')
