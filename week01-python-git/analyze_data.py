# #day2
# import pandas as pd

# # load the dataset
# df = pd.read_csv("iris.csv")

# # show first 5 rows
# print("First 5 rows : ")
# print(df.head(5))

# # summary statistics
# print("\nSummary statistics : ")
# print(df.describe())

#day3
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def summarize_data(df):
    print("\n2. First 5 rows : ")
    print(df.head(5))
    print("\n2. Summary Statistics : ")
    print(df.describe())

def main():
    df = load_data("iris.csv")
    summarize_data(df)

if __name__ == "__main__":
    main()