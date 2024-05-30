import pandas as pd

# Load the Parquet file into a DataFrame
df = pd.read_parquet('yellow_tripdata_2021-01.parquet')

# Export the DataFrame to a CSV file
df.to_csv('yellow_tripdata_2021-01.csv', index=False)