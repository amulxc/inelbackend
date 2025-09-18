from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from base.models import (
    Category, Post, CareerForm, ContactInquiry, AftermarketForm,
    VehicleCategory, ProductType, Product, Newsletter, Policy,InvestorTabHeading,InvestorSubheading,InvestorSubheadingContent
)
from base.serializers import (
    CategorySerializer, PostSerializer, CareerFormSerializer,
    ContactInquirySerializer, AftermarketFormSerializer,
    VehicleCategorySerializer, ProductTypeSerializer, ProductSerializer,
    NewsletterSerializer, PolicySerializer,InvestorTabHeadingSerializer,InvestorSubheadingSerializer,InvestorSubheadingContentSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
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
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
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
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ContactInquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
    permission_classes = [permissions.AllowAny]
    
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
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AftermarketFormViewSet(viewsets.ModelViewSet):
    queryset = AftermarketForm.objects.all()
    serializer_class = AftermarketFormSerializer
    permission_classes = [permissions.AllowAny]
    
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
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VehicleCategoryViewSet(viewsets.ModelViewSet):
    queryset = VehicleCategory.objects.all().order_by('order')
    serializer_class = VehicleCategorySerializer
    permission_classes = [permissions.AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"vehicleCategories": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all().order_by('order')
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"productTypes": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('order')  # Order by order field      
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        # Check if we should use scooter ordering
        use_scooter_order = request.query_params.get('use_scooter_order', '').lower() == 'true'
        
        if use_scooter_order:
            # Filter for Scooter applications and order by scooter_order
            queryset = queryset.filter(
                vehicle_categories__name__icontains='Scooter'
            ).distinct().order_by('scooter_order', 'order')
        else:
            # Use default ordering
            queryset = queryset.order_by('order')
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({"products": serializer.data})
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        type_ids = request.query_params.get('type_ids', '').split(',')
        type_ids = [tid.strip() for tid in type_ids if tid.strip()]
        
        if not type_ids:
            return Response(
                {"error": "type_ids parameter is required (comma-separated list)"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Filter products that have ANY of the specified types
        products = Product.objects.filter(types__id__in=type_ids).distinct()
        serializer = self.get_serializer(products, many=True)
        return Response({"products": serializer.data})
    
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
    
    @action(detail=False, methods=['get'])
    def scooter_applications(self, request):
        """
        Get products that belong to Scooter vehicle category, ordered by scooter_order field.
        This provides specialized ordering for Scooter applications while keeping existing order intact.
        """
        # Filter products that have 'Scooter' in their vehicle categories
        products = Product.objects.filter(
            vehicle_categories__name__icontains='Scooter'
        ).distinct().order_by('scooter_order', 'order')
        
        serializer = self.get_serializer(products, many=True)
        return Response({"scooter_products": serializer.data})

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
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"policies": serializer.data}) 
    
class InvestorViewSet(viewsets.ModelViewSet):
    queryset = InvestorTabHeading.objects.all()
    serializer_class = InvestorTabHeadingSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class InvestorSubheadingViewSet(viewsets.ModelViewSet):
    queryset = InvestorSubheading.objects.all().order_by('order')
    serializer_class = InvestorSubheadingSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'])
    def update_order(self, request):
        """
        Update the order of multiple InvestorSubheading items.
        Expects a list of objects with 'id' and 'order' fields.
        """
        try:
            order_data = request.data.get('order_data', [])
            if not isinstance(order_data, list):
                return Response(
                    {"error": "order_data must be a list"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update each item's order
            for item_data in order_data:
                item_id = item_data.get('id')
                new_order = item_data.get('order')
                
                if item_id is None or new_order is None:
                    return Response(
                        {"error": "Each item must have 'id' and 'order' fields"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                try:
                    subheading = InvestorSubheading.objects.get(id=item_id)
                    subheading.order = new_order
                    subheading.save()
                except InvestorSubheading.DoesNotExist:
                    return Response(
                        {"error": f"InvestorSubheading with id {item_id} not found"},
                        status=status.HTTP_404_NOT_FOUND
                    )
            
            return Response({"message": "Order updated successfully"})
            
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class InvestorSubheadingContentViewSet(viewsets.ModelViewSet):
    queryset = InvestorSubheadingContent.objects.all().order_by('order')
    serializer_class = InvestorSubheadingContentSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'])
    def update_order(self, request):
        """
        Update the order of multiple InvestorSubheadingContent items.
        Expects a list of objects with 'id' and 'order' fields.
        """
        try:
            order_data = request.data.get('order_data', [])
            if not isinstance(order_data, list):
                return Response(
                    {"error": "order_data must be a list"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Update each item's order
            for item_data in order_data:
                item_id = item_data.get('id')
                new_order = item_data.get('order')
                
                if item_id is None or new_order is None:
                    return Response(
                        {"error": "Each item must have 'id' and 'order' fields"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                try:
                    content = InvestorSubheadingContent.objects.get(id=item_id)
                    content.order = new_order
                    content.save()
                except InvestorSubheadingContent.DoesNotExist:
                    return Response(
                        {"error": f"InvestorSubheadingContent with id {item_id} not found"},
                        status=status.HTTP_404_NOT_FOUND
                    )
            
            return Response({"message": "Content order updated successfully"})
            
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )