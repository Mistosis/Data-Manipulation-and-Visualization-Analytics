import pandas as pd
import os

base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
df = pd.read_csv(os.path.join(base_path, 'winemag_cleaned.csv'))

print("--- Step 11: 'Star' Wineries Analysis ---")

# Best winery by average points for top 5 countries (minimum 10 reviews)
top_countries = df['country'].value_counts().head(5).index

print("\nTop Winery in Leading Countries (Avg Points):")
for country in top_countries:
    winery_stats = df[df['country'] == country].groupby('winery')['points'].agg(['mean', 'count'])
    pro_wineries = winery_stats[winery_stats['count'] >= 10]
    if not pro_wineries.empty:
        star = pro_wineries['mean'].idxmax()
        avg = pro_wineries.loc[star, 'mean']
        print(f"[{country}] Star Winery: {star} ({avg:.2f} pts)")

print("\nAnalysis complete.")
