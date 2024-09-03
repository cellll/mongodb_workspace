
import io
import os
import asyncio
import nest_asyncio
import motor.motor_tornado
import motor.motor_asyncio
import time
import concurrent.futures
from tqdm import tqdm
import math
import bson
from  datetime import datetime
import glob
nest_asyncio.apply()


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://127.0.0.1:17020')
db_name = 'N_TEST_GRIDFS'
db = client[db_name]
bucket = motor.motor_asyncio.AsyncIOMotorGridFSBucket(db)

video_dir = '/son/result_video'
mp4_files = glob.glob(os.path.join(video_dir, '*.mp4'))[:20]

worker = 20
total = len(mp4_files)

def run_upload_from_stream_with_id(filepath):
    filename = os.path.basename(filepath)
    new_oid = bson.ObjectId()
    with open(filepath, 'rb') as f:
        data = f.read()
    file_oid = bucket.upload_from_stream_with_id(
        new_oid, filename, io.BytesIO(data)
    )
    print (new_oid, file_oid)
    
async def run_upload_concurrent():
    with concurrent.futures.ThreadPoolExecutor(max_workers = worker) as pool:
        for loop in range(math.ceil(total / worker)):
            start = max(0, loop * worker)
            end = min((loop + 1) * worker, total)
            print (loop, start, end)
            files = mp4_files[start:end]
            pool.map(run_upload_from_stream_with_id, files)
#             upload_futures = [pool.submit(run_upload_from_stream_with_id, f, loop) for f in files]
#             for fut in upload_futures:
#                 fut.result()
#             await asyncio.sleep(0.2)

print (datetime.now())
asyncio.run(run_upload_concurrent())
print (datetime.now())




####### sync
# worker = 20
# total = len(mp4_files)

# def run_upload_from_stream_with_id(filepath, loop):
#     filename = os.path.basename(filepath)
#     new_oid = bson.ObjectId()
#     with open(filepath, 'rb') as f:
#         data = f.read()
#     file_oid = bucket.upload_from_stream_with_id(
#         new_oid, filename, io.BytesIO(data), metadata={'loop' : loop}
#     )
#     print (new_oid, file_oid)
    
# async def run_upload_concurrent():
#     with concurrent.futures.ThreadPoolExecutor(max_workers = worker) as pool:
#         for loop in range(math.ceil(total / worker)):
#             start = max(0, loop * worker)
#             end = min((loop + 1) * worker, total)
#             print (loop, start, end)
#             files = mp4_files[start:end]
#             upload_futures = [pool.submit(run_upload_from_stream_with_id, f, loop) for f in files]
#             for fut in upload_futures:
#                 fut.result()
#             await asyncio.sleep(0.2)

# print (datetime.now())
# asyncio.run(run_upload_concurrent())
# print (datetime.now())
