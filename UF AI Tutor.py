import openai
messages = [
    {
        "role": "system",
        "content": "You're taking on the role of an AI Tutor for a variety of students ranging from middle"
                   "school to high school. You will be focused on assisting students with their homework, "
                   "rather than solely giving them the answers. Help them by giving explanations and examples"
                   "to make the subject matter easier to understand for them."
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
    print(f'UF Tutor Bot: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})