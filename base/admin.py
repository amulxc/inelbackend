from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import (
    # Blog
    Category, Post,
    
    # Forms
    CareerForm, ContactInquiry, AftermarketForm,
    
    # Products
    VehicleCategory, ProductType, Product, FeatureImage,
    
    # Newsletter & Policies
    Newsletter, Policy,

    # Investor Section
    InvestorTabHeading, InvestorSubheading, InvestorSubheadingContent
)

# -------------------------------
# 📝 Blog Admin
# -------------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'name': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date_added')
    list_filter = ('category', 'author', 'date_added')
    search_fields = ('title', 'meta_title', 'meta_description', 'intro', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_added'
    ordering = ('-date_added',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category', 'date_added')
        }),
        ('SEO Information', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Content', {
            'fields': ('featured_image', 'intro', 'body')
        }),
    )

# -------------------------------
# 📩 Form Submissions Admin
# -------------------------------

@admin.register(CareerForm)
class CareerFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role_applied_for', 'application_type')
    list_filter = ('application_type', 'role_applied_for')
    search_fields = ('first_name', 'last_name', 'email', 'role_applied_for')

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'message')

@admin.register(AftermarketForm)
class AftermarketFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company_name', 'country')
    list_filter = ('country',)
    search_fields = ('first_name', 'last_name', 'email', 'company_name', 'country', 'message')

# -------------------------------
# 🚗 Products Admin
# -------------------------------

@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ('name', 'short_name')

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FeatureImageInline(admin.TabularInline):
    model = FeatureImage
    extra = 1
    fields = ('feature_name', 'image', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'pdf_file')
    list_filter = ('type', 'vehicle_categories')
    search_fields = ('id', 'name', 'description')
    filter_horizontal = ('vehicle_categories',)
    inlines = [FeatureImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'name', 'type', 'vehicle_categories')
        }),
        ('Media Files', {
            'fields': ('image', 'graph_image', 'pdf_file'),
            'description': 'Upload product images to static/products/images/, graphs to static/products/graphs/, and PDFs to static/products/pdfs/'
        }),
        ('Details', {
            'fields': ('specifications', 'description')
        }),
    )

@admin.register(FeatureImage)
class FeatureImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'feature_name', 'image')
    list_filter = ('product',)
    search_fields = ('product__name', 'feature_name', 'description')
    raw_id_fields = ('product',)

# -------------------------------
# 📰 Newsletter & Policy Admin
# -------------------------------

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    readonly_fields = ('date_subscribed',)
    ordering = ('-date_subscribed',)

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('pdf_title', 'date_added')
    search_fields = ('pdf_title',)
    readonly_fields = ('date_added',)
    ordering = ('-date_added',)

# -------------------------------
# 📊 Investor Section Admin
# -------------------------------

class InvestorSubheadingContentForm(forms.ModelForm):
    use_editor = forms.BooleanField(
        required=False, 
        initial=False,
        label="Use Rich Text Editor",
        help_text="Check this to enable the rich text editor for content"
    )
    
    class Meta:
        model = InvestorSubheadingContent
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If the instance has editor_content, check the use_editor by default
        if self.instance and self.instance.pk and self.instance.editor_content:
            self.fields['use_editor'].initial = True

    class Media:
        js = ('admin/js/investor_content_admin.js',)
        css = {
            'all': ('admin/css/investor_content_admin.css',)
        }

# Inline form without rich text editor - just basic fields
class InvestorSubheadingContentInline(admin.TabularInline):
    model = InvestorSubheadingContent
    extra = 1
    fields = ('title', 'pdf_name', 'link')  # Removed use_editor and editor_content
    verbose_name = "Content Item"
    verbose_name_plural = "Investor Subheading Contents (Show)"
    
    class Media:
        css = {
            'all': ('admin/css/investor_content_admin.css',)
        }

@admin.register(InvestorTabHeading)
class InvestorTabHeadingAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name', 'link')

@admin.register(InvestorSubheading)
class InvestorSubheadingAdmin(admin.ModelAdmin):
    list_display = ('tab_heading', 'name', 'content_count')
    search_fields = ('tab_heading__name', 'name')
    inlines = [InvestorSubheadingContentInline]
    
    def content_count(self, obj):
        count = obj.contents.count()
        return format_html(
            '<span style="background-color: #4CAF50; color: white; padding: 2px 6px; border-radius: 3px;">{}</span>',
            count
        )
    content_count.short_description = 'Content Items'

@admin.register(InvestorSubheadingContent)
class InvestorSubheadingContentAdmin(admin.ModelAdmin):
    form = InvestorSubheadingContentForm
    list_display = ('subheading', 'title', 'pdf_name', 'link', 'has_editor_content')
    search_fields = ('subheading__name', 'title', 'pdf_name', 'link')
    raw_id_fields = ('subheading',)
    list_filter = ('subheading__tab_heading',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('subheading', 'title', 'pdf_name', 'link')
        }),
        ('Rich Text Content', {
            'fields': ('use_editor', 'editor_content'),
            'classes': ('collapse',),
            'description': 'Check "Use Rich Text Editor" to enable the rich text editor below'
        }),
    )
    
    def has_editor_content(self, obj):
        if obj.editor_content and obj.editor_content.strip():
            return format_html(
                '<span style="color: green;">✓ Yes</span>'
            )
        return format_html(
            '<span style="color: #999;">✗ No</span>'
        )
    has_editor_content.short_description = 'Has Content'
