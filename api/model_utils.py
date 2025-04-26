import requests

# Ton URL ngrok obtenu en sortie de Colab
COLAB_URL = "http://ba0f-34-19-75-40.ngrok-free.app"

def generate_commented_code(input_code: str) -> str:
    try:
        resp = requests.post(f"{COLAB_URL}/generate-doc", json={"code": input_code})
        resp.raise_for_status()
        return resp.json().get("output", "// Erreur : pas de clé 'output'")
    except Exception as e:
        return f"// Exception lors de l’appel à Colab : {e}" 