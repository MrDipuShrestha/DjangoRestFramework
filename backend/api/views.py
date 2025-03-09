from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializer import ProductSerializer

from django.forms.models import model_to_dict

from products.models import Products
# from django.http import JsonRespons


class ResponseRawData(APIView):
    
    def get(self, request):
        
        queryset = Products.objects.all().order_by("?").first()
        serializer = {}

        if queryset:
            serializer = ProductSerializer(queryset) 
        return Response(serializer.data)
