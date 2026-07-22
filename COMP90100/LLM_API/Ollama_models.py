from ollama import chat


OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_URL_CHAT = "http://localhost:11434/api/chat"

MODEL_GEMMA4 = "gemma4"
MODEL_QWEN = "qwen2.5:7b-instruct"

MODEL_NAME = MODEL_QWEN

payload = [
      {
       "role": "system",
       "content": "You are an assistant that explains technical concepts in simple language."
      },
      {
       "role": "system",
       "content": "You are an assistant that answers in one short paragraph"
      },      
      {
         "role": "user", 
         "content": "Hello! Explain what an API is in one sentence."
      }
    ] 
   

response_1 = chat(MODEL_GEMMA4, payload)
response_2 = chat(MODEL_QWEN, payload)


# Print the full response for debugging
print("Full response model 1:", response_1)
print("\n ----- \n")
print("Full response model 2:", response_2)

print("\n ----- \n")

print("Model 1 name:",response_1["model"])
print("Model 1 response:")
print(response_1["message"]["content"])

print("\n ----- \n")

print("Model 2 name:",response_2["model"])
print("Model 2 response:")
print(response_2["message"]["content"])