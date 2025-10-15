def chatbot():
    while True:
        user = input("You: ").lower()
        if 'hello' in user:
            print("Bot: Hi there!")
        elif 'how are you' in user:
            print("Bot: I'm good, thanks!")
        elif 'bye' in user:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I didn't understand that.")

chatbot()
