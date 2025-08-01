from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Category, Post, CareerForm, ContactInquiry, AftermarketForm,
    VehicleCategory, ProductType, Product, FeatureImage, Newsletter, Policy ,InvestorTabHeading,InvestorSubheading,InvestorSubheadingContent
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
    types = serializers.SerializerMethodField()
    vehicleCategories = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    pdf = serializers.SerializerMethodField()
    graph = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'types', 'vehicleCategories', 'image',
            'graph', 'pdf', 'specifications', 'features', 'description'
        ]
    
    def get_types(self, obj):
        return [type_obj.name for type_obj in obj.types.all()]
    
    def get_vehicleCategories(self, obj):
        return [category.name for category in obj.vehicle_categories.all()]
    
    def get_features(self, obj):
        request = self.context.get('request')
        feature_images = obj.feature_images.all()
        features_dict = {}
        for feature in feature_images:
            if feature.image:
                features_dict[feature.feature_name] = request.build_absolute_uri(feature.image.url)
            else:
                features_dict[feature.feature_name] = None
        return features_dict
    
    def get_pdf(self, obj):
        request = self.context.get('request')
        if obj.pdf_file:
            return request.build_absolute_uri(obj.pdf_file.url)
        return None
    
    def get_graph(self, obj):
        request = self.context.get('request')
        if obj.graph_image:
            return request.build_absolute_uri(obj.graph_image.url)
        return None
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

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
        request = self.context.get('request')
        if obj.pdf_file:
            return request.build_absolute_uri(obj.pdf_file.url)
        return None

class InvestorSubheadingContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorSubheadingContent
        fields = [
            'id',
            'title',
            'pdf_name',
            'link',
            'editor_content',
        ]


class InvestorSubheadingSerializer(serializers.ModelSerializer):
    contents = InvestorSubheadingContentSerializer(many=True, read_only=True)

    class Meta:
        model = InvestorSubheading
        fields = [
            'id',
            'name',
            'contents',
        ]


class InvestorTabHeadingSerializer(serializers.ModelSerializer):
    subheadings = InvestorSubheadingSerializer(many=True, read_only=True)

    class Meta:
        model = InvestorTabHeading
        fields = [
            'id',
            'name',
            'link',
            'subheadings',
        ]