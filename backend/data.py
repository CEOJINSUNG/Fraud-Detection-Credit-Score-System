import sys
import requests
import base64
import json
import boto3
import csv
from datetime import datetime, timezone, timedelta
import pandas as pd
from backend.settings import MY_AWS_ACCESS_KEY_ID, MY_AWS_SECRET_ACCESS_KEY

def main():
    transaction = []
    s3 = boto3.resource(
        "s3",
        aws_access_key_id = MY_AWS_ACCESS_KEY_ID,
        aws_secret_access_key = MY_AWS_SECRET_ACCESS_KEY
    )
    k = 0
    j = 0
    with open("../data/PS_20174392719_1491204439457_log.csv") as f:
        raw =  csv.DictReader(f)

        for row in raw:
            if k < 50:
                transaction.append(row)
                k = k + 1
            else:
                df = pd.DataFrame.from_dict(transaction)
                df.to_parquet("transaction.parquet", engine="pyarrow", compression="snappy")
                thing = s3.Object("jinsung-fraud-detection", "transaction/dt={}/transaction.parquet".format(j))
                data = open("transaction.parquet", "rb")
                thing.put(Body = data)
                transaction.clear()
                j = j + 1

    # 63.5MB 정도의 데이터가 들어감
    # kor_time = timezone(timedelta(hours = 9.0))
    # dt = datetime.now(kor_time).strftime("%Y-%m-%d-%H-%M-%S")
    return 0

if __name__ == "__main__":
    main()