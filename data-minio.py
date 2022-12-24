from io import BytesIO
import pandas as pd
from minio import Minio

minioClient = Minio('127.0.0.1:9000',
            access_key='minioadmin',
            secret_key='minioadmin',
            secure=False)

df = pd.DataFrame()
csv_bytes = df.to_csv().encode('utf-8')
csv_buffer = BytesIO(csv_bytes)

minioClient.result = minioClient.fput_object("bigdataku", "ted", "20221013_ted_talks.csv", content_type="application/csv",)

print("Upload dataset ke minio berhasil!")

