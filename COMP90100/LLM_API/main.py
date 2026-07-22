import os
import requests
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
  raise ValueError("API key not found. Check your .env file.")
else:
  print("API key found and looks good so far!")

OLLAMA_URL = "http://localhost:11434/api/generate"
#MODEL_NAME = "qwen2.5:7b-instruct"

#API_URL="https://openrouter.ai/api/v1/chat/completions"
#MODEL_NAME = "openrouter/free"

OLLAMA_URL_1 = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma4"


headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type":"application/json"
}

# payload = {
#   "model": f"{MODEL_NAME}",
#   "messages": [
#     {
#       "role": "system",
#       "content": "You are a helpful assistant that explains concepts clearly."
#     },
#     {
#       "role": "user",
#       "content": "Explain what an API is in one sentence."
#     }
#     ],
#     "temperature": 0.3,
#     "max_tokens": 50
# }

# payload = {
#    "model": f"{MODEL_NAME}",
#    "messages": [
#       {
#          "role": "user", 
#          "content": "Hello! Explain what an API is in one sentence."
#       }
#     ] 
#    }

payload = [
      {
         "role": "user", 
         "content": "Hello! Explain what an API is in one sentence."
      }
    ] 
   


#response = requests.post(API_URL, headers=headers, json=payload)
#response = requests.post(OLLAMA_URL_1, json=payload)
response = chat(MODEL_NAME, payload)

# if response.status_code != 200:
#     print("Request failed:")
#     print(response.text)
#     exit()


data = response

# Print the full response for debugging
print("Full response:")
print(data)


print("\n------")
print("------")
print("------\n")

# Extract and print the generated text from the response
#generated_text_content = data["choices"][0]["message"]["content"]
#generated_text_resoning = data["choices"][0]["message"]["reasoning"]

generated_text_content = data["message"]["content"]
#generated_text_resoning = data["message"]["reasoning"]

generated_model_name = data["model"]

print("Model name:")
print(generated_model_name)

print("Model response:")
print(generated_text_content)

# print("Model resosning:")
# print(generated_text_resoning)
