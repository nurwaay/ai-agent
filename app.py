def agent_response(message):
    if not message.strip():
        return "Please enter a message."

    if message.lower() == "help":
        return "Available commands: help"

    return f"AI Agent received: {message}"


user_message = input("Enter your request: ")
print(agent_response(user_message))