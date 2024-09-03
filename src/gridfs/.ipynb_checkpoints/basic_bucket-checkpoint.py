import os
import time
import bson
from pymongo import MongoClient
import gridfs
import tarfile 
import io


db_name = 'coco2017'
client = MongoClient('mongodb://127.0.0.1:37020')
db = client[db_name]
fs = gridfs.GridFS(db)
bucket = gridfs.GridFSBucket(db)


# upload
filename = '10000.tar.gz'
t0 = time.time()
with open(filename, 'rb') as f:
    data = f.read()
    file_id = bucket.upload_from_stream(filename, data)
    print (file_id)
t1 = time.time()
print (t1 - t0)

# download
t00 = time.time()
out_filename = '11111.tar.gz'
with open(out_filename, 'wb') as f:
    bucket.download_to_stream(file_id, f)
t01 = time.time()
print (t01 - t00)



