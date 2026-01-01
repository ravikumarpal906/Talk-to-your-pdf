import os
import google.generativeai as genai

# PASTE YOUR API KEY HERE
os.environ["GOOGLE_API_KEY"] = "AIzaSyCoxkU59EwZ7yrPZKqOOdKEKoXT4-6CTQc" # <--- Put your actual key here

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Checking available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Found: {m.name}")
except Exception as e:
    print(f"Error: {e}")