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


def vendor_prefomance_util(data):
    try:
        pass
    except Exception as e:
        return "feild to retrive",401