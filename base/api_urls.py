from rest_framework.routers import DefaultRouter
from .api_views import (
    CategoryViewSet, PostViewSet, CareerFormViewSet,
    ContactInquiryViewSet, AftermarketFormViewSet,
    VehicleCategoryViewSet, ProductTypeViewSet, ProductViewSet,
    NewsletterViewSet, PolicyViewSet ,InvestorViewSet
)

# Create a custom router that doesn't generate nested routes
class NoNestedRouter(DefaultRouter):
    def get_nested_routes(self, parent_prefix, lookup, parent_lookup, parent_prefix2):
        return []

router = NoNestedRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'career', CareerFormViewSet)
router.register(r'contact', ContactInquiryViewSet)
router.register(r'aftermarket', AftermarketFormViewSet)
router.register(r'vehicle-categories', VehicleCategoryViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'newsletter', NewsletterViewSet)
router.register(r'policies', PolicyViewSet)
router.register(r'investor', InvestorViewSet)

app_name = 'api'
