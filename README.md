#  Cloud-Hosted Notebooks

  Welcome to my project! This repository contains all the code and resources related to the project.

## Getting Started
### Prerequisites
  A Google account for accessing Google Colab.
  Basic knowledge of Python and data manipulation libraries.
### Setting up the Notebook
  Open Google Colab: Visit Google Colab and sign in with your Google account.
  Create a New Notebook: Click on New Notebook to start a new Jupyter notebook.
  Clone the GitHub Repository: (Optional) If the notebook is hosted on GitHub, you can clone it directly into Google Colab.

## Google Colab Link
https://colab.research.google.com/drive/1r1uVyrKdG3y6_gTwDXgwSY5ynr7y_7wl?usp=sharing

## Main Code
```
import seaborn as sns
import matplotlib.pyplot as plt
```
```
# Load the 'tips' dataset from Seaborn
df = sns.load_dataset('tips')

# Basic info
df.info()

# Descriptive statistics
df.describe()

# Check for missing values
df.isnull().sum()
```
```
# Pairplot to visualize relationships
sns.pairplot(df, hue="time")  # 'time' is a column in the 'tips' dataset
plt.show()

# Select only numeric columns for correlation heatmap
numeric_cols = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.show()
```

## Result
  Relationships
  ![Relationships](relation.png)
  Heatmap
  ![Heatmap](heatmap.png)


