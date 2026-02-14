import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"

class LLMError(Exception):
    pass

def perguntar_llm(prompt: str) -> str:
    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        r.raise_for_status()
        data = r.json()

        if "response" not in data:
            raise LLMError("Resposta inválida do modelo")

        return data["response"]

    except requests.exceptions.Timeout:
        raise LLMError("O modelo demorou para responder")

    except requests.exceptions.ConnectionError:
        raise LLMError("O Ollama não está em execução")

    except Exception:
        raise LLMError("Erro inesperado ao consultar o modelo")
