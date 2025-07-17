import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. DATA LOADING AND CLEANING
data = pd.read_csv('/Users/macbook/Downloads/BIPANDA Franck.csv')
# Interpretation: Import the customer churn data. Convert monthly and total charges to numbers,
# replacing non-convertible values with NaN. Remove any rows missing these crucial values.
data['Total Charges'] = pd.to_numeric(data['Total Charges'], errors='coerce')
data['Monthly Charges'] = pd.to_numeric(data['Monthly Charges'], errors='coerce')
data = data.dropna(subset=['Total Charges', 'Monthly Charges'])

# 2. DATA STRUCTURE & QUALITY CHECK
print("Shape of data:", data.shape)
print("\nMissing values:\n", data.isnull().sum())
print("\nData types:\n", data.dtypes)
print("\nBasic statistics:\n", data.describe(include="all"))
# Interpretation: Check the dataset's size, missing values per column, types of each column, and descriptive statistics.
# This helps spot problems and understand data composition before analysis.

# 3. DATA EXPLORATION: MAIN VARIABLES
print(data.head())
print("\nMain descriptive statistics:")
print(data[['Monthly Charges', 'Total Charges', 'Tenure Months']].describe())
# Interpretation: Preview how the data looks, confirming import worked and seeing value ranges for major metrics.

# 4. MONTHLY CHARGES HISTOGRAM
plt.figure(figsize=(10, 6))
plt.hist(data['Monthly Charges'], bins=30, color='blue', alpha=0.7)
plt.title("Histogram of Monthly Charges")
plt.xlabel("Monthly Charge ($)")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()
# Interpretation: Shows if most customers are concentrated in certain price ranges, and reveals outliers.

# 5. BOXPLOT FOR MONTHLY CHARGES
plt.figure(figsize=(10, 6))
plt.boxplot(data['Monthly Charges'], vert=False)
plt.title("Boxplot of Monthly Charges")
plt.xlabel("Monthly Charge ($)")
plt.grid(axis='x')
plt.show()
# Interpretation: Highlights high and low outliers, plus the spread and median of monthly charges.

# 6. TOP 25 CLIENTS BY TOTAL SPENT
total_spent = data.groupby('CustomerID')['Total Charges'].sum().reset_index()
top_25 = total_spent.sort_values(by='Total Charges', ascending=False).head(25)
plt.figure(figsize=(12, 7))
plt.bar(top_25['CustomerID'], top_25['Total Charges'], color='orange')
plt.title("Total Spent per Client (Top 25)")
plt.xlabel("CustomerID")
plt.ylabel("Total Charges ($)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
# Interpretation: Reveals your most lucrative customers—losing these impacts overall revenue the most.

# 7. TENURE VS. TOTAL PAID SCATTERPLOT
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Tenure Months', y='Total Charges', hue='Churn Reason', legend=False, palette='viridis')
plt.title("Tenure vs. Total Paid")
plt.xlabel("Tenure (Months)")
plt.ylabel("Total Charges ($)")
plt.grid()
plt.show()
# Interpretation: Confirms that the longer customers stay, the more they pay in total. Outliers might indicate unique usage patterns.

# 8. CORRELATION HEATMAP
plt.figure(figsize=(8, 5))
corr = data[['Monthly Charges', 'Total Charges', 'Tenure Months']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix (Monthly Charges, Total Charges, Tenure)")
plt.show()
# Interpretation: Visualizes the strength and direction of relationships among your main numeric variables.

# 9. TOP 5 CLIENTS BY TOTAL SPENT
top5 = total_spent.sort_values(by='Total Charges', ascending=False).head(5)
plt.figure(figsize=(8, 5))
plt.bar(top5['CustomerID'], top5['Total Charges'], color='green')
plt.title("Top 5 Biggest Spenders")
plt.xlabel("CustomerID")
plt.ylabel("Total Charges ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
# Interpretation: Pinpoint the individual customers responsible for the highest lifetime value.

# 10. TOP 10 CHURN REASONS
plt.figure(figsize=(12, 6))
top_reasons = data['Churn Reason'].value_counts().head(10)
sns.barplot(y=top_reasons.index, x=top_reasons.values, palette='mako')
plt.title("Top 10 Churn Reasons")
plt.xlabel("Number of Customers")
plt.ylabel("Churn Reason")
plt.show()
# Interpretation: Identifies the main drivers of customer departures—guides where to focus retention efforts.

