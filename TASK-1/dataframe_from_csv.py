import pandas as pd
#import re

#Soal No 2
#def to_snake_case(s):
#    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
#    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s)
#    return s.lower()

df = pd.read_csv("../dataset/sample.csv", sep=",")
#df.columns = [to_snake_case(col) for col in df.columns]
#df.to_csv("../dataset/sample.csv", index=False)
print(df)
print("")
print(df.head(10))

#Soal No 3
df_single_col = df["passenger_count"]
print("select single column")
print("")
print(df_single_col.head(10))

df_multiple_col = df[["vendor_id", "passenger_count", "trip_distance", "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount"]]
print("select multiple columns")
print("")
print(df_multiple_col)

#Soal No 4
df['vendor_id'] = df['vendor_id'].astype(int)
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
df['passenger_count'] = df['passenger_count'].astype(int)
df['trip_distance'] = df['trip_distance'].astype(float)
df['ratecode_id'] = df['ratecode_id'].astype(int)
df['store_and_fwd_flag'] = df['store_and_fwd_flag'].astype('category')
df['pu_location_id'] = df['pu_location_id'].astype(int)
df['do_location_id'] = df['do_location_id'].astype(int)
df['payment_type'] = df['payment_type'].astype('category')
df['fare_amount'] = df['fare_amount'].astype(float)
df['extra'] = df['extra'].astype(float)
df['mta_tax'] = df['mta_tax'].astype(float)
df['tip_amount'] = df['tip_amount'].astype(float)
df['tolls_amount'] = df['tolls_amount'].astype(float)
df['improvement_surcharge'] = df['improvement_surcharge'].astype(float)
df['total_amount'] = df['total_amount'].astype(float)
df['congestion_surcharge'] = df['congestion_surcharge'].astype(float)
print(df.dtypes)
