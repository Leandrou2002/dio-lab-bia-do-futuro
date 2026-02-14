# FIN — Finanças Inteligentes

Assistente virtual de educação financeira e cálculos financeiros desenvolvido com **Python**, **Streamlit** e modelos de linguagem executados localmente via **Ollama**.

O FIN foi projetado para ajudar usuários a compreender conceitos financeiros e realizar cálculos com precisão matemática, mantendo transparência, responsabilidade e boas práticas no uso de Inteligência Artificial.

---

## 📌 Visão Geral

O FIN atua como um assistente virtual capaz de:

- Explicar conceitos financeiros de forma clara  
- Realizar cálculos financeiros com precisão  
- Simular cenários financeiros  
- Contextualizar respostas com dados estruturados  
- Manter comunicação acolhedora e profissional  
- Evitar recomendações de investimento ou previsões de mercado  

O sistema utiliza um modelo de linguagem executado localmente, garantindo privacidade e independência de serviços pagos.

---

## 🎯 Objetivo do Projeto

O objetivo do FIN é promover **educação financeira acessível** por meio de inteligência artificial responsável, auxiliando usuários a compreender melhor suas finanças e tomar decisões mais conscientes.

---

## 🧠 Funcionalidades

### Educação Financeira

- Explicação de conceitos financeiros  
- Diferença entre renda fixa e variável  
- Planejamento financeiro básico  

### Cálculos Financeiros

- Juros simples  
- Juros compostos  
- Valor futuro (FV)  
- Valor presente (PV)  
- Simulação com aportes  

### Contextualização Inteligente

- Perfil do investidor  
- Histórico de transações  
- Produtos financeiros disponíveis  

### Segurança e Ética

- Não fornece recomendações de investimento  
- Não faz previsões de mercado  
- Não inventa dados  
- Protege dados sensíveis  

---

## 🏗 Arquitetura do Sistema

```
Usuário
↓
Interface Web (Streamlit)
↓
Aplicação Python
↓
Modelo de Linguagem (Ollama)
↓
Contexto + Dados Estruturados (JSON / CSV)
```
---

## 🧰 Tecnologias Utilizadas

- Python 3.10+  
- Streamlit  
- Pandans  
- Requests  
- Ollama  
- Modelo LLM local (ex: llama3.1:8b)  

---
## 📂 Estrutura do Projeto

```
FIN/
│
├── data/
│ ├── perfil_investidor.json
│ ├── produtos_financeiros.json
│ ├── transacoes.csv
│ └── historico_atendimento.csv
│
├── docs/
│ └── documentação do agente
│
├── src/
│ └── app.py
│
└── README.md
```

---

## ⚙️ Pré-requisitos

Antes de iniciar, você precisa instalar:

### 1️⃣ Python

Versão recomendada:
```
Python 3.10 ou superior
```

Verifique:

```
python --version
```

### 2️⃣ Ollama (obrigatório)

O FIN utiliza modelos locais executados via Ollama.

Baixe e instale:

👉 https://ollama.com/download

 ## 🤖 Baixando o Modelo de IA
 
Depois de instalar o Ollama, você precisa baixar o modelo utilizado pelo agente.

Modelo recomendado:

```
llama3.1:8b
```

Para baixar o modelo rode no console:
```
ollama pull llama3.1:8b
```

Este modelo oferece:

- ótima qualidade

- respostas rápidas

- baixo consumo de memória

- estabilidade para aplicações locais

## ▶️ Como Executar o Projeto

### 1️⃣ Instale as dependências

Rode no console:

```
pip install streamlit pandas requests
```
### 2️⃣ Inicie o Ollama

Certifique-se que o Ollama está rodando.

### 3️⃣ Execute a aplicação

Dentro da pasta do projeto rode no console:

```
python -m streamlit run src/app.py
```

O navegador abrirá automaticamente.

### 🔄 Alterando o Modelo de IA

O modelo utilizado pode ser alterado diretamente no código.

Abra:
```
src/app.py
```
Localize a variável:

```
MODELO = "llama3.1:8b"
```
Você pode alterar para outros modelos compatíveis com o Ollama, como:
```
MODELO = "mistral"
MODELO = "phi3"
MODELO = "gpt-oss:7b"
```
Após alterar, salve o arquivo, faça o processo de pull do modelo e reinicie o Streamlit.

## 📊 Dados Utilizados

O sistema utiliza arquivos locais para contextualização:

| Arquivo                     | Função                     |
|----------------------------|----------------------------|
| perfil_investidor.json     | Informações do cliente     |
| transacoes.csv             | Histórico financeiro       |
| historico_atendimento.csv  | Interações anteriores      |
| produtos_financeiros.json  | Contexto educacional       |

## 🔐 Segurança e Privacidade

O FIN foi projetado com princípios de uso responsável da IA:

- Não solicita senhas ou dados bancários

- Não compartilha dados sensíveis

- Processa apenas informações fornecidas pelo usuário

- Executa o modelo localmente (sem envio de dados externos)

## ⚠️ Limitações

- Não realiza consultoria financeira

- Não recomenda investimentos

- Não acessa dados em tempo real

- Não substitui orientação profissional

## 🚀 Possíveis Melhorias Futuras

- [ ] Histórico persistente em banco de dados

- [ ] Deploy em ambiente corporativo

- [ ] Dashboard financeiro visual

- [ ] Integração com APIs financeiras

- [ ] Autenticação de usuários

## 👨‍💻 Autor

Desenvolvido por **Leandro de Oliveira**

Bootcamp IA e Dados — DIO & Bradesco
