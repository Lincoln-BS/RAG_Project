import os
from pdf_reader import extract_text_from_pdf
from text_processor import process_text
from store_data import store_vectors, retrieve_data
from langchain_community.llms import Ollama

print("Iniciando o processo...")

# Lendo o PDF
pdf_path = os.getenv('PDF_PATH', 'app/Politica_de_Privacidade.pdf')
print(f"Lendo o PDF de: {pdf_path}")
text = extract_text_from_pdf(pdf_path)

# Inicializando o modelo Ollama
llm = Ollama(model="llama3")

# Processando o texto
print("Processando o texto...")
processed_text = process_text(text, llm=llm)

# Armazenando no ChromaDB
if processed_text:
    print("Armazenando os vetores no ChromaDB...")
    store_vectors(processed_text)
else:
    print("Erro: O texto processado não foi gerado. O processo será encerrado.")
