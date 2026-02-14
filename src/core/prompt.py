def montar_prompt(system_prompt: str, contexto: str, pergunta: str) -> str:
    return f"""
{system_prompt}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta do usuário:
{pergunta}
"""
