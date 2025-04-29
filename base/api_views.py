from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from base.models import Category, Post, CareerForm, ContactInquiry, AftermarketForm, VehicleCategory, ProductType, Product, Newsletter, Policy
from base.serializers import (
    CategorySerializer, PostSerializer, CareerFormSerializer,
    ContactInquirySerializer, AftermarketFormSerializer, VehicleCategorySerializer, ProductTypeSerializer, ProductSerializer,
    NewsletterSerializer, PolicySerializer
)
from .swagger import (
    category_list_schema, category_detail_schema,
    post_list_schema, post_detail_schema,
    career_form_schema, contact_inquiry_schema, aftermarket_form_schema,
    vehicle_category_list_schema, vehicle_category_detail_schema,
    product_type_list_schema, product_type_detail_schema,
    product_list_schema, product_detail_schema, product_create_schema,
    product_by_type_schema, product_by_category_schema,
    career_form_list_schema, career_form_detail_schema, career_form_update_schema, career_form_delete_schema,
    contact_inquiry_list_schema, contact_inquiry_detail_schema, contact_inquiry_update_schema, contact_inquiry_delete_schema,
    aftermarket_form_list_schema, aftermarket_form_detail_schema, aftermarket_form_update_schema, aftermarket_form_delete_schema
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
    
    @career_form_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @career_form_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @career_form_update_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @career_form_update_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @career_form_delete_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ContactInquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
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
    
    @contact_inquiry_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @contact_inquiry_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @contact_inquiry_update_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @contact_inquiry_update_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @contact_inquiry_delete_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AftermarketFormViewSet(viewsets.ModelViewSet):
    queryset = AftermarketForm.objects.all()
    serializer_class = AftermarketFormSerializer
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
    
    @aftermarket_form_list_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @aftermarket_form_detail_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @aftermarket_form_update_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @aftermarket_form_update_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @aftermarket_form_delete_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

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

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Successfully subscribed to newsletter"},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"policies": serializer.data}) 