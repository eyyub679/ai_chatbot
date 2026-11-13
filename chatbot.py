from openai import OpenAI
import os
from dotenv import load_dotenv
def main():
    load_dotenv()
    api_key=os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY not found. Please set it in your .env file.")
        return
    client=OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    context=[{"role":"system","content":"You are a helpful assistant."}]
    print("Enter \"q\" to exit")
    while True:
        prompt=input("\nYou: ")
        if prompt=="q":
            print("Shutting down...")
            break
        context.append({"role":"user","content":prompt})
        response=client.chat.completions.create(
            model="nvidia/nemotron-3-ultra-550b-a55b:free",
            messages=context,
            stream=True
        ) # type: ignore
        # answer=response.choices[0].message.content, now response is a generator
        answer=""
        print()
        for chunk in response:
            delta=chunk.choices[0].delta.content if chunk.choices else None
            if delta:
                answer+=delta
                print(delta,end="",flush=True)
        context.append({"role":"assistant","content":answer})
if __name__ == "__main__":
    main()
