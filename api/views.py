import shutil
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from .model_utils import generate_commented_code
from .html_to_md import convert_html_to_markdown
import tempfile
import subprocess
import os
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import re
from django.conf import settings
def extract_class_name(code: str) -> str:
    match = re.search(r'class\s+(\w+)', code)
    return match.group(1) if match else "MyClass"

def generate_doxygen_doc(commented_code: str, request) -> tuple[str, str, str]:
    with tempfile.TemporaryDirectory() as tempdir:
        class_name = extract_class_name(commented_code)
        code_file = os.path.join(tempdir, f"{class_name}.java")
        doxyfile = os.path.join(tempdir, "Doxyfile")
        output_dir = os.path.join(tempdir, "output")
        html_dir = os.path.join(output_dir, "html")

        with open(code_file, "w") as f:
            f.write(commented_code)
        doxyfile_content = f"""
# Projet
PROJECT_NAME           = "Generated Documentation"
OUTPUT_DIRECTORY       = {output_dir}
INPUT                  = {tempdir}
FILE_PATTERNS          = *.java
RECURSIVE              = YES

# Génération de sortie
GENERATE_HTML          = YES
GENERATE_LATEX         = NO
GENERATE_XML           = NO
HTML_OUTPUT            = html
GENERATE_TREEVIEW      = YES
HTML_DYNAMIC_SECTIONS  = YES
DISABLE_INDEX          = NO
FULL_PATH_NAMES        = NO

# Extraction
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = YES
EXTRACT_STATIC         = YES
EXTRACT_LOCAL_CLASSES  = YES
EXTRACT_ANON_NSPACES   = YES
EXTRACT_PACKAGE        = YES

# Graphiques
HAVE_DOT               = YES
DOT_NUM_THREADS        = 2
COLLABORATION_GRAPH    = YES
CALL_GRAPH             = YES
CALLER_GRAPH           = YES
UML_LOOK               = YES
DOT_IMAGE_FORMAT       = svg
INTERACTIVE_SVG        = YES
DOT_PATH               = 
DOTFILE_DIRS           =

# Documentation de code
JAVADOC_AUTOBRIEF      = YES
MULTILINE_CPP_IS_BRIEF = YES
INLINE_INFO            = YES
INHERIT_DOCS           = YES

# Affichage
QUIET                  = YES
TAB_SIZE               = 4
"""

        with open(doxyfile, "w") as f:
            f.write(doxyfile_content)

        # Vérification que Doxygen est installé
        try:
            subprocess.run(["doxygen", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            raise RuntimeError("Doxygen n'est pas installé ou n'est pas trouvé dans le PATH.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Erreur lors de la vérification de Doxygen : {e}")

        # Exécution de Doxygen
        subprocess.run(["doxygen", doxyfile], check=True)
        target = os.path.join(settings.MEDIA_ROOT, "docs")  # NOUVEAU chemin cible complet

        index_file = os.path.join(html_dir, "index.html")
        final_path = None  

        if os.path.exists(html_dir) and os.path.exists(index_file):
            shutil.rmtree(target, ignore_errors=True)
            shutil.copytree(html_dir, target)
            with open(index_file, "r") as f:
                html_content = f.read()
            final_path = os.path.join(target, "index.html")
        else:
            html_content = "<p>Aucune documentation générée</p>"

        markdown = convert_html_to_markdown(
            html_content,
            html_output_dir=html_dir,
            target_docs_dir=tempdir
        )

        return markdown, html_content, final_path

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_code(request):
    print("Requête reçue !")
    print("Utilisateur authentifié :", request.user)
    print("Corps de la requête :", request.data)

    code = request.data.get('code', '')
    if not code:
        return Response({'error': 'Code non fourni'}, status=400)

    commented_code = generate_commented_code(code)
    markdown, html_data, file_path = generate_doxygen_doc(commented_code, request)

    if file_path:
        full_url = request.build_absolute_uri('/media/docs/index.html')
    else:
        full_url = None

    return Response({
        'commented_code': commented_code,
        'documentation_md': markdown,
        'documentation_html': html_data,
        'documentation_url': full_url
    }, status=200)
