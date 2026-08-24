import requests
import json

#Ollama Server
url = "http://localhost:11434/api/generate"

print("Chat com Gemma:2b (local)")
print("Digite 'sair' a qualquer momento para encerrar.")

while True:

    #input
    prompt_texto = input("\nVocê: ")

    if prompt_texto.lower() == "sair":
        print("Encerrando o chat... Até mais!")
        break

    if not prompt_texto.strip():
        continue

    #Model Name
    #Prompt used
    #Server
    payload = {
        "model": "gemma:2b", 
        "prompt": prompt_texto,
        "stream": True
    }

    print("Gemma: ", end="", flush=True)

    #Requisition HTTP(POST)
    resposta = requests.post(url, json=payload, stream=True)

    tokens_entrada = 0
    tokens_saida = 0

    #Loop that captures the words
    for linha in resposta.iter_lines():
        if linha:
            #translate from bytes to dictionary
            fragmento = json.loads(linha.decode('utf-8'))

            #Pick the generated word, and print on screen
            palavra = fragmento.get("response", "")
            print(palavra, end="", flush=True)

            #When the AI had the job done, print "done"
            if fragmento.get("done") == True:
                tokens_entrada = fragmento.get("prompt_eval_count", 0)
                tokens_saida = fragmento.get("eval_count", 0)

print(f"\n[Prompt: {tokens_entrada}, Resposta: {tokens_saida}, Total: {tokens_entrada + tokens_saida} tokens]")