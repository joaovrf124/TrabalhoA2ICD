from openai import OpenAI

prompt = []
client = OpenAI(api_key="chave")

def addInfo(comments, movie):
        i = 0
        while i < len(comments):
            if(i % 10 == 0):
                prompt.append({"role":"user", "content": f"A seguir estão os commentarios do filme {movie}: {comments[i - 9 :i]}. Ache padrões de satisfação do cliente e áreas para melhoria."})
                openIa(prompt)
            elif(i == len(comments)):      
                prompt.append({"role":"user", "content": f"A seguir estão os commentarios do filme {movie}: {comments[int(i / 10) + 1 : i]}. Ache padrões de satisfação do cliente e áreas para melhoria."})
                openIa(prompt)
            i = i + 1

def openIa(prompt):
    response = client.chat.completions.create(
    messages = prompt,
    model = "gpt-3.5-turbo-0125",
    max_tokens = 1000,
    temperature = 1
    )
    print(23 / 10)
    prompt.append({"role":"assistant","content":response.choices[0].message.content})
