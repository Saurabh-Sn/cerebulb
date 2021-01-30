from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import categorySerializer, ProductSerializer, ListCategorySerializer, ListProductSerializer
from .models import Product, Category


class CategoryView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = categorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        serializer = categorySerializer
        if self.action == 'list' or self.action == 'retrieve':
            serializer = ListCategorySerializer
        return serializer

    @action(methods=['DELETE'], detail=False, url_path='category/(?P<pk>\d+)', url_name='delete')
    def delete_category(self, request, pk=None):
        category = get_object_or_404(Category, id=pk)
        category.is_deleted = True
        category.update()
        for products in category.product.all():
            products.is_deleted = True
            products.update()
        return Response({'messages': 'deleted successful.'}, status=status.HTTP_204_NO_CONTENT)


class ProductView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.filter(is_deleted=False)

    def get_queryset(self):
        queryset = Product.objects.filter(is_deleted=False)
        if 'mf_year' in self.request.query_params:
            queryset = queryset.filter(product_mfg_date__year=mf_year)
        return queryset

    def get_serializer_class(self):
        serializer = ProductSerializer
        if self.action == 'list' or self.action == 'retrieve':
            serializer = ListProductSerializer
        return serializer

    @action(methods=['DELETE'], detail=False, url_path='product/(?P<pk>\d+)', url_name='delete')
    def delete_product(self, request, pk=None):
        product = get_object_or_404(Product, id=pk)
        product.is_deleted = True
        product.update()
        return Response({'messages': 'deleted successful.'}, status=status.HTTP_204_NO_CONTENT)


