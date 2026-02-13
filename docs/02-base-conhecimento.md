# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Manter continuidade das interações e preservar contexto recente |
| `perfil_investidor.json` | JSON | Personalizar respostas com base no perfil, objetivo e patrimônio do cliente |
| `produtos_financeiros.json` | JSON | Explicar conceitos relacionados a produtos financeiros de forma educativa |
| `transacoes.csv` | CSV | Analisar padrões de gastos e contextualizar explicações financeiras |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram mantidos como base estrutural do projeto, porém foram organizados e ajustados para garantir:

- Padronização de codificação em UTF-8  
- Consistência de nomenclatura dos campos  
- Melhor organização para leitura via Python  
- Compatibilidade com o contexto enviado ao modelo  

Não foram adicionados dados externos ou datasets públicos. O projeto utiliza exclusivamente os arquivos fornecidos no desafio.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados no início da sessão da aplicação utilizando leitura explícita com codificação UTF-8.

Os dados são convertidos para estruturas Python (dicionários e listas) e permanecem em memória durante a execução da aplicação Streamlit.

Exemplo de carregamento:

```python
perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
transacoes = pd.read_csv("./data/transacoes.csv")

```
## Como os dados são usados no prompt?

> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não substituem o System Prompt, mas são incorporados dinamicamente ao contexto enviado ao modelo.

A estrutura da requisição ao modelo contém:

1. System Prompt com regras comportamentais e anti-alucinação

2. Dados estruturados do cliente (perfil, patrimônio, objetivo)

3. Informações relevantes das transações, quando necessário

4. Pergunta atual do usuário

Os dados são formatados em texto estruturado antes de serem enviados ao modelo, garantindo clareza e controle de contexto.

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Objetivo Principal: Construir reserva de emergência
- Patrimônio Total: R$ 25.000
- Reserva de Emergência: R$ 8.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Restaurante - R$ 120

Pergunta do usuário:
"Quanto preciso investir por mês para atingir R$ 50.000 em 3 anos?"
```
