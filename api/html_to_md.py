# api/html_to_md.py
from bs4 import BeautifulSoup
import markdownify
import os
import shutil

def convert_html_to_markdown(html_content: str, html_output_dir: str, target_docs_dir: str) -> str:
    """
    - html_content     : le contenu brut de index.html
    - html_output_dir  : dossier '…/output/html' généré par Doxygen
    - target_docs_dir  : dossier temporaire où on va copier les assets
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # 1) On cherche le div principal contenant la doc
    content_div = soup.find("div", id="doc-content") or soup.find("div", class_="contents")
    if not content_div:
        # fallback : on prend tout le body
        content_div = soup.body

    # 2) Copier les images (diagrammes .svg) et réécrire leurs URLs
    assets_dir = os.path.join(target_docs_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    for img in content_div.find_all("img"):
        src = img.get("src")
        if not src:
            continue
        # src peut être relatif, on prend juste le nom de fichier
        base = os.path.basename(src)
        src_path = os.path.join(html_output_dir, src)
        dst_path = os.path.join(assets_dir, base)
        try:
            shutil.copyfile(src_path, dst_path)
            # on change l'URL dans le HTML pour pointer vers assets/
            img["src"] = f"assets/{base}"
        except FileNotFoundError:
            # si l'image est introuvable, on la laisse telle quelle
            pass

    # 3) Transformer le contenu HTML nettoyé en Markdown
    #    on limite le scope à content_div
    md = markdownify.markdownify(str(content_div), heading_style="ATX")

    # 4) Supprimer d'éventuels liens vides
    md = md.replace("[]()", "")

    return md
