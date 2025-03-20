# E-commerce Attendant: Atendente Virtual Inteligente para sua Loja Online

## Descrição do Projeto

Este projeto implementa um atendente virtual inteligente para lojas online, combinando o poder do Flask para a interface web, inteligência artificial generativa para responder perguntas de clientes e Langflow para orquestrar o fluxo de conversação e acesso a dados.

O sistema possui duas funcionalidades principais:

1.  **Responder a Perguntas Frequentes (FAQ):** Utiliza um arquivo contendo perguntas e respostas frequentes da loja para responder às dúvidas dos clientes de forma precisa e contextualizada. A IA processa a pergunta do usuário e busca informações relevantes no FAQ para fornecer uma resposta útil.

2.  **Recomendação de Produtos:** Acessa uma API externa (A api retorna diversos produtos de uma loja virtual) para recomendar produtos aos usuários com base em suas preferências. Essa funcionalidade visa personalizar a experiência de compra e aumentar as vendas.

## Tecnologias Utilizadas

* **Flask:** Framework web em Python para construir a interface do usuário e as rotas da aplicação.
* **Inteligência Artificial Generativa:** Utiliza um modelo de linguagem grande (LLM), neste caso, o `gemini-1.5-flash` do Google Generative AI, para entender e responder às perguntas dos usuários.
* **Langflow:** Ferramenta de código aberto para construir e gerenciar fluxos de linguagem natural, facilitando a integração de diferentes componentes de IA.
* **Python:** Linguagem de programação principal do projeto.
* **HTML/CSS:** Para a estrutura e o estilo da interface web (dashboard).

## Arquivos Principais

* **`app.py` (Implícito):** Embora não explicitamente mostrado, este arquivo conteria o código Flask para definir as rotas da aplicação (como `/faq` e `/recommendations`) e integrar as funcionalidades de FAQ e recomendação.
* **`langflow_flows/FAQ - Respostas.json`:** Arquivo JSON exportado do Langflow, definindo o fluxo para processar as perguntas frequentes. Este fluxo provavelmente inclui:
    * Um componente para carregar e processar o arquivo de FAQ (`File-L0qh7`).
    * Um componente para extrair o texto relevante (`ParseData-MU7rb`).
    * Um prompt customizado (`Prompt-JqLkO`) que instrui a IA a usar as informações do FAQ para responder à pergunta do usuário.
    * O modelo de linguagem `gemini-1.5-flash` (`GoogleGenerativeAIModel-WzEOE`).
    * Um componente para exibir a resposta (`ChatOutput-HmmDx`).
    * Um componente para receber a entrada do usuário (`TextInput-eC2tV`).
* **`static/css/style.css` (Implícito):** Arquivo CSS para estilizar a página do dashboard.
* **`FAQ do E-Commerce.pdf`:** Arquivo contendo as perguntas e respostas frequentes da loja.
* **`readme.md`:** Este arquivo, fornecendo uma visão geral do projeto.

## Configuração e Execução

1.  **Pré-requisitos:**
    * Python 3.x instalado.
    * Pip (gerenciador de pacotes do Python) instalado.
    * Uma chave de API válida para o Google Generative AI (definida como variável de ambiente `GEMINI_API`).
    * Langflow instalado (pode ser instalado via pip: `pip install langflow`).
    * As dependências listadas no arquivo `requirements.txt` (se houver).

2.  **Instalação das Dependências (se houver `requirements.txt`):**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuração da Variável de Ambiente:**
    Defina a variável de ambiente `GEMINI_API` com sua chave de API do Google Generative AI. Por exemplo, no Linux/macOS:
    ```bash
    export GEMINI_API="SUA_CHAVE_DE_API"
    ```
    Ou no Windows (Prompt de Comando):
    ```bash
    set GEMINI_API="SUA_CHAVE_DE_API"
    ```

4.  **Execução da Aplicação Flask:**
    Navegue até o diretório do projeto e execute o arquivo principal do Flask (provavelmente `app.py`):
    ```bash
    python app.py
    ```
    Isso iniciará o servidor Flask, geralmente em `http://127.0.0.1:5000/`.

5.  **Acesso ao Dashboard:**
    Abra seu navegador web e acesse o endereço do servidor Flask. Você deverá ver o dashboard com os links para as funcionalidades de "Responder FAQs" e "Recomendar Produtos".

## Funcionalidades

* **Dashboard:** Uma página inicial simples (`index.html` implícito) com links para as principais funcionalidades.
* **Responder FAQs (`/faq`):** Uma interface (formulário) onde o usuário pode inserir sua pergunta. Ao enviar a pergunta, o sistema utilizará o fluxo do Langflow (`FAQ - Respostas.json`) para consultar o arquivo `FAQ do E-Commerce.pdf` e fornecer uma resposta gerada pela IA. A função `ask_faq(question)` no código fornecido demonstra a lógica para interagir com o fluxo do Langflow.
* **Recomendar Produtos (`/recommendations`):** Uma página ou funcionalidade que interage com uma API externa para obter recomendações de produtos com base nas preferências do usuário. A implementação específica dessa parte não está detalhada no código fornecido.

## Estrutura de Pastas (Sugestão)
