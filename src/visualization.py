import plotly.express as px
import pandas as pd
from collections import Counter
import os
import numpy as np

# Emotion word categories
emotion_dict = {
    "peur": [
        "mort", "destruction", "peur", "désespoir", "danger", "souffrance",
        "menace", "oppression", "tyran", "persécution", "aservir"
    ],
    "gloire": [
        "victoire", "gloire", "honneur", "respect", "courage", "triomphe",
        "héros", "justice", "sacrifice", "résilience", "espoir"
    ],
    "colère": [
        "ennemi", "traître", "rage", "révolte", "despotisme", "indignation",
        "violence", "rébellion", "cruauté", "tyrannie", "brutalité"
    ],
    "patriotisme": [
        "nation", "loyauté", "devoir", "sacrifice", "patrie", "unité",
        "liberté", "solidarité", "dignité", "valeurs", "justice"
    ],
}

# Get the absolute path of the data directory
script_dir = os.path.dirname(os.path.abspath(__file__))  # Location of datavisualization.py
data_dir = os.path.join(script_dir, "../data")  # Adjust to be at the same level as src/

# Function to load and tokenize text
def load_text(filename):
    filepath = os.path.join(data_dir, filename)
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return []
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read().lower().split()

# Load the texts
response_text = load_text("response.txt")
french_text = load_text("frenchPropaganda.txt")

# Count words related to emotions
def count_emotion_words(text, emotion_dict):
    word_counts = Counter(text)
    return {emotion: sum(word_counts[word] for word in words if word in word_counts)
            for emotion, words in emotion_dict.items()}

response_counts = count_emotion_words(response_text, emotion_dict)
french_counts = count_emotion_words(french_text, emotion_dict)

# Prepare data for visualization
data = []
for emotion in emotion_dict.keys():
    data.append({"text": "response.txt", "emotion": emotion, "count": response_counts.get(emotion, 0)})
    data.append({"text": "frenchPropaganda.txt", "emotion": emotion, "count": french_counts.get(emotion, 0)})

df = pd.DataFrame(data)

# Create an interactive bubble chart
fig = px.scatter(df, 
                 x="emotion", 
                 y="text", 
                 size="count", 
                 color="emotion", 
                 hover_name="emotion",
                 size_max=100, 
                 title="Emotional Profile Comparison")

# Custom function to position the words like rays
def generate_word_positions(emotion, n=10, radius=1.5):
    # Randomly position words around the bubble (in polar coordinates)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    positions = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]
    
    # Place words around the bubble
    words = emotion_dict[emotion]
    return positions, words

# Add the rays (words) to the plot
annotations = []
for i, emotion in enumerate(emotion_dict.keys()):
    positions, words = generate_word_positions(emotion)
    
    # Add the words around the bubble
    for j, (x_offset, y_offset) in enumerate(positions):
        annotations.append(dict(
            x=x_offset + i,  # Center bubble at i on x-axis
            y=1,  # Keep y-axis fixed for simplicity
            text=words[j],
            showarrow=True,
            arrowhead=2,
            ax=x_offset,
            ay=y_offset,
            font=dict(size=10, color="black")
        ))

# Update layout for rays
fig.update_layout(
    xaxis_title="Emotion",
    yaxis_title="Text Source",
    showlegend=False,
    annotations=annotations
)


# Customize layout
fig.update_layout(
    xaxis_title="Emotion",
    yaxis_title="Text Source",
    showlegend=False
)

# Show the figure
fig.show()
