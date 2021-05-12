from django.views.generic import ListView
from rest_framework import viewsets, status
from .models import *
from .serializers import ProductSerializer
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    '''============Search============'''
    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        queryset = self.get_queryset().filter(Q(title__icontains=query) | Q(description__icontains=query))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''===========Filter============='''
    @action(methods=['GET'], detail=False)
    def filter(self, request):
        filter = request.query_params.get('filter')
        if filter == 'expensive-first':
            queryset = self.get_queryset().order_by('price')
        elif filter == 'cheap-first':
            queryset = self.get_queryset().order_by('-price')
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

