from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import vitalSigns
from .serializers import PostVitalSignSerializer
from rest_framework import status
# Create your views here.
class PostvitalSigns(APIView):
    permission_classes=(AllowAny,)
    serializer_class=PostVitalSignSerializer
    def post(self,request):
        VSserializer=PostVitalSignSerializer(data=request.data)
        if VSserializer.is_valid():
            VSserializer.save()
            return Response({"status": "success", "data": VSserializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": VSserializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class GetvitalSigns(APIView):
    def get(self,request):
        getVS=vitalSigns.objects.filter().order_by('-id')[0]
        Current_vitalSign=getVS.vitalSignsList
        return Response (Current_vitalSign)