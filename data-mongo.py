import pymongo
from io import BytesIO
import pandas as pd
from minio import Minio

client = Minio('127.0.0.1:9000',
            access_key='minioadmin',
            secret_key='minioadmin',
            secure=False)

clientMongo = pymongo.MongoClient("mongodb://localhost:27017")
db = clientMongo["dbBigDataku"]
col = db["colBigDataku"]
response = client.get_object("bigdataku", "ted")
data = pd.DataFrame(pd.read_csv(response))
data = data.to_dict(orient="records")
col.insert_many(data)
print ("Upload object ke mongodb berhasil")

