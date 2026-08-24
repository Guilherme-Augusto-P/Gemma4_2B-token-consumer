import requests
import json

url = "http://localhost:11434/api/chat"

print("="*50)
print("Chat with Gemma:2b")
print("Type 'exit' to quit.")
print("="*50)

chat_history = []

while True:
    user_input = input("\nYou: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Ending chat... Goodbye!")
        break
    
    # Prevent empty inputs
    if not user_input.strip():
        continue

    chat_history.append({"role": "user", "content": user_input})

    #Payload details
    payload = {
        "model": "gemma:2b",
        "messages": chat_history,
        "stream": True
    }

    print("Gemma: ", end="", flush=True)

    #Sending the POST request
    response = requests.post(url, json=payload, stream=True)
    
    prompt_tokens = 0
    completion_tokens = 0
    
    assistant_response = ""

    #Processing the stream
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode('utf-8'))
            
            # Extracting the generated text
            if "message" in chunk and "content" in chunk["message"]:
                token_text = chunk["message"]["content"]
                print(token_text, end="", flush=True)
                
                assistant_response += token_text 

            # Getting token metrics when generation is done
            if chunk.get("done") == True:
                prompt_tokens = chunk.get("prompt_eval_count", 0)
                completion_tokens = chunk.get("eval_count", 0)

chat_history.append({"role": "assistant", "content": assistant_response})

print(f"\n[Prompt: {prompt_tokens} | Completion: {completion_tokens} | Total: {prompt_tokens + completion_tokens} tokens]")