from ast import operator
from django.core import serializers
from django.forms.models import model_to_dict
import uuid
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate
from bson.objectid import ObjectId

from comman.utils import *
from VendorManagementSystem.settings import *
from rest_framework.authtoken.models import Token


def createn_purchase_orders_util(data):
    try:
        delivery_date = datetime.datetime.now()
        data["delivery_date:"]=delivery_date
        LocalMongoHelper().getCollection(PURCHASE_COLLECTION).insert_one(data)
        return "user created",200
    except Exception as e:
        return "feild creating",401
    


def get_all_purchase_orders_util():
    try:
        all_profil = LocalMongoHelper().getCollection(PURCHASE_COLLECTION).find({},{"_id":0})
        all_profile_details = []
        for details in all_profil:
            all_profile_details.append(details)
        return all_profile_details,200
    except Exception as e:
        return "feild creating",401
    

def get_one_purchase_orders_util(_id):
    try:
        user_detaild = LocalMongoHelper().getCollection(PURCHASE_COLLECTION).find_one({"_id":ObjectId(_id)},{"_id":0})
        return user_detaild,200
    except Exception as e:
        return "feilds getting id",401
    

def update_purchase_orders_util(_id,values):
    try:
        LocalMongoHelper().getCollection(PURCHASE_COLLECTION).update_one({"_id":ObjectId(_id)},{ "$set": values})
        user_detaild = LocalMongoHelper().getCollection(PURCHASE_COLLECTION).find_one({"_id":ObjectId(_id)},{"_id":0})
        return user_detaild,200
    
    except Exception as e:
        return "feilds getting id",401
def delete_purchase_orders_util(_id):
    try:
        LocalMongoHelper().getCollection(PURCHASE_COLLECTION).delete_one({"_id":ObjectId(_id)})
        return "selected recode is deleted",200
    except Exception as e:
        return "feild delete Id",401