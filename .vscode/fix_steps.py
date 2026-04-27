import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path_html = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.html'
with open(path_html, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('16 Passos', '15 Passos')
# Remove ou ajusta o número 16 do menu lateral (Falar com a gente)
html = html.replace('<span class="nav-num">16</span>', '<span class="nav-num">✦</span>')

with open(path_html, 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML atualizado.')

path_css = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
with open(path_css, 'r', encoding='utf-8') as f:
    css = f.read()

# Substituir 'passo x de 16' por 'passo x de 15'
css = css.replace('passo 1 de 16', 'passo 1 de 15')
css = css.replace('passo 2 de 16', 'passo 2 de 15')
css = css.replace('passo 3 de 16', 'passo 3 de 15')
css = css.replace('passo 4 de 16', 'passo 4 de 15')
css = css.replace('passo 5 de 16', 'passo 5 de 15')
css = css.replace('passo 6 de 16', 'passo 6 de 15')
css = css.replace('passo 7 de 16', 'passo 7 de 15')
css = css.replace('passo 8 de 16', 'passo 8 de 15')
css = css.replace('passo 9 de 16', 'passo 9 de 15')
css = css.replace('passo 10 de 16', 'passo 10 de 15')
css = css.replace('passo 11 de 16', 'passo 11 de 15')
css = css.replace('passo 12 de 16', 'passo 12 de 15')
css = css.replace('passo 13 de 16', 'passo 13 de 15')
css = css.replace('passo 14 de 16', 'passo 14 de 15')
css = css.replace('passo 15 de 16', 'passo 15 de 15')

# O passo 16 no CSS:
# #contato .sec-tag::before { content: "passo 16 de 16";
# Vamos substituir por algo que faça sentido, ou remover o ::before dele.
css = css.replace('content: "passo 16 de 16";', 'content: "suporte";')
css = css.replace('passo 16 de 16', 'suporte')

with open(path_css, 'w', encoding='utf-8') as f:
    f.write(css)
print('CSS atualizado.')
