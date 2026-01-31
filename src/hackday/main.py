import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def preguntar_a_phi3(prompt: str) -> str:
    payload = {
        "model": "phi3:mini",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data["response"]

def main():
    print("Hackday funcionando correctamente")

    respuesta = preguntar_a_phi3(
        "Explícame qué es inteligencia artificial en una frase corta"
    )

    print("Respuesta del modelo:")
    print(respuesta)

if __name__ == "__main__":
    main()
