import time
import bson
import traceback
from datetime import datetime
from pytz import timezone

import pymongo
from pymongo import MongoClient, errors
from utils import get_basic_logger, get_db_url, get_default_db_configs

class CRUDClient:
    def __init__(self, logger=None, url='', **client_args):

        logger = get_basic_logger() if not logger else logger
        url = get_db_url() if not url else url
        client_args = get_default_db_configs() if not client_args else client_args
        
        self.logger = logger
        self.logger.debug(f'Connect to DB : {url} with configs : {client_args}')
        self.client = MongoClient(url, **client_args)
        time.sleep(1)
        if not self.client.nodes:
            self.logger.error(f'Connection Error : Invalid MongoDB url : {url}')
            raise ConnectionError(f'Invalid MongoDB url : {url}')
            
            
    """ INSERT """
    def insert_many(self, db_name:str, col_name:str, docs:list) -> dict:
        insert_result = {'status' : False, 'inserted_count' : 0, 'reason' : ''}
        
        if not docs:
            insert_result['reason'] = 'empty docs'
            return insert_result
        
        now = datetime.now(timezone('Asia/Seoul'))
        for doc in docs:
            doc['insertedTime'] = now
        
        try:
            msg = ''
            col = self.client[db_name][col_name]
            in_result = col.insert_many(docs)

            if in_result:
                insert_result['status'] = in_result.acknowledged
                insert_result['inserted_count'] = len(in_result.inserted_ids)
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}, inserted_count: {len(in_result.inserted_ids)}')
                
                
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            insert_result['reason'] = msg
            return insert_result

    
    """ UPDATE """
    def update_one(self, db_name:str, col_name:str, condition:dict, contents:dict, upsert=False) -> dict:
        update_result = {'status' : False, 'matched_count': 0, 'modified_count' : 0, 'reason' : ''}
        
        if not condition:
            update_result['reason'] = 'empty condition.'
            return update_result
        if not contents:
            update_result['reason'] = 'empty update contents.'
            return update_result
        
        try:
            msg = ''
            col = self.client[db_name][col_name]
            uo_result = col.update_one(condition, contents, upsert=upsert)
            if uo_result:
                update_result['status'] = uo_result.acknowledged
                update_result['matched_count'] = uo_result.matched_count
                update_result['modified_count'] = uo_result.modified_count
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}, matched_count: {uo_result.matched_count}, modified_count: {uo_result.modified_count}')
                    
        except errors.OperationFailure as opf:
            msg = f'[OperationFailrue] Check if condition is valid.\n{opf._message}'
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            update_result['reason'] = msg
            return update_result
        
    def update_many(self, db_name:str, col_name:str, condition:dict, contents:dict, upsert=False) -> dict:
        
        update_result = {'status' : False, 'matched_count': 0, 'modified_count' : 0, 'reason' : ''}
        
        if not condition:
            update_result['reason'] = 'empty condition.'
            return update_result
        if not contents:
            update_result['reason'] = 'empty update contents.'
            return update_result
        
        try:
            msg = ''
            col = self.client[db_name][col_name]
            um_result = col.update_many(condition, contents, upsert=upsert)
            if um_result:
                update_result['status'] = um_result.acknowledged
                update_result['matched_count'] = um_result.matched_count
                update_result['modified_count'] = um_result.modified_count
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}, matched_count: {um_result.matched_count}, modified_count: {um_result.modified_count}')
                
                    
        except errors.OperationFailure as opf:
            msg = f'[OperationFailrue] Check if condition is valid.\n{opf._message}'
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            update_result['reason'] = msg
            return update_result

    """ DELETE """
    def delete_one(self, db_name:str, col_name:str, condition:dict) -> dict:
        delete_result = {'status': False, 'deleted_count' : 0, 'reason' : ''}
        if not condition:
            delete_result['reason'] = 'empty condition.'
            return delete_result
        
        try:
            col = self.client[db_name][col_name]
            do_result = col.delete_one(condiiton)
            if do_result:
                delete_result['status'] = do_result.acknowledged
                delete_result['deleted_count'] = do_result.deleted_count
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}, deleted_count: {do_result.deleted_count}')
                
        except errors.OperationFailure as opf:
            msg = f'[OperationFailrue] Check if condition is valid.\n{opf._message}'
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            delete_result['reason'] = msg
            return delete_result
        
    def delete_many(self, db_name:str, col_name:str, condition:dict) -> dict:
        delete_result = {'status': False, 'deleted_count' : 0, 'reason' : ''}
        if not condition:
            delete_result['reason'] = 'empty condition.'
            return delete_result
        
        try:
            msg = ''
            col = self.client[db_name][col_name]
            dm_result = col.delete_many(condition)
            if dm_result:
                delete_result['status'] = dm_result.acknowledged
                delete_result['deleted_count'] = dm_result.deleted_count
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}, deleted_count: {dm_result.deleted_count}')
            
        except errors.OperationFailure as opf:
            msg = f'[OperationFailrue] Check if condition is valid.\n{opf._message}'
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            delete_result['reason'] = msg
            return delete_result
        
            
    """ FIND """
    def find_one(self, db_name:str, col_name:str, condition:dict) -> dict:
        result = { 'status' : False, 'reason' : '', 'doc' : {}}
        
        try:
            msg = ''
            col = self.client[db_name][col_name]
            doc = col.find_one(condition)
            if doc:
                if isinstance(doc['_id'], bson.ObjectId):
                    doc['_id'] = str(doc['_id'])
                result['status'] = True
                result['doc'] = doc
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}, doc count: 1')
                    
        except errors.OperationFailure as opf:
            msg = f'[OperationFailrue] Check if condition is valid.\n{opf._message}'
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            result['reason'] = msg
            return result
        
        
    def find(self, db_name:str, col_name:str, condition:dict) -> dict:
        result = { 'status' : False, 'reason' : '', 'docs' : []}
        
        try:
            msg = ''
            col = self.client[db_name][col_name]
            cursor = col.find(condition)
            for doc in cursor:
                if isinstance(doc['_id'], bson.ObjectId):
                    doc['_id'] = str(doc['_id'])
                result['docs'].append(doc)
                
            self.logger.debug(f"db_name: {db_name}, col_name: {col_name}, doc count: {len(result['docs'])}")
                
            if result['docs']:
                result['status'] = True
            else:
                msg = 'No documents found.'
                
        except errors.OperationFailure as opf:
            msg = f'[OperationFailrue] Check if condition is valid.\n{opf._message}'
        except TypeError as te:
            msg = f'[TypeError] {te}'
        except errors.ExecutionTimeout as eto:
            msg = f'[ExecutionTimeout] {eto}'
        except errors.NetworkTimeout as nto:  
            msg = f'[NetworkTimeout] {nto}'
        except errors.CursorNotFound as cnf:
            msg = f'[CursorNotFound] {cnf}'
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            result['reason'] = msg
            return result
        
        
    def create_collection(self, db_name:str, col_name:str) -> dict:
        
        create_result = {'status' : False, 'reason' : ''}
        
        try:
            # 1. create collection
            msg = ''
            db = self.client[db_name]
            created_col = db.create_collection(
                name = col_name,
                clusteredIndex = {
                    'key' : {'_id' : 1},
                    'unique' : True
                }
            )
            
            if isinstance(created_col, pymongo.collection.Collection):
                create_result['status'] = True
                self.logger.debug(f'db_name: {db_name}, col_name: {col_name}')
                
