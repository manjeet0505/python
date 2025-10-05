from openai import OpenAI
import os

key = os.getenv("OPENAI_API_KEY")

messages = []

client = OpenAI(api_key=key)

def completion(message):
    global messages
    messages.append({"role": "user", "content": message})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )

    assistant_reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_reply})

    print(assistant_reply)


if __name__ == "__main__":
    user_question = input("Hi there! What would you like to ask? ")
    completion(user_question)
