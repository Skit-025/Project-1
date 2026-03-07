# Simple Python Chatbot

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Chatbot: Hello! How can I help you?")
    
    elif "how are you" in user_input:
        print("Chatbot: I am functioning normally.")
    
    elif "your name" in user_input:
        print("Chatbot: I am a simple Python chatbot.")
    
    elif "help" in user_input:
        print("Chatbot: You can ask me simple questions.")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    
    else:
        print("Chatbot: I don't understand that.")
