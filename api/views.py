from time import strftime
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializer import APISerializer
from api.models import UUIDStorageModel

# Create your views here.
class FetchUUIDAPIView(APIView):
    """Fetch UUID"""

    serializer_class = APISerializer()

    def get(self, request):

        UUIDStorageModel.objects.create()
        uuids = UUIDStorageModel.objects.all().order_by('-created_datetime')
        data = dict()
        for uuid in uuids:
            data[str(uuid.created_datetime.strftime("%Y-%m-%d %H:%M:%S%z"))] = str(uuid.id)
        
        response_payload = {
            "status" : True,
            "data" : data
        }
        return Response(response_payload, status=status.HTTP_200_OK)