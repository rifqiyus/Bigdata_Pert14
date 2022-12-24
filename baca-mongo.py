import pymongo
import pandas as pd
from pymongo import MongoClient
client = MongoClient()
db = client.dbBigDataku
collection = db.colBigDataku
data = pd.DataFrame(list(collection.find()))
print(data)