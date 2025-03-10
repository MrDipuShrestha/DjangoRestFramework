from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializer import ProductSerializer
from rest_framework import status

from django.forms.models import model_to_dict

from products.models import Products
from django.http import JsonResponse


class ResponseRawData(APIView):
    # def get(self, request):
        
    #     queryset = Products.objects.all().order_by("?").first()
    #     serializer = {}

    #     if queryset:
    #         serializer = ProductSerializer(queryset) 
    #     return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("invlaid data!", status=status.HTTP_400_BAD_REQUEST)