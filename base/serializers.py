from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Category, Post, CareerForm, ContactInquiry, AftermarketForm,
    VehicleCategory, ProductType, Product, FeatureImage, Newsletter, Policy
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    
    class Meta:
        model = Post
        fields = [
            'id', 'meta_title', 'meta_description', 'title', 'slug', 
            'date_added', 'author', 'featured_image', 'category', 'category_id',
            'intro', 'body'
        ]
        read_only_fields = ['slug']

class CareerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerForm
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'application_type', 'role_applied_for', 'current_location',
            'resume', 'message', 'agreed_to_terms'
        ]

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ['id', 'name', 'email', 'phone_number', 'message']

class AftermarketFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AftermarketForm
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'company_name', 'country', 'message'
        ]

class VehicleCategorySerializer(serializers.ModelSerializer):
    shortName = serializers.CharField(source='short_name')
    
    class Meta:
        model = VehicleCategory
        fields = ['name', 'img', 'shortName']

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name', 'img']

class FeatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureImage
        fields = ['feature_name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    vehicleCategories = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    pdf = serializers.SerializerMethodField()
    graph = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'type', 'vehicleCategories', 'image',
            'graph', 'pdf', 'specifications', 'features', 'description'
        ]
    
    def get_type(self, obj):
        return obj.type.name
    
    def get_vehicleCategories(self, obj):
        return [category.name for category in obj.vehicle_categories.all()]
    
    def get_features(self, obj):
        feature_images = obj.feature_images.all()
        features_dict = {}
        for feature in feature_images:
            features_dict[feature.feature_name] = feature.image.url if feature.image else None
        return features_dict
    
    def get_pdf(self, obj):
        return obj.pdf_file.url if obj.pdf_file else None
    
    def get_graph(self, obj):
        return obj.graph_image.url if obj.graph_image else None

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['email', 'date_subscribed']
        read_only_fields = ['date_subscribed']

class PolicySerializer(serializers.ModelSerializer):
    pdf_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Policy
        fields = ['id', 'pdf_title', 'pdf_url', 'date_added']
        read_only_fields = ['date_added']
    
    def get_pdf_url(self, obj):
        return obj.pdf_file.url if obj.pdf_file else None

