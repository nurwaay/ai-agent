def agent_response(message):
    return f"AI Agent received: {message}"


user_message = input("Введите запрос: ")
print(agent_response(user_message))