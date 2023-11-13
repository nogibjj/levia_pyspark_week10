import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# Fetch the Iris dataset
iris = fetch_openml(name='iris', version=1)
data = iris.data
feature_names = data.columns
target = iris.target

# Convert target to numeric if it's in string format
target = pd.Categorical(target).codes

# Create a DataFrame
df = pd.DataFrame(data, columns=feature_names)
df['target'] = target

# Basic info
df.info()

# Descriptive statistics
df.describe()

# Check for missing values
df.isnull().sum()

# Pairplot to visualize relationships
sns.pairplot(df, hue="target")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
