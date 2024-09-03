import os
import time
import bson
from pymongo import MongoClient
import gridfs
import tarfile 
import io


db_name = 'coco2017'
client = MongoClient('mongodb://127.0.0.1:17020')
db = client[db_name]
fs = gridfs.GridFS(db)
bucket = gridfs.GridFSBucket(db)

fcol = db['fs.files']
ccol = db['fs.chunks']


# find, write 
cursor = fcol.find(condition).limit(10000)
t0 = time.time()
with tarfile.open('aa/train.tar.gz', 'w:gz') as tar:
    for i, doc in enumerate(cursor):
        doc_id = doc['_id']
        filename = doc['filename']
        
        data = fs.get(doc['_id']).read()
        
        tarinfo = tarfile.TarInfo(filename)
        bio = io.BytesIO()
        bio.write(data)
        tarinfo.size = bio.tell()
        bio.seek(0)
        tar.addfile(tarinfo, bio)
t1 = time.time()
print (t1 - t0)
