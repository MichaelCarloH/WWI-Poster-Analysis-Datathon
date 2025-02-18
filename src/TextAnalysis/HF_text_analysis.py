import os
import re
import json
from huggingface_hub import InferenceClient
import pandas as pd

# Load API Key
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("API key not found. Make sure you've set HF_API_KEY.")

# Path to the text file
file_path = "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984787_1_DIGI_0035_00001_VIEW_MAIN.jpg.txt"

# Read the text file
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# Insert text into the prompt
prompt = f'''
You are a historical text analyst. Your task is to analyze WW1 propaganda text by:
1. Correcting common OCR errors (e.g., misread characters, missing spaces, incorrect word formations).
2. Extracting metadata like date, author etc and numerical scores for different attributes and in your thought process explain why you give a particular score.

Here is the raw text from a document:

"{text_content}"

### Step 1: OCR Error Correction
- Fix character misinterpretations: `0 ↔ O`, `1 ↔ l`, `I ↔ 1`, `rn → m`, `vv → w`
- Detect and correct misspelled words based on the document language (French, German, Dutch).
- Restore broken words and remove unnecessary line breaks.
- ONLY return a valid JSON object with no additional text, reasoning, or explanations.
- DON'T print your thinking in the response (</think>)
- your response should only be from ''' "to" ''' of the JSON answer


### Step 2: Text Analysis
After correcting the OCR errors, analyze the corrected text and return results in JSON format:
```json
{{
  "date": "Extract date as dd-mm-yy",
  "publisher": "If there is the publisher extract it, otherwise assign NA",
  "language": "Retrieve language of text",
  "author": "Find author's name, otherwise assign NA",
  "corrected_text": "Corrected version of the input text.",
  "sentiment": {{ "positive": X.XX, "negative": X.XX, "neutral": X.XX }},
  "emotion_scores": {{ "fear": X.XX, "anger": X.XX, "hope": X.XX, "glory": X.XX, "patriotism": X.XX }},
  "word_frequencies": {{ "victory": X, "death": X, "enemy": X, "glory": X }},
  "topic_scores": {{ "military": X.XX, "economy": X.XX, "propaganda": X.XX }},
  "propaganda_techniques": {{ "appeal_to_fear": X.XX, "bandwagon": X.XX, "demonization": X.XX }},
  "readability_score": X.XX,
  "sentence_complexity": X.XX,
  "imperative_usage": X.XX,
  "historical_references": {{ "battle_mentions": X, "leader_mentions": X }}
}}'''



client = InferenceClient(
	provider="together",
	api_key=HF_API_KEY
)

messages = [
	{
		"role": "user",
		"content": prompt
	}
]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1", 
	messages=messages, 
	max_tokens=15000,
)

print(completion.choices[0].message)

# Extract JSON response
response_text = completion.choices[0].message['content']
print(response_text)

json_match = re.search(r'\{.*\}', response_text, re.DOTALL)

if json_match:
    json_text = json_match.group(0)  # Extract the JSON content
    try:
        response_data = json.loads(json_text)  # Convert to dictionary
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response.")
        response_data = {}
else:
    print("Error: No valid JSON found in response.")
    response_data = {}

# Convert dictionary to DataFrame
df = pd.json_normalize(response_data)

# Append to an Excel file
excel_path = "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/analysis_results.xlsx"

try:
    existing_df = pd.read_excel(excel_path)
    df = pd.concat([existing_df, df], ignore_index=True)
except FileNotFoundError:
    pass  # No existing file, so we'll just write the new data

df.to_excel(excel_path, index=False)

print("Analysis results saved to", excel_path)