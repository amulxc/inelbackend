from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from base.models import Category, Post, CareerForm, ContactInquiry, AftermarketForm, VehicleCategory, ProductType, Product
from base.serializers import (
    CategorySerializer, PostSerializer, CareerFormSerializer,
    ContactInquirySerializer, AftermarketFormSerializer, VehicleCategorySerializer, ProductTypeSerializer, ProductSerializer
)
from .swagger import (
    category_list_schema, category_detail_schema,
    post_list_schema, post_detail_schema,
    career_form_schema, contact_inquiry_schema, aftermarket_form_schema,
    vehicle_category_list_schema, vehicle_category_detail_schema,
    product_type_list_schema, product_type_detail_schema,
    product_list_schema, product_detail_schema, product_create_schema,
    product_by_type_schema, product_by_category_schema
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
    @category_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @category_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        category = self.get_object()
        posts = Post.objects.filter(category=category)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    
    @post_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @post_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response(
                {"error": "category_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class CareerFormViewSet(viewsets.ModelViewSet):
    queryset = CareerForm.objects.all()
    serializer_class = CareerFormSerializer
    http_method_names = ['get', 'post']  # Only allow GET and POST methods
    permission_classes = [permissions.AllowAny]
    
    @career_form_schema
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Application submitted successfully"},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class ContactInquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
    http_method_names = ['get', 'post']  # Only allow GET and POST methods
    permission_classes = [permissions.AllowAny]
    
    @contact_inquiry_schema
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Inquiry submitted successfully"},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class AftermarketFormViewSet(viewsets.ModelViewSet):
    queryset = AftermarketForm.objects.all()
    serializer_class = AftermarketFormSerializer
    http_method_names = ['get', 'post']  # Only allow GET and POST methods
    permission_classes = [permissions.AllowAny]
    
    @aftermarket_form_schema
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Aftermarket inquiry submitted successfully"},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class VehicleCategoryViewSet(viewsets.ModelViewSet):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer
    permission_classes = [permissions.AllowAny]
    
    @vehicle_category_list_schema
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"vehicleCategories": serializer.data})
    
    @vehicle_category_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.AllowAny]
    
    @product_type_list_schema
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"productTypes": serializer.data})
    
    @product_type_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    
    @product_list_schema
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"products": serializer.data})
    
    @product_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @product_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @product_by_type_schema
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        type_id = request.query_params.get('type_id')
        if not type_id:
            return Response(
                {"error": "type_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        product_type = get_object_or_404(ProductType, id=type_id)
        products = Product.objects.filter(type=product_type)
        serializer = self.get_serializer(products, many=True)
        return Response({"products": serializer.data})
    
    @product_by_category_schema
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response(
                {"error": "category_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        category = get_object_or_404(VehicleCategory, id=category_id)
        products = Product.objects.filter(vehicle_categories=category)
        serializer = self.get_serializer(products, many=True)
        return Response({"products": serializer.data}) 