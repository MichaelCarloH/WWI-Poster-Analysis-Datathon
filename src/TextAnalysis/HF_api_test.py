import os
import requests

# Load API key from environment
HF_API_KEY = os.getenv("HF_API_KEY")  # Should be set in your system

if not HF_API_KEY:
    raise ValueError("API key not found. Make sure you've set HF_API_KEY in your environment.")

# Choose a test model (BART for text summarization)
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Send a simple test request
response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("✅ Hugging Face API key is working!")
else:
    print(f"❌ Error: {response.status_code}, {response.json()}")
