import os
import pandas as pd
import json
import re

# Path to the folder containing your text files
folder_path = "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/Posters/texts/french/"

# Get the list of all text files in the folder and limit it to the first 10
text_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')][:10]

# Initialize list to collect results
all_results = []

# Loop through the first 10 files
for file_path in text_files:
    file_name = os.path.basename(file_path)  # Extract just the filename

    # Read the text file
    with open(file_path, "r", encoding="utf-8") as file:
        text_content = file.read()

    print(f"Processing file: {file_name}")  # Debugging print

    # Simulate an API response (replace this with mock data for testing)
    response_data = {
        "date": "01-01-1917",
        "publisher": "NA",
        "language": "French",
        "author": "NA",
        "corrected_text": text_content,
        "sentiment": {"positive": 0.10, "negative": 0.05, "neutral": 0.85},
        "emotion_scores": {"fear": 0.2, "anger": 0.1, "hope": 0.3, "glory": 0.4, "patriotism": 0.5},
        "word_frequencies": {"victory": 5, "death": 3, "enemy": 2, "glory": 4},
        "topic_scores": {"military": 0.8, "economy": 0.2, "propaganda": 0.9},
        "propaganda_techniques": {"appeal_to_fear": 0.7, "bandwagon": 0.5, "demonization": 0.3},
        "readability_score": 0.75,
        "sentence_complexity": 0.65,
        "imperative_usage": 0.55,
        "historical_references": {"battle_mentions": 2, "leader_mentions": 1}
    }

    # Convert to DataFrame and include filename
    df = pd.json_normalize(response_data)
    df.insert(0, "Filename", file_name)  # Insert filename as the first column

    # Append results to the list
    all_results.append(df)

# Combine all results into one DataFrame
final_df = pd.concat(all_results, ignore_index=True)

# Save the combined results to an Excel file
excel_path = "C:/Users/Michael/WWI-Poster-Analysis-Datathon/data/analysis_results.xlsx"
final_df.to_excel(excel_path, index=False)

print(f"Analysis results saved to {excel_path}")
