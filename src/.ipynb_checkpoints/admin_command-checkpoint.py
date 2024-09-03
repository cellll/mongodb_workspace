from pymongo import MongoClient


# Config server ReplSet initiate
cli = MongoClient(cfgsvr_ip, int(cfgsvr_port), directConnection=True, socketTimeoutMS=1000)
replSetConfig = {
    '_id' : 'ConfigReplSet',
    'members' : [
        {
            '_id' : 0,
            'host' : f'{cfgsvr_ip}:{cfgsvr_port}'
        }
    ]
}
try:
    result = cli.admin.command('replSetInitiate', replSetConfig)
        if isinstance(result, dict):
            if 'ok' in result:
                if result['ok'] == 1.0:
                    print (f'=> Configure Configserver')
    
except pymongo.errors.OperationFailure as ofe:
    if ofe.code == 23:
        print (ofe.details['errmsg'])
finally:
    cli.close()

print (f'=> Run Configserver')


# db, collection:  enable shard
client = MongoClient() 
client.admin.command('enableSharding',  'mongotest')
client.admin.command({'shardCollection': 'mongotest.signals', 'key': {'valueX': 1, 'valueY': 1}})
