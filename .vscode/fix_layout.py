import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Padronizar sec-body para melhor legibilidade
if 'max-width: 640px;' not in content:
    content = re.sub(r'(\.sec-body\s*\{[^}]*)', r'\g<1>  max-width: 640px;\n', content)

# 2. Melhorar os espaçamentos das seções (Desktop)
# Atualmente tem coisas espalhadas, mas vamos focar nas regras gerais de margem/padding
content = re.sub(r'padding:\s*40px\s+36px;', 'padding: 64px 24px;', content)
content = re.sub(r'padding:\s*48px\s+36px\s+40px;', 'padding: 64px 24px 48px;', content)

# 3. Melhorar espaçamentos mobile (Media Queries de 900px)
content = re.sub(r'padding:\s*24px\s+36px\s+36px\s+!important;', 'padding: 32px 24px 40px !important;', content)
content = re.sub(r'padding-top:\s*34px;', 'padding-top: 48px;', content)
content = re.sub(r'padding-bottom:\s*34px;', 'padding-bottom: 48px;', content)
content = re.sub(r'padding:\s*18px\s+24px\s+0;', 'padding: 24px 24px 0;', content)
content = re.sub(r'margin-top:\s*22px;', 'margin-top: 24px;', content)
content = re.sub(r'margin-top:\s*18px;', 'margin-top: 24px;', content)

# 4. Ajustar Hero padding base e arredondamentos
content = re.sub(r'padding:\s*80px\s+32px\s+48px;', 'padding: 96px 32px 64px;', content)

# 5. Padronizar line-height do sec-body (se existir) para 1.6 ou 1.7
# Isso já costuma ser bom, mas vamos garantir ritmos de parágrafos.
content = re.sub(r'margin-bottom:\s*18px;', 'margin-bottom: 24px;', content)
content = re.sub(r'margin-bottom:\s*14px;', 'margin-bottom: 16px;', content)
content = re.sub(r'gap:\s*14px\s+20px;', 'gap: 16px 24px;', content)
content = re.sub(r'gap:\s*7px;', 'gap: 8px;', content)
content = re.sub(r'gap:\s*10px;', 'gap: 12px;', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('O Layout foi refinado para proporções e escalas matemáticas mais elegantes.')
