# Basic Chatbot

def chatbot():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi! How can I help you?")
        elif user_input == "how are you":
            print("Bot: I am fine, thank you!")
        elif user_input == "what is your name":
            print("Bot: I am a simple Python chatbot.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()