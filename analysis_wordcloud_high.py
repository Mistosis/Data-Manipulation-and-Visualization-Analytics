import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 8: Word Cloud - High Rating Wines (95+) ---")

text = " ".join(review for review in df[df['points'] >= 95]['description'])
wordcloud = WordCloud(max_words=100, background_color="white", colormap="viridis").generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Common Descriptors in High-Rating Wines (95+)')
plt.savefig(os.path.join(base_path, 'wordcloud_high.png'))

print(f"\nWordcloud saved to wordcloud_high.png")
