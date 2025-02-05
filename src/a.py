import ollama

# Read the text file
with open("C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/FL4984787_1_DIGI_0035_00001_VIEW_MAIN.jpg.txt", "r", encoding="utf-8") as file:
    text_content = file.read()

# Insert text into the DeepSeek-R1 prompt
deepseek_prompt = f'''
You are a historical text analyst. Your task is to analyze WW1 propaganda text by:
1. Correcting common OCR errors (e.g., misread characters, missing spaces, incorrect word formations).
2. Extracting numerical scores for different attributes.

Here is the raw text from a document:

"{text_content}"

### Step 1: OCR Error Correction
- Fix character misinterpretations: `0 ↔ O`, `1 ↔ l`, `I ↔ 1`, `rn → m`, `vv → w`
- Detect and correct misspelled words based on the document language (French, German, Dutch).
- Restore broken words and remove unnecessary line breaks.

### Step 2: Text Analysis
After correcting the OCR errors, analyze the corrected text and return results in JSON format:
```json
{{
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

print(deepseek_prompt)

response = ollama.chat(model="deepseek-r1", messages = [{"role": "user", "content": deepseek_prompt}])

print(response["message"]["content"])