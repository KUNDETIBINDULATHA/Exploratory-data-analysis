import pandas as pd
data = pd.read_csv("Titanic-Dataset.csv")
print(data.head())
print(data.info())
print(data.isnull().sum())
print(data.describe())
import matplotlib.pyplot as plt

data["Survived"].value_counts().plot(kind="bar")

plt.title("Survival Count")

plt.show()
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Titanic-Dataset.csv")

# Show first 5 rows
print(data.head())

# Dataset information
print(data.info())

# Missing values
print(data.isnull().sum())

# Statistical summary
print(data.describe())

# Survival graph
data["Survived"].value_counts().plot(kind="bar")

plt.title("Survival Count")

plt.show()