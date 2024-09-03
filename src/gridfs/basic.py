import os
from pymongo import MongoClient
from datetime import datetime, timedelta
import gridfs
import time
import bson

client = MongoClient('mongodb://127.0.0.1:17020')
db = client['test']
fs = gridfs.GridFS(db)

# BASIC PUT
filepath = '/son/video/chewingdog.mp4'
filename = os.path.basename(filepath)

with open(filepath, 'rb') as f:
    data = f.read()
    t0 = time.time()
    result = fs.put(data, filename=filename)
    t1 = time.time()
print (result, t1 - t0)


# FIND
col = db['fs.files']
cursor = col.find({})
for doc in cursor:
    print (doc)

# GET 
col = db['fs.files']
cur = col.find()

for c in cur:
    t0 =time.time()
    data = fs.get(c['_id']).read() # fs.chunks
    t1 =time.time()
    file_name = c['filename']
    print (len(data))
    print (f'get, read data : {t1 - t0}')
    
    with open(file_name, 'wb') as f:
        f.write(data)
    t2 = time.time()
    
    print (f'write file : {t2 - t1}')
    
