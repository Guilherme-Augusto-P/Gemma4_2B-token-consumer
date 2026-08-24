import requests
import json
import time

def stream_chat(messages, model_name = "gemma:2b"):

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": model_name,
        "messages": messages,
        "Stream": True
    }

    start_time = time.time()
    response = requests.post(url, json=payload, stream=True)

    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode('utf-8'))

            if "message" in chunk and "content" in chunk["message"]:
                yield {
                    "type": "text",
                    "content": chunk["message"]["content"]
                }

            if chunk.get("done") == True:
                end_time = time.time()
                yield {
                    "type": "metrics",
                    "prompt_tokens": chunk.get("prompt_eval_count", 0),
                    "completion_tokens": chunk.get("eval_count", 0),
                    "duration": end_time - start_time
                }