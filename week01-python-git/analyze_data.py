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

# #day3
# import pandas as pd

# def load_data(file_path):
#     return pd.read_csv(file_path)

# def summarize_data(df):
#     print("\n2. First 5 rows : ")
#     print(df.head(5))
#     print("\n2. Summary Statistics : ")
#     print(df.describe())

# def main():
#     df = load_data("iris.csv")
#     summarize_data(df)

# if __name__ == "__main__":
#     main()

#day4
import argparse
import pandas as pd
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    return pd.read_csv(file_path)

def summarize_data(df):
    print("\n3. First 5 records : ")
    print(df.head(5))
    print("\n3. Summary statistics : ")
    print(df.describe())

def main():
    parser = argparse.ArgumentParser(description="Analyze a CSV file.")
    parser.add_argument("--file", type=str, required=True, help="Path to the CSV file")
    args = parser.parse_args()

    try:
        df = load_data(args.file)
        summarize_data(df)
    except FileNotFoundError as e:
        print(f"3. FileNotFoundError : {e}")
    except Exception as e:
        print(f"3. Exception : {e}")

if __name__ == "__main__":
    main()
