import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
base_path = r'c:\Users\E-BOOKS WORKSTATION\Desktop\miracle'
cleaned_file = os.path.join(base_path, 'winemag_cleaned.csv')
df = pd.read_csv(cleaned_file)

print("--- Data Analysis: Price vs quality ---")
correlation = df['price'].corr(df['points'])
print(f"Correlation coefficient between price and points: {correlation:.4f}")

# Grouping by points to see average price
avg_price_per_point = df.groupby('points')['price'].mean().reset_index()
print("\nAverage Price per Point Level:")
print(avg_price_per_point.tail(10)) # Top ratings

# Basic visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='points', y='price', alpha=0.1)
plt.title('Correlation between Price and Points (Quality)')
plt.xlabel('Points (80-100)')
plt.ylabel('Price ($)')
plt.yscale('log') # Prices can vary wildly, log scale helps
plt.grid(True, which="both", ls="-", alpha=0.2)

# Save visualization
plot_file = os.path.join(base_path, 'price_points_correlation.png')
plt.savefig(plot_file)
print(f"\nVisualization saved to {plot_file}")

# Identify outliers
print("\n--- Potential High-Value Outliers (High points, Low price) ---")
best_value = df[(df['points'] >= 95) & (df['price'] <= 30)]
print(best_value[['title', 'points', 'price', 'variety', 'country']].head(10) if 'title' in df.columns else best_value[['variety', 'country', 'points', 'price']].head(10))
