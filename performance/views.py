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



@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,JSONRenderer))
@permission_classes((AllowAny,))
@csrf_exempt
def vendor_prefomance(request):
    from purchase.utils import vendor_prefomance_util
    message,status_code = vendor_prefomance_util()
    if status_code == 400:
        return HttpResponse( {message}, status=status_code)
    else:    
        return HttpResponse(json.dumps({'message' : message,'status':status_code}), content_type="application/json") 
