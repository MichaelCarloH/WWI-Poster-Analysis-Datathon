from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# List of themes from the provided data
themes_data = [{'themes': {'pride': 3, 'suffering': 5, 'sacrifice': 4, 'engineering': 4, 'war': 6, 'unity': 3, 'resilience': 2, 'human cost': 3, 'innovation': 2, 'empathy': 2, 'pressure': 2, 'family': 2, 'duty': 2, 'collaboration': 2, 'justice': 2, 'hope': 2}}, {'themes': ['national pride', 'human suffering', 'empathy', 'sacrifice', 'peace', 'healing', 'unity', 'justice', 'military success', 'resilience', 'loss', 'understanding', 'advocacy']}, {'themes': ['Pride in military efforts', 'Sacrifices for the greater good', 'Human cost of war', 'Frustration with propaganda portrayal', 'Importance of national strength and security', 'Need for empathy and unity', 'Call for justice and accountability', 'Support for troops and military advancements']}, {'themes': {'human suffering': 5, 'empathy': 4, 'peace': 4, 'sacrifice': 3, 'loss': 3, 'understanding': 3, 'advocacy': 3, 'victory narratives': 2, 'unity': 2, 'justice': 2, 'grief': 2, 'oppression': 2, 'bravery': 1, 'resilience': 1, 'community support': 1, 'healing': 1}}, {'themes': {'empathy': 3, 'suffering': 4, 'military necessity': 3, 'context of struggle': 3, 'human cost of war': 2, 'frustration': 2, 'future of nation': 3, 'unity': 2, 'justice': 2, 'sacrifice': 2}}, {'themes': ['human cost of war', 'suffering and loss', 'national pride', 'empathy and compassion', 'unity and justice', 'broader implications of war', 'inclusive dialogue', 'peace and healing']}, {'themes': ['pride', 'determination', 'bravery', 'suffering', 'sacrifice', 'national unity', 'support for troops', 'human cost of war', 'complexity of conflict', 'empathy', 'military necessity', 'call for justice', 'importance of peace']}, {'themes': {'empathy': 3, 'suffering': 4, 'military success': 3, 'unity': 3, 'justice': 3, 'peace': 4, 'human cost': 2, 'national identity': 2, 'compassion': 2, 'healing': 3}}, {'themes': {'war': 5, 'suffering': 4, 'Germany': 4, 'military': 4, 'innocent lives': 3, 'human cost': 3, 'victories': 3, 'empathy': 3, 'loss': 3, 'peace': 3, 'justice': 3, 'unity': 2, 'sacrifice': 2, 'resilience': 2, 'oppression': 2, 'national pride': 2, 'community': 2, 'accountability': 2, 'future': 2, 'impact': 2, 'balance': 2}}, {'themes': {'pride': 3, 'suffering': 4, 'national identity': 4, 'support for Germany': 4, 'human cost of war': 3, 'unity': 3, 'justice': 2, 'resilience': 2, 'empathy': 2, 'loss': 3, 'aggression': 1, 'defense': 1}}, {'themes': {'human cost': 5, 'suffering': 4, 'military efforts': 3, 'empathy': 3, 'unity': 3, 'justice': 3, 'shared humanity': 2, 'loss': 2, 'resilience': 2, 'oppression': 2, 'victories': 2, 'families': 2, 'conflict': 2, 'hope': 1, 'sacrifice': 1, 'courage': 1, 'dignity': 1, 'peace': 1, 'accountability': 1, 'future': 1}}, {'themes': {'empathy': 3, 'human suffering': 4, 'military success': 3, 'national pride': 3, 'unity': 3, 'justice': 3, 'conflict': 3, 'loss': 3, 'peace': 3, 'duty': 3}}, {'themes': {'war': 5, 'suffering': 4, 'military': 4, 'peace': 4, 'sacrifice': 3, 'human cost': 3, 'empathy': 3, 'victories': 2, 'responsibility': 2, 'unity': 2, 'justice': 2, 'safety': 2, 'loss': 2, 'oppression': 2, 'bravery': 1, 'hope': 1, 'resilience': 1, 'duty': 1, 'future': 1, 'understanding': 1}}, {'themes': {'empathy': 3, 'human cost of war': 3, 'suffering': 4, 'unity': 3, 'community support': 2, 'healing': 2, 'loss': 3, 'resilience': 2, 'importance of history': 1, 'cultural heritage': 1, 'justice': 2, 'oppression': 2, 'military victories': 2, 'pain': 3, 'sacrifice': 2}}, {'themes': {'military success': 3, 'human suffering': 5, 'national security': 3, 'unity and justice': 3, 'empathy': 2, 'balance': 3, 'peace': 3, 'sacrifice': 2, 'resilience': 2, 'oppression': 2}}]












# Aggregate all themes into a single list
all_themes = [theme for entry in themes_data for theme in entry['themes']]

# Count the frequency of each theme
theme_counts = Counter(all_themes)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(theme_counts)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()