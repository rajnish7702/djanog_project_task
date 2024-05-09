import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
import datetime
from VendorManagementSystem import settings as s
import pickle
import redis
import pymongo
import redis
import pickle
import datetime
from VendorManagementSystem.settings import *
from sklearn.model_selection import train_test_split
from cryptography.fernet import Fernet



MONGO_COLLECTIONS = {MONGO_COLLECTION_PARTS: "parts"}


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return obj




def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance



@singleton
class CacheHelper:
    def __init__(self):
        self.redis_cache = redis.StrictRedis(
            host=REDIS_CLIENT_HOST, port=REDIS_CLIENT_PORT, db=0, socket_timeout=1
        )
        print("REDIS CACHE UP!")

    def get_redis_pipeline(self):
        return self.redis_cache.pipeline()

    def set_json(self, dict_obj):
        try:
            k, v = list(dict_obj.items())[0]
            v = pickle.dumps(v)
            return self.redis_cache.set(k, v)
        except redis.ConnectionError:
            return None

    def get_json(self, key):
        try:
            temp = self.redis_cache.get(key)
            # print(temp)
            if temp:
                try:
                    temp = pickle.loads(temp)
                except:
                    temp = json.loads(temp.decode())
            return temp
        except redis.ConnectionError:
            return None
        return None

    def execute_pipe_commands(self, commands):
        return None


@singleton
class LocalMongoHelper:
    client = None

    def __init__(self):
        if not self.client:
            self.client = MongoClient(host=MONGO_SERVER_HOST, port=MONGO_SERVER_PORT)
        self.db = self.client[MONGO_DB]
        self.DB = None
        self.db_cname = None

    def getDatabase(self):
        return self.db
             

    def create_index(self, collection_name, field_name):
        self.getCollection(collection_name).create_index(
            [(field_name, pymongo.TEXT)],
            name="search_index",
            default_language="english",
        )

    def getCollection(
        self, cname, create=False, codec_options=None, domain_override=None
    ):
        _DB = MONGO_DB
        
        
        self.DB = self.client[_DB]

        
        if cname is not None:
            if domain_override:
                cname = domain_override + cname
                # print(cname)
            else:
                cname =  cname
                
        if cname in MONGO_COLLECTIONS:
            if codec_options:
                self.db_cname = self.DB.get_collection(
                    MONGO_COLLECTIONS[cname], codec_options=codec_options
                )
            self.db_cname = self.DB[MONGO_COLLECTIONS[cname]]
        else:
            self.db_cname = self.DB[cname]
        print('##############################')
        print(self.db_cname)
        return self.db_cname
    

    def get_data(self, collection_name):
       
        collection_name = MONGO_DB + collection_name
        mycoll = self.db[collection_name]
        data = [x for x in mycoll.find()]
        return data

    def collection_checker_util(self, cname):
        _DB = MONGO_DB
        self.DB = self.client[_DB]
        # collectionExists = self.DB.listCollectionNames().into(new ArrayList()).contains(testCollectionName)
        collectionExists = self.DB.list_collection_names()
        # print(collectionExists)
        collection_name = "vendor" + cname
        # print('collection_checkr_util_checking the recipie',collection_name,collectionExists)
        if collection_name in collectionExists:
            return True
        else:
            return False