#             # 2. create index
#             index_result = created_col.create_index([('_id', 'hashed')])
#             self.logger.debug(index_result)
                
            # 3. enable sharding
            enable_result = self.client.admin.command('enableSharding', db_name)
            self.logger.debug(enable_result)
            
            # 4. shard collection
            shard_result = self.client.admin.command({'shardCollection': f'{db_name}.{col_name}', 'key': {'_id': 1}})
            self.logger.debug(shard_result)
                
        except pymongo.errors.CollectionInvalid as cie:
            msg = f'[CollectionInvalid] {cie}'
            create_result['status'] = True
        except Exception as e:
            msg = f'[{type(e)}] {e}'
        finally:
            create_result['reason'] = msg
            return create_result
        
    def list_collection_names(self, db_name:str) -> list:
        
        list_result = {'status' : False, 'reason' : '', 'collection_names' : []}
        
        try:
            msg = ''
            db = self.client[db_name]
            collection_names = db.list_collection_names()
            
            if collection_names:
                list_result['status'] = True
                list_result['collection_names'].extend(collection_names)
            
         except Exception as e:
            msg = f'[{type(e)}] {e}'
            
        finally:
            list_result['reason'] = msg
            return list_result
        
        
    def count_documents(self, db_name:str, col_name:str) -> dict:
        
        count_result = {'status' : False, 'reason' : '', 'doc_count' : 0}
        try:
            msg = ''
            col = self.client[db_name][col_name]
            count = col.count_documents({})
            
            if count:
                count_result['status'] = True
                count_result['doc_count'] = count
            
        except Exception as e:
            msg = f'[{type(e)}] {e}'
            
        finally:
            count_result['reason'] = msg
            return count_result
        
        
