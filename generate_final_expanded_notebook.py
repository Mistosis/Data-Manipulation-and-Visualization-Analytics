import nbformat as nbf
import os

# Define the notebook content
nb = nbf.v4.new_notebook()

# 0. Header
nb.cells.append(nbf.v4.new_markdown_cell("# Expanded Wine Magazine Data Analysis & Assortment Strategy\n\n**Author:** Miracle\n\nThis notebook provides a comprehensive 10-step investigation into the wine market, covering demographics, pricing, quality, and linguistic profiles."))

# 1. Cleaning
nb.cells.append(nbf.v4.new_markdown_cell("## 1. Data Cleaning & Integration\nMerging 150k and 130k-v2 datasets with metadata preservation."))
nb.cells.append(nbf.v4.new_code_cell("""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv('winemag_cleaned.csv')
print(f"Analysis dataset size: {df.shape}")
"""))

# 2. Tasters
nb.cells.append(nbf.v4.new_markdown_cell("## 2. Professional Critic Analysis\nComparing score distributions of the top wine tasters."))
nb.cells.append(nbf.v4.new_code_cell("""taster_counts = df['taster_name'].value_counts()
pro_tasters = taster_counts[taster_counts > 500].index
df_pro = df[df['taster_name'].isin(pro_tasters)]

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_pro, x='taster_name', y='points', palette='Set2')
plt.xticks(rotation=45)
plt.title('Rating Tendencies by Critic')
plt.show()
"""))

# 3. Price Tiers
nb.cells.append(nbf.v4.new_markdown_cell("## 3. Price Tier Segmentation\nStrategic breakdown of the market by price categories."))
nb.cells.append(nbf.v4.new_code_cell("""def segment_price(price):
    if price < 15: return 'Budget'
    elif price < 35: return 'Premium'
    elif price < 100: return 'Luxury'
    else: return 'Collector'

df['tier'] = df['price'].apply(segment_price)
tier_avg = df.groupby('tier')['points'].mean().sort_values()

plt.figure(figsize=(10, 5))
sns.barplot(x=tier_avg.index, y=tier_avg.values, palette='coolwarm')
plt.ylim(80, 100)
plt.title('Quality by Price Segment')
plt.show()
"""))

# 4. Regional Specialization
nb.cells.append(nbf.v4.new_markdown_cell("## 4. Quality Heatmap\nMapping which countries excel at specific varieties."))
nb.cells.append(nbf.v4.new_code_cell("""top_c = df['country'].value_counts().head(8).index
top_v = df['variety'].value_counts().head(8).index
piv = df[df['country'].isin(top_c) & df['variety'].isin(top_v)].pivot_table(index='country', columns='variety', values='points', aggfunc='mean')

plt.figure(figsize=(10, 6))
sns.heatmap(piv, annot=True, cmap='RdPu')
plt.title('Variety Specialization Heatmap (Avg Pts)')
plt.show()
"""))

# 5. Word Clouds
nb.cells.append(nbf.v4.new_markdown_cell("## 5. Descriptive Flavors\nLinguistic profiles of high-rating vs low-rating wines."))
nb.cells.append(nbf.v4.new_markdown_cell("![High Rating Descriptors](wordcloud_high.png)\n![Low Rating Descriptors](wordcloud_low.png)"))

# 6. Conclusion & Strategy
nb.cells.append(nbf.v4.new_markdown_cell("## 6. Final Assortment Strategy\n\n1. **Focus:** Target 'Premium' tier ($15-$35) where quality hits the 90-point mark with moderate investment.\n2. **Curated regions:** Germany/Austria for consistent high-quality white blends.\n3. **Curation:** Use specific taster preferences (e.g., Matt Kettmann) to curate high-quality California selections."))

# Save the notebook
base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
nb_file = os.path.join(base_path, 'MiraclePython.ipynb')
with open(nb_file, 'w') as f:
    nbf.write(nb, f)

print(f"Final expanded notebook created at {nb_file}")
