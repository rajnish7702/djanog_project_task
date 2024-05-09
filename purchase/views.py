from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.http import HttpResponse
import json
from django.contrib.auth.models import Group, Permission
from rest_framework import status
from rest_framework.response import Response


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import get_object_or_404
import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from comman.utils import LocalMongoHelper
from rest_framework.permissions import AllowAny



@api_view(['POST'])
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
@permission_classes((AllowAny,))
@csrf_exempt
def createn_purchase_orders(request):

    data = json.loads(request.body)
    from purchase.utils import createn_purchase_orders_util
    message,status_code = createn_purchase_orders_util(data)
    if status_code == 400:
        return HttpResponse( {message}, status=status_code)
    else:    
        return HttpResponse(json.dumps({'message' : message,'status':status_code}), content_type="application/json") 


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
@permission_classes((AllowAny,))
@csrf_exempt
def get_all_purchase_orders(request):

    from purchase.utils import get_all_purchase_orders_util
    message,status_code = get_all_purchase_orders_util()
    if status_code == 400:
        return HttpResponse( {message}, status=status_code)
    else:    
        return HttpResponse(json.dumps({'message' : message,'status':status_code}), content_type="application/json") 



@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
@permission_classes((AllowAny,))
@csrf_exempt
def get_one_purchase_orders(request,_id):
    
    from purchase.utils import get_one_purchase_orders_util
    message,status_code = get_one_purchase_orders_util(_id)
    if status_code == 400:
        return HttpResponse( {message}, status=status_code)
    else:    
        return HttpResponse(json.dumps({'message' : message,'status':status_code}), content_type="application/json") 



@api_view(['PUT'])
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
@permission_classes((AllowAny,))
@csrf_exempt
def update_purchase_orders(request,_id):
    data = json.loads(request.body)
    value = data.get("values")
    from purchase.utils import update_purchase_orders_util
    message,status_code = update_purchase_orders_util(_id,value)
    if status_code == 400:
        return HttpResponse( {message}, status=status_code)
    else:    
        return HttpResponse(json.dumps({'message' : message,'status':status_code}), content_type="application/json") 


@api_view(['DELETE'])
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
@permission_classes((AllowAny,))
@csrf_exempt
def delete_purchase_orders(request,_id):
    
    from purchase.utils import delete_purchase_orders_util
    message,status_code = delete_purchase_orders_util(_id)
    if status_code == 400:
        return HttpResponse( {message}, status=status_code)
    else:    
        return HttpResponse(json.dumps({'message' : message,'status':status_code}), content_type="application/json") 
