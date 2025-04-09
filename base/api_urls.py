from rest_framework.routers import DefaultRouter
from django.urls import path, include
from base import api_views

# Create a custom router that doesn't generate nested routes
class NoNestedRouter(DefaultRouter):
    def get_nested_routes(self, parent_prefix, lookup, parent_lookup, parent_prefix2):
        return []

router = NoNestedRouter(trailing_slash=False)
router.register(r'aftermarket', api_views.AftermarketFormViewSet, basename='aftermarket')
router.register(r'categories', api_views.CategoryViewSet, basename='category')
router.register(r'posts', api_views.PostViewSet, basename='post')
router.register(r'career', api_views.CareerFormViewSet, basename='career')
router.register(r'contact', api_views.ContactInquiryViewSet, basename='contact')
router.register(r'vehicle-categories', api_views.VehicleCategoryViewSet, basename='vehicle-category')
router.register(r'product-types', api_views.ProductTypeViewSet, basename='product-type')
router.register(r'products', api_views.ProductViewSet, basename='product')

app_name = 'api'
