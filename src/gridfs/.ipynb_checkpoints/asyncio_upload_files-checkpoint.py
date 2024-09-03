import os
from pymongo import MongoClient
from datetime import datetime, timedelta
import time
import functools
import bson
import glob
import asyncio
import nest_asyncio
import concurrent.futures
from tqdm import tqdm
import math
import bson
from  datetime import datetime
from gridfs import GridFS, GridFSBucket
nest_asyncio.apply()


client = MongoClient('mongodb://127.0.0.1:17020')
db = client['N_TEST_GRIDFS_SYNC']
fs = GridFS(db)
bucket = GridFSBucket(db)
buckets = [GridFSBucket(db) for i in range(20)]

# get file names
video_dir = '/son/video/result_video'
mp4_files = glob.glob(os.path.join(video_dir, '*.mp4'))

worker = 20
total = len(mp4_files)

def run_upload_from_stream_with_id(filepath, idx):
    filename = os.path.basename(filepath)
    new_oid = bson.ObjectId()
    t0 = time.time()
    with open(filepath, 'rb') as f:
        file_oid = buckets[idx].upload_from_stream_with_id(new_oid, filename, f.read())
    t2 = time.time()
    
    print (f'{t2 - t0}')
#     print (new_oid, file_oid)
    
def callback(before, fut):
    after = time.time()
    print (f'Elapsed : {after - before}, {fut}')
    
    
async def run_upload_concurrent():
    with concurrent.futures.ThreadPoolExecutor(max_workers = worker) as pool:
        
        upload_futures = list()
        for idx, filepath in enumerate(mp4_files):
            idx = int(idx % 20)
            before = time.time()
            fut = pool.submit(run_upload_from_stream_with_id, filepath, idx)
            fut.add_done_callback(functools.partial(callback, before))
            upload_futures.append(fut)
            
        for future in concurrent.futures.as_completed(upload_futures):
            print (f'FUTURE RESULT : {future.result()}')
        
#         for future in upload_futures:
#             print (future.result())
            
asyncio.run(run_upload_concurrent())





