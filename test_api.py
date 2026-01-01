import os
from langchain_google_genai import ChatGoogleGenerativeAI

# PASTE YOUR API KEY HERE
os.environ["GOOGLE_API_KEY"] = "AIzaSyCoxkU59EwZ7yrPZKqOOdKEKoXT4-6CTQc"

# We use the model name exactly as it appeared in your list (without 'models/')
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest")

try:
    print("Sending request to Google...")
    response = llm.invoke("Hello, explain Generative AI in one sentence.")
    print("\n✅ SUCCESS! Response from Google:")
    print(response.content)
except Exception as e:
    print(f"\n❌ Error: {e}")