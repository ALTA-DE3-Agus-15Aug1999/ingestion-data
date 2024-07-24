import pandas as pd
from sqlalchemy import create_engine, Integer, String, Float, DateTime

pd.set_option('display.max_columns', None)

df = pd.read_parquet("../dataset/yellow_tripdata_2023-01.parquet", engine='fastparquet') 
#print(df.head(5))

df.columns = [col.lower().replace(' ', '_') for col in df.columns]

df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
df['passenger_count'] = df['passenger_count'].astype(int)
df['trip_distance'] = df['trip_distance'].astype(float)

df = df.dropna()

df = df.drop_duplicates()

df = df[df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime']]
df = df[df['passenger_count'] > 0]
df = df[df['trip_distance'] > 0]

dtype = {
    'vendor_id': Integer,
    'tpep_pickup_datetime': DateTime,
    'tpep_dropoff_datetime': DateTime,
    'passenger_count': Integer,
    'trip_distance': Float,
    'ratecode_id': Integer,
    'store_and_fwd_flag': String,
    'pu_location_id': Integer,
    'do_location_id': Integer,
    'payment_type': Integer,
    'fare_amount': Float,
    'extra': Float,
    'mta_tax': Float,
    'tip_amount': Float,
    'tolls_amount': Float,
    'improvement_surcharge': Float,
    'total_amount': Float,
    'congestion_surcharge': Float,
    "airport_fee": Float
}

print(df.head(5))