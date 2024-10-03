import openai  

# Substitua pela sua chave API  
chave_api = "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"  

openai.api_key = chave_api  

def pergunta_cliente(mensagem):  
    resposta = openai.ChatCompletion.create(  
        model="gpt-3.5-turbo",  # ou "gpt-4" se você tiver acesso  
        messages=[  
            {"role": "user", "content": mensagem}  
        ],  
        max_tokens=150,  # Quantidade máxima de tokens na resposta  
        temperature=0.7  # Grau de criatividade nas respostas  
    )  
    return resposta.choices[0].message['content'].strip()  

# Exemplo de interação  
if __name__ == "__main__":  
    while True:  
        pergunta = input("Pergunte sobre nossos produtos: ")  
        if pergunta.lower() == 'sair':  
            break  
        resposta = pergunta_cliente(pergunta)  
        print("Resposta do Bot: ", resposta)