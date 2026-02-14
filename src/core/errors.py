def erro_amigavel(msg: str) -> str:
    if "Ollama" in msg:
        return "⚠️ O assistente está offline no momento. Verifique se o Ollama está em execução."

    if "demorou" in msg:
        return "⏳ O assistente está demorando mais que o normal. Tente novamente."

    return "❌ Não foi possível processar sua solicitação agora. Tente mais tarde."