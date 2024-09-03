import os
import asyncio
import nest_asyncio
import motor.motor_tornado
import motor.motor_asyncio
import time
import concurrent.futures
from tqdm import tqdm
import math
nest_asyncio.apply()

_LIMIT = 1000
_LEN_LIST = 500
_NUM_WORKERS = math.ceil(_LIMIT/_LEN_LIST)

async def download(dataset_name, base_dir, data_type, file_type):
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://127.0.01:17020')
    db = client[dataset_name]
    bucket = motor.motor_asyncio.AsyncIOMotorGridFSBucket(db)
    ccol = db['fs.chunks']
    fcol = db['fs.files']

    print (f'START Download {data_type} {file_type}')
    condition = {'metadata.meta.dist_id' : {'$regex' : data_type}, 'metadata.file.type' : file_type}
    total_count = await fcol.count_documents(condition)
    print (total_count)
    cursor = bucket.find(condition)
    with tqdm(total = total_count) as pbar:
        pbar.set_description(f'Download {data_type} {file_type}')
        with concurrent.futures.ThreadPoolExecutor(max_workers=_NUM_WORKERS) as pool:
            for _ in range(math.ceil(total_count / _LIMIT)):
                all_docs = list()
                for i in range(math.ceil(_LIMIT/_LEN_LIST)):
                    docs = await cursor.to_list(length=_LEN_LIST)
                    all_docs.append(docs)
                future_save = [pool.submit(down, docs, bucket, base_dir) for docs in all_docs]
                for future in future_save:
                    future.result()
                pbar.update(_LIMIT)
            await asyncio.sleep(0.5)
            
    
def down(docs, bucket, base_dir):
    for doc in docs:
        doc_id = doc['_id']
        filename = doc['filename']
        file_dir = doc['metadata']['file']['dir']
        
#         base_dir = 'coco2017'
        dir_path = os.path.join(base_dir, file_dir)
        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path)
            except Exception as e:
                pass
        file_path = os.path.join(dir_path, filename)
        
#         print (doc['metadata']['file']['index'])
        ff = open(file_path, 'wb')
        bucket.download_to_stream(doc_id, ff)
        

t0 = time.time()
asyncio.run(download('coco2017', 'val', 'image'))
t1 = time.time()
print (t1-t0)


