import pandas as pd

# load the dataset
df = pd.read_csv("iris.csv")

# show first 5 rows
print("First 5 rows : ")
print(df.head(5))

# summary statistics
print("\nSummary statistics : ")
print(df.describe())