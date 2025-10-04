from google import genai

apikey = genai.Client(api_key="YOUR_API_KEY_HERE")
is_running = True

def callapi():
    user_input = input("type your question:\n")
    if user_input == "quit":
        return False
    else:
        print("Thinking...\n")
        response = apikey.models.generate_content(
            model="gemini-2.5-flash", contents=user_input
        )
        print(response.text + "\n")
        return True

while is_running:
    is_running = callapi()