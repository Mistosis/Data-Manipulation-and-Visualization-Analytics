import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 4: Taster Consistency Analysis ---")
# Only keep tasters with more than 500 reviews
taster_counts = df['taster_name'].value_counts()
pro_tasters = taster_counts[taster_counts > 500].index

df_pro = df[df['taster_name'].isin(pro_tasters)]

plt.figure(figsize=(14, 8))
sns.boxplot(data=df_pro, x='taster_name', y='points', palette='vlag')
plt.xticks(rotation=45)
plt.title('Score Distribution by Professional Taster (>500 reviews)')
plt.tight_layout()
plt.savefig(os.path.join(base_path, 'taster_analysis.png'))

print("\nTaster Statistics (Average Points):")
print(df_pro.groupby('taster_name')['points'].mean().sort_values(ascending=False))

print(f"\nGraph saved to taster_analysis.png")
