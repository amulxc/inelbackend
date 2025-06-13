from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.core.exceptions import ValidationError


###########################################################################################################
# Products
###########################################################################################################

class VehicleCategory(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/products/categories/')
    short_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/products/types/')
    
    def __str__(self):
        return self.name

class FeatureImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='feature_images')
    feature_name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='static/products/features/')
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('product', 'feature_name')
        ordering = ['feature_name']

    def __str__(self):
        return f"{self.feature_name} - {self.product.name}"

class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    vehicle_categories = models.ManyToManyField(VehicleCategory)
    image = models.ImageField(upload_to='static/products/images/')
    graph_image = models.ImageField(upload_to='static/products/graphs/', blank=True, null=True, help_text="Upload product graph or chart image")
    pdf_file = models.FileField(upload_to='static/products/pdfs/', blank=True, null=True, help_text="Upload product PDF documentation")
    
    # Specifications stored as JSON
    specifications = models.JSONField()
    
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_features(self):
        """Helper method to get all features for this product"""
        return self.feature_images.all()


############################################################################################################
# Blog
############################################################################################################

class Category(models.Model):
     name = models.CharField(max_length=200)
     
     def __str__(self):
        return self.name

class Post(models.Model):
   meta_title = models.CharField(max_length=200, blank=True, null=True)
   meta_description = models.TextField(blank=True, null=True)
   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="Leave it for auto slug ")
   date_added = models.DateField()  
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   featured_image = models.ImageField(upload_to='static/blog/images/', blank=False, null=False)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Used ForeignKey here
   intro = models.TextField(max_length=600)
   body = RichTextUploadingField(blank=False, null=False)
  
   
   def save(self, *args, **kwargs):
        if not self.slug:
            # Generate the slug based on the title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
   
   
   def __str__(self):
        return self.title

   class Meta:
       ordering = ['-date_added']



############################################################################################################
# Forms
############################################################################################################

class CareerForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    
    application_type = models.CharField(max_length=100)
    role_applied_for = models.CharField(max_length=255)
    
    current_location = models.CharField(max_length=255)
    
    resume = models.FileField(upload_to='resumes/', max_length=500)
    
    message = models.TextField(blank=True, null=True)

    agreed_to_terms = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Job Application by {self.first_name} {self.last_name} for {self.role_applied_for}"


class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    message = models.TextField()

    def __str__(self):
        return f"Inquiry from {self.name}"


class AftermarketForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    company_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100)

    message = models.TextField()

    def __str__(self):
        return f"Aftermarket Inquiry from {self.first_name} {self.last_name}"

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Policy(models.Model):
    pdf_title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='static/policies/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pdf_title



class InvestorTabHeading(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Investor Tab Heading"
        verbose_name_plural = "Investor Tab Headings"

    def __str__(self):
        return self.name


class InvestorSubheading(models.Model):
    tab_heading = models.ForeignKey(InvestorTabHeading, on_delete=models.CASCADE, related_name='subheadings')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Investor Subheading"
        verbose_name_plural = "Investor Subheadings"

    def __str__(self):
        return f"{self.name} ({self.tab_heading.name})"


class InvestorSubheadingContent(models.Model):

    subheading = models.ForeignKey(InvestorSubheading, on_delete=models.CASCADE, related_name='contents')


    title = models.CharField(max_length=255, blank=True, null=True)
    pdf_name = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    editor_content = RichTextUploadingField(blank=True, null=True)

    class Meta:
        verbose_name = "Investor Subheading Content"
        verbose_name_plural = "Investor Subheading Contents"

    def __str__(self):
        return self.title or self.pdf_name or "Investor Content"