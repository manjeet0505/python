from openai import OpenAI

key = "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"

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
