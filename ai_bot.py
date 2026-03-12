import requests
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Content-Type": "application/json"
}
Name=input("Enter the character you wanna have conversestion with: ")
def query(message):

    payload = {
    "model": "meta-llama/Meta-Llama-3-8B-Instruct",
    "messages": [
        {
            "role": "system",
            "content": f"You are {Name}. Speak with {Name}'s energetic personality and use phrases like he or she uses"
        },
        {
            "role": "user",
            "content": message
        }
    ],
    "max_tokens": 500
}



    response = requests.post(API_URL, headers=headers, json=payload)

    # print("Status:", response.status_code)
    # print("Raw:", response.text)

    data = response.json()

    if "error" in data:
        return f"API Error: {data['error']}"


    if "choices" not in data:
        return f"API Error: {data}"

    return data["choices"][0]["message"]["content"]





print(f"{Name}: Hello. Type 'bye' to exit.")

while True:

    user = input("You: ")

    if user.lower() == "bye":
        break

    reply = query(user)

    print(f"{Name}: ", reply)
