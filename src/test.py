import pandas as pd
train = pd.read_parquet("./data/train.parquet")
print(train.head())
