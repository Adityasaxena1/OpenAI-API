import common


while True:
    user_input = input("Ask me anything: ")

    if user_input.lower() == "stop":
        break
    else:
        common.get_openai_response(user_input)



