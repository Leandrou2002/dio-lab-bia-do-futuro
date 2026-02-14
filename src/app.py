# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
                       
import json
import pandas as pd
import streamlit as st

from core.system_prompt import SYSTEM_PROMPT
from core.context import montar_contexto
from core.prompt import montar_prompt
from services.llm_service import perguntar_llm, LLMError
from core.errors import erro_amigavel

# ===== Carregar dados =====
perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json", encoding="utf-8"))

contexto = montar_contexto(
    perfil,
    transacoes,
    historico,
    produtos
)

st.set_page_config(
    page_title="FIN - Finanças Inteligentes",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

.stChatMessage {
    padding: 0.75rem 1rem;
    border-radius: 14px;
    margin-bottom: 0.75rem;
    max-width: 85%;
    line-height: 1.6;
    font-size: 15px;
}

.stChatMessage.user {
    background-color: #1e293b;
    margin-left: auto;
}

.stChatMessage.assistant {
    background-color: #020617;
    border: 1px solid #1e293b;
    margin-right: auto;
}

textarea {
    border-radius: 12px !important;
}
            
h1 {
    font-weight: 600;
    letter-spacing: 0.5px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## FIN")
    st.caption("Finanças Inteligentes")
    st.divider()

    st.markdown("### Cliente")
    st.write(f"**Nome:** {perfil['nome']}")
    st.write(f"**Idade:** {perfil['idade']} anos")

    st.divider()

    st.markdown("### Perfil do Investidor")
    st.write(perfil["perfil_investidor"].capitalize())

    st.divider()

    st.markdown("### Objetivo Principal")
    st.write(perfil["objetivo_principal"])

    st.divider()

    st.markdown("### Resumo Financeiro")
    st.metric(
        "Patrimônio Total",
        f"R$ {perfil['patrimonio_total']:,.2f}"
    )
    st.metric(
        "Reserva de Emergência",
        f"R$ {perfil['reserva_emergencia_atual']:,.2f}"
    )

    st.divider()
    st.caption("Dados tratados com confidencialidade")


st.title("FIN - Finanças Inteligentes")

if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    st.chat_message(msg["role"]).write(msg["content"])

if pergunta := st.chat_input("Digite sua dúvida financeira..."):
    st.session_state.chat.append({
        "role": "user",
        "content": pergunta
    })

    with st.spinner("FIN está analisando sua solicitação..."):
        try:
            prompt_final = montar_prompt(
                SYSTEM_PROMPT,
                contexto,
                pergunta
            )

            resposta = perguntar_llm(prompt_final)

            st.session_state.chat.append({
                "role": "assistant",
                "content": resposta
            })

        except LLMError as e:
            st.session_state.chat.append({
                "role": "assistant",
                "content": erro_amigavel(str(e))
            })

    st.rerun()
