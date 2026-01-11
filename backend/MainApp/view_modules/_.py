# Test function goes here 

# Internal
from ..constants import *

# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view([METHOD_GET])
def hello_world(request):
    return Response({'hello' : 'world'}, status=status.HTTP_200_OK)

@api_view([METHOD_GET])
def hello_thing(request, url_thing):
    output = f'Hello {str(url_thing).upper()}'

    return Response({'output' : output}, status=status.HTTP_200_OK)
