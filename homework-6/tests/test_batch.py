import batch
import pandas as pd
from datetime import datetime

def test_prepare_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2), dt(1, 10)),
        (1, 2, dt(2, 2), dt(2, 3)),
        (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),     
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    actual_df = batch.prepare_data(pd.DataFrame(data, columns=columns))

    expected_df = pd.DataFrame({
        'PULocationID': ['-1', '1', '1'], 
        'DOLocationID': ['-1', '-1', '2'],
        'tpep_pickup_datetime': [dt(1, 2), dt(1, 2), dt(2, 2)],
        'tpep_dropoff_datetime': [dt(1, 10), dt(1, 10), dt(2, 3)],
        'duration': [8.0, 8.0, 1.0]
    })

    assert expected_df.equals(actual_df)

def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)