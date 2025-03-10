from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Products
from .serializer import ProductSerializer


class ProductDetialAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductCreatListeAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title

        serializer.save(content=content)


# Function based view
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            data = get_object_or_404(Products, pk=pk)
            serializer = ProductSerializer(data, many=False)
            return Response(serializer.data)
        # List view
        queryset = Products.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    if method == "POST":
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            
            if content is None:
                content = title

            serializer.save(content=content)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("invlaid data!", status=status.HTTP_400_BAD_REQUEST)

    