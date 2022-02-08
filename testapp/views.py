from re import L
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class TestGetApi(APIView):
    def get(self, request):
        return Response(
            {
                "status": 200,
                "data": True
            }
        )

class TestPostApi(APIView):
    def post(self, request):
        return Response(
            {
                "data": request.data['data']
            }
        )