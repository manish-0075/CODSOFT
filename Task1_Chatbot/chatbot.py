print("=" * 50)
print("        WELCOME TO AI CHATBOT")
print("=" * 50)
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thank you for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is CODSOFT AI ChatBot.")

    elif user_input == "who created you":
        print("Bot: I was created as part of a CODSOFT AI Internship project.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user_input == "help":
        print("Bot: You can ask me questions like:")
        print("- Hello")
        print("- How are you")
        print("- What is your name")
        print("- Who created you")
        print("- What can you do")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")