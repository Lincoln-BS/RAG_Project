# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Copie o arquivo PDF para o diretório de trabalho no container
COPY Politica_de_Privacidade.pdf /app/Politica_de_Privacidade.pdf

# Defina o comando padrão para iniciar a aplicação
CMD ["python", "app/main.py"]
