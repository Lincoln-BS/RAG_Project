import os
import uuid
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

# Função para criar e verificar a coleção no ChromaDB
def initialize_chromadb():
    client = chromadb.Client()
    db_name = os.getenv('CHROMADB_NAME', 'policy_db')  # Nome da coleção
    # Cria a coleção se não existir
    if db_name not in client.list_collections():
        print(f"Criando a coleção: {db_name}")
        client.create_collection(name=db_name)
    return client.get_collection(name=db_name)

# Função para armazenar vetores no ChromaDB
def store_vectors(vectors):
    if not vectors:
        print("Erro: Vetores vazios ou None. Não é possível armazenar no ChromaDB.")
        return
    
    print("Inicializando ChromaDB...")
    try:
        collection = initialize_chromadb()
        ids = [str(uuid.uuid4()) for _ in range(len(vectors))]
        print("Armazenando os vetores...")
        collection.add(documents=vectors, ids=ids)
        print("Vetores armazenados com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o ChromaDB ou armazenar os vetores: {e}")

# Função para consultar dados no ChromaDB
def retrieve_data(query):
    print("Consultando ChromaDB...")
    try:
        collection = initialize_chromadb()
        results = collection.query(query_texts=[query])
        return results
    except Exception as e:
        print(f"Erro ao consultar o ChromaDB: {e}")
        return None

