
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Rename columns for easier reference
df = pd.read_csv("C:\\Users\\sarve\\AppData\\Local\\Programs\\Python\\Python311\\Stage1_Data_Analysis_Dataset.csv")

df.columns = [
    "City", "Ward", "Plastic_Waste_Generated", "Recycled_Waste_Percentage",
    "Population", "Waste_Hotspots", "Community_Engagement_Percentage"
]
print(df)
# Identify top 10 waste-generating cities
top_waste_cities = df.groupby("City")["Plastic_Waste_Generated"].sum().sort_values(ascending=False)

#Q1 Cities to check 
cities_to_check = ["Aryanagar", "Bhavanipur", "Devnagar", "Vishwanagar"]
filtered_df = df[df["City"].isin(cities_to_check)]
highest_waste_city = filtered_df.groupby("City")["Plastic_Waste_Generated"].sum().idxmax()
print("City with the highest plastic waste:", highest_waste_city)

#Q2
columns_of_interest = [
    'Recycled_Waste_Percentage', 
    'Population', 
    'Plastic_Waste_Generated', 
    'Community_Engagement_Percentage', 
    'Waste_Hotspots'
]
data_subset = df[columns_of_interest]
correlation_matrix = data_subset.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Recycling Rates and Factors')
plt.show()

#Q3
city_recycling_rates = df.groupby('City')['Recycled_Waste_Percentage'].mean()
lowest_recycling_city = city_recycling_rates.idxmin()
lowest_recycling_rate = city_recycling_rates.min()
print(f"City with Lowest Recycling Percentage: {lowest_recycling_city}")
print(f"Recycling Rate: {lowest_recycling_rate:.2f}%")



# Calculate correlation with Recycling Efficiency
numeric_df = df.select_dtypes(include=['number'])
correlation_values = numeric_df.corr()["Recycled_Waste_Percentage"].sort_values(ascending=False)
print(correlation_values)
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
# Plot waste generation hotspots
plt.figure(figsize=(12, 5))
top_waste_cities.plot(kind="bar", color="red")
plt.title("Top 10 Waste-Generating Cities")
plt.xlabel("City")
plt.ylabel("Total Plastic Waste Generated (kg/day)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Recycling efficiency vs. Waste generation scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(
    x=df["Plastic_Waste_Generated"],
    y=df["Recycled_Waste_Percentage"],
    hue=df["City"],
    palette="viridis",
    alpha=0.7
)
plt.title("Waste Generation vs. Recycling Efficiency")
plt.xlabel("Plastic Waste Generated (kg/day)")
plt.ylabel("Recycling Efficiency (%)")
plt.grid(True)
plt.show()

# Community engagement vs. Recycling efficiency scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(
    x=df["Community_Engagement_Percentage"],
    y=df["Recycled_Waste_Percentage"],
    hue=df["City"],
    palette="coolwarm",
    alpha=0.7
)
plt.title("Community Engagement vs. Recycling Efficiency")
plt.xlabel("Community Engagement (%)")
plt.ylabel("Recycling Efficiency (%)")
plt.grid(True)
plt.show()

#Upload a PDF with the following visualizations: 
"""
1. Create a bar chart comparing the plastic waste generation across five different cities  
2. Generate a scatter plot to show the correlation between community engagement and recycling rates
3. Illustrate the proportion of plastic waste recycled vs. generated in a selected city"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Bar Chart of Plastic Waste Generation
top_cities = df.groupby('City')['Plastic_Waste_Generated'].mean().nlargest(5)
plt.figure(figsize=(10,6))
top_cities.plot(kind='bar')
plt.title('Average Plastic Waste Generation by City')
plt.xlabel('City')
plt.ylabel('Plastic Waste (kg/day)')
plt.xticks(rotation=45)
plt.tight_layout()

# 2. Scatter Plot: Community Engagement vs Recycling Rates
plt.figure(figsize=(10,6))
plt.scatter(df['Community_Engagement_Percentage'], df['Recycled_Waste_Percentage'])
plt.title('Community Engagement vs Recycling Rates')
plt.xlabel('Community Engagement (%)')
plt.ylabel('Recycling Rate (%)')
plt.tight_layout()

# 3. Pie Chart for Zaverinagar's Waste
zaverinagar_data = df[df['City'] == 'Zaverinagar']
waste_generated = zaverinagar_data['Plastic_Waste_Generated'].mean()
waste_recycled = zaverinagar_data['Recycled_Waste_Percentage'].mean() * waste_generated / 100
plt.figure(figsize=(8,8))
plt.pie([waste_recycled, waste_generated-waste_recycled], 
        labels=['Recycled', 'Non-Recycled'], 
        autopct='%1.1f%%')
plt.title('Zaverinagar Waste Recycling Proportion')
plt.show()
