# chatbot-llm-streamlit-langchain

Desenvolvimento duma interface gráfica simples em Python que permita que usuários interajam com um modelo de linguagem grande (LLM).

Para esta atividade de desenvolvimento inicial, que é simples, porque o objetivo é didático: mostra a ligação entre Streamlit, entrada do usuário, LangChain/LLM e resposta na tela.

Em empresas, normalmente a interface, a lógica de negócio, a configuração e a chamada ao modelo ficam separadas.

Em produção geralmente há camadas de serviço, logs, tratamento de erro, limite de uso, autenticação, controle de custo e monitoramento. Se o modelo falhar, a aplicação precisa mostrar uma mensagem adequada, não quebrar. Em produção, toda chamada a LLM deve ter limite de tokens, timeout, controle por usuário e registro de uso.

Nesta atividade será mantido o `ChatOpenAI` no código, mas sem chave. Para manter a estrutura sem custo.

Depois, *a posteriori*, para fazer funcionar, sem custo, com IA real, crio que a melhor adaptação seria trocar para **Gemini via API gratuita** ou  **OpenRouter com modelo free** . Isto será uma adaptação deste desenvolvimeto.
