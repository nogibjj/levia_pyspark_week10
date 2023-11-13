import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset from Seaborn
df = sns.load_dataset('tips')

# Basic info
df.info()

# Descriptive statistics
df.describe()

# Check for missing values
df.isnull().sum()

# Pairplot to visualize relationships
sns.pairplot(df, hue="time")  # 'time' is a column in the 'tips' dataset
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
