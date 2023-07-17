import pandas as pd
import batch
from datetime import datetime
import os

def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)

year=2022
month=1

data = [
    (None, None, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2), dt(1, 10)),
    (1, 2, dt(2, 2), dt(2, 3)),
    (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
    (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),     
]

endpoint_url = os.getenv('S3_ENDPOINT_URL')

options = {
    'client_kwargs': {
        'endpoint_url': endpoint_url
    }
}

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df_input = pd.DataFrame(data, columns=columns)

df_input.to_parquet(
    batch.get_input_path(year, month),
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)

os.system(f"python batch.py {year} {month}")

df_actual = pd.read_parquet(batch.get_output_path(year, month), storage_options=options)

