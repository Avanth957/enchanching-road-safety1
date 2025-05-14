import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file (adjust encoding if needed)
df = pd.read_csv("global_traffic_accident.csv", encoding="ISO-8859-1")

# View basic info
print("First 5 rows of the dataset:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary statistics:")
print(df.describe(include='all'))

# Group by country (replace 'Country' with your actual column name)
if 'Country' in df.columns:
    country_counts = df['Country'].value_counts()
    print("\nAccidents by country:")
    print(country_counts)

    # Plotting
    plt.figure(figsize=(10,6))
    country_counts.head(10).plot(kind='bar', color='skyblue')
    plt.title('Top 10 Countries by Number of Accidents')
    plt.xlabel('Country')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# You can repeat similar grouping for 'Year', 'Severity', etc.