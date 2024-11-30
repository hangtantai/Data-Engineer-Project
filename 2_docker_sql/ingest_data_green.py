# import necessary library
import pandas as pd
from sqlalchemy import create_engine
import os
import argparse
from time import time
from datetime import datetime

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # the backup files 
    if url.endswith('.csv.gz'):
        csv_name = 'output_green.csv.gz'
    else:
        csv_name = 'output_green.csv'

    os.system(f"wget {url} -O {csv_name}")

    # create engine to connect local database
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    engine.connect()

    # using iteration to split database and add by chunksize
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    # convert string to date time
    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], format='%Y-%m-%d %H:%M:%S')


    df.head(n=0).to_sql(name = table_name, con = engine, if_exists="replace")
    df.to_sql(name=table_name, con=engine, if_exists='append')


    while True:
        try:
            t_start = time()
            df= next(df_iter)

            df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
            df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], format='%Y-%m-%d %H:%M:%S')   

            df.to_sql(name = table_name, con = engine, if_exists="append")
            t_end = time()
            print("Insert Another Chunk...., took %.3f second" % (t_end - t_start))
        except StopIteration:
            print("Finish ingesting data into the postgres database")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
