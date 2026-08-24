from llm_api import stream_chat

def main():
    print("=" * 50)
    print("Chat with Gemma:2b")
    print("Type 'exit' to quit.")
    print("=" * 50)

    chat_history = []

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Ending chat... Goodbye!")
            break

        if not user_input.strip():
            continue

        chat_history.append({"role": "user", "content": user_input})

        print("Gemma: ", end="", flush=True)

        assistant_response = ""
        prompt_tokens = 0
        completion_tokens = 0
        duration = 0

        for data in stream_chat(chat_history) :
            if data["type"] == "text":
                text_chunk = data["content"]
                print(text_chunk, end="", flush=True)
                assistant_response += text_chunk

            elif data["type"] == "metrics":
                prompt_tokens = data["prompt_tokens"]
                completion_tokens = data["completion_tokens"]
                duration = data["duration"]

        chat_history.append({"role": "assistant", "content": assistant_response})

        tokens_per_second = completion_tokens / duration if duration > 0 else 0

        print(f"\n\n[Metrics - Prompt: {prompt_tokens} | Completion: {completion_tokens} | Time: {duration:.2f}s | Speed: {tokens_per_second:.2f} tokens/s]")

if __name__ == "__main__":
    main()