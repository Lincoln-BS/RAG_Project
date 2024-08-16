# Starsoft RAG Challenge

**Desafio realizado por:** Lincoln Bonifácio Souza

## Descrição

Este projeto é uma solução para o desafio técnico de Recuperação Aumentada de Conhecimento (RAG) da Starsoft. A aplicação desenvolvida processa e armazena informações extraídas de um documento PDF (Política de Privacidade), utilizando diversas tecnologias de inteligência artificial e armazenamento de vetores.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento da aplicação.
- **LangChain**: Framework para construção de aplicações com base em IA.
- **ChromaDB**: Banco de dados especializado em armazenamento de vetores.
- **Ollama**: Ferramenta para execução e gerenciamento de modelos de linguagem grandes (LLMs) localmente.
- **Docker**: Para contêinerização da aplicação.
- **Docker Compose**: Para orquestração dos serviços necessários.

## Funcionalidades

- Leitura e extração de texto de um PDF (Política de Privacidade).
- Processamento do texto extraído utilizando o framework LangChain.
- Armazenamento dos vetores resultantes do processamento no ChromaDB.
- Recuperação e consulta dos dados armazenados.

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

### Passos para Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Lincoln-BS/starsoft-rag-challenge.git
   cd starsoft-rag-challenge

2. **Construa e inicie os contêineres:**
    
    docker-compose up --build
Isso vai baixar as imagens necessárias, instalar as dependências e iniciar a aplicação.

3. **Acesse a aplicação:**
 
A aplicação estará disponível localmente na porta 5000. Para acessar, abra o navegador e vá até http://localhost:5000.

4. **Finalizando:**
Para parar os contêineres, use:
    docker-compose down


**Estrutura do Projeto**

**app/:** Contém os scripts principais para leitura, processamento e armazenamento de dados.
    **main.py:** Script principal que coordena o fluxo da aplicação.
    **pdf_reader.py:** Lê e extrai o texto do PDF.
    **text_processor.py:** Processa o texto utilizando LangChain.
    **store_data.py:** Armazena e recupera dados no ChromaDB.
**Dockerfile:** Configuração do Docker para construir a imagem da aplicação.
**docker-compose.yml:** Configuração do Docker Compose para orquestração dos serviços.
**Politica_de_Privacidade.pdf:** PDF utilizado para extração e processamento de texto.
**requirements.txt:** Dependências Python necessárias para a execução do projeto.
**Contribuição**
Este projeto foi desenvolvido como parte de um teste técnico. No momento, não aceitamos contribuições externas.

**Licença**
Este projeto é de código fechado, desenvolvido exclusivamente para o desafio técnico da Starsoft.

**Desenvolvido por Lincoln Bonifácio Souza**