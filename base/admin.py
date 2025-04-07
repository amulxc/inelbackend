from django.contrib import admin
from .models import Category, Post, CareerForm, ContactInquiry, AftermarketForm

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

@admin.register(CareerForm)
class CareerFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role_applied_for', 'application_type')
    list_filter = ('application_type', 'role_applied_for')
    search_fields = ('first_name', 'last_name', 'email', 'role_applied_for')
    readonly_fields = ('first_name', 'last_name', 'email', 'phone_number', 'application_type', 
                      'role_applied_for', 'current_location', 'resume', 'message', 'agreed_to_terms')
    
    def has_add_permission(self, request):
        return False  # Disable adding from admin

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone_number', 'message')
    
    def has_add_permission(self, request):
        return False  # Disable adding from admin

@admin.register(AftermarketForm)
class AftermarketFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company_name', 'country')
    list_filter = ('country',)
    search_fields = ('first_name', 'last_name', 'email', 'company_name', 'country', 'message')
    readonly_fields = ('first_name', 'last_name', 'email', 'phone_number', 'company_name', 
                      'country', 'message')
    
    def has_add_permission(self, request):
        return False  # Disable adding from admin
