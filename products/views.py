from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .documents import ProductDocument
from rest_framework.permissions import IsAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        search = ProductDocument.search().query('match', name=query)
        results = search.execute()
        serializer = ProductDocumentSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)