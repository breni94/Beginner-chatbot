# Simple Chatbot Example
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. How can I help you today?")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "exit":
            print("Chatbot: It was nice talking to you. Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")
        elif "what is your name" in user_input:
            print("Chatbot: I'm a simple chatbot. I don't have a fancy name yet!")
        elif "help" in user_input:
            print("Chatbot: Sure! Let me know what you need help with.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you try asking something else?")
            
# Run the chatbot
chatbot()
