import pandas as pd

# Read one dataset
df = pd.read_csv("data/flats.csv")

print("Dataset shape:", df.shape)
print("First 5 rows:")
print(df.head(5))
