from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from rest_framework import status
from django.core.cache import cache
import json


class GetStock(APIView):
    def get(self, request):
        json_data = cache.get("Data")
        if json_data:
            stock_data = json.loads(json_data)
        else:
            return Response(data={"message": "Data Empty"}, status=status.HTTP_404_NOT_FOUND)

        return Response(data=stock_data, status=status.HTTP_200_OK)
