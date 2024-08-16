from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def process_text(text, llm):
    template = "Resuma o seguinte texto: {text}"
    prompt = PromptTemplate(input_variables=["text"], template=template)
    
    # Usando LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    try:
        print(f"Texto a ser processado: {text[:200]}...")  # Exibir os primeiros 200 caracteres do texto
        
        print("Executando a cadeia de processamento...")
        processed_text = chain.invoke({"text": text})
        print("Texto processado com sucesso:", processed_text)
        
        # Convertendo o texto processado para uma lista, se necessário
        if isinstance(processed_text, dict) and 'text' in processed_text:
            processed_text = [processed_text['text']]
        
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")
        processed_text = None
    
    return processed_text
