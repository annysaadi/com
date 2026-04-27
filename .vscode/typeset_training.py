import re

def typeset(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Ellipsis
    html = html.replace("...", "…")
    html = html.replace(" . . . ", " … ")

    # 2. Smart quotes for specific known phrases
    quotes = [
        "Centro de Lives", 
        "Cadastro de Informações Bancárias", 
        "Ver Relatório de Ganho", 
        "Descobrir", 
        "moedas acumuladas", 
        "Faça mais vídeos", 
        "Avisos de Sistema"
    ]
    for q in quotes:
        html = html.replace(f'"{q}"', f'“{q}”')

    # 3. Widow/Orphan control
    # Replace the space before the last word (up to 15 chars) before a closing tag
    pattern = re.compile(r'( )([A-Za-zÀ-ÿ0-9.,!?…;:\'"”’\-]{1,15})(</(?:p|h[1-6]|li|span|div|a|em|strong)>)')
    
    # Run it a couple of times to catch nested scenarios
    for _ in range(3):
        html = pattern.sub(lambda m: "&nbsp;" + m.group(2) + m.group(3), html)

    # Some manual touch-ups for where tags might interfere
    html = html.replace(" o<br />", " o<br/>")  # normalize br
    html = html.replace(" o<br/>", "&nbsp;o<br/>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    typeset("c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/.vscode/training_work.html")
