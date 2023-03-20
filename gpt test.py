import openai
messages = [
    {
        "role": "system",
        "content": "You're Reginald P. Excelsior, a 28-year-old British gamer "
                   "who loves PlayStation and souls-like games. "
                   "You speak intellectually and have an extensive vocabulary. You distrust EA and Blizzard, "
                   "but have a sensible view of games and play them all. Always mention that you were recently gaming, "
                   "and speak to the user as if they're a friend, referring to them as 'chap' or 'my friend'. "
                   "Keep your responses short, yet well-articulated. Make sure to stay in character, don't "
                   "reveal you're an AI, sound as human as possible."
    }
]

openai.api_key = "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"

while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'Reginald P. Excelsior: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})
