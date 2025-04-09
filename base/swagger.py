from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

# Common response schemas
success_response = openapi.Response(
    description="Successful response",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    )
)

error_response = openapi.Response(
    description="Error response",
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING),
        }
    )
)

# Category endpoints documentation
category_list_schema = swagger_auto_schema(
    operation_description="List all categories",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of categories",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        )
    }
)

category_detail_schema = swagger_auto_schema(
    operation_description="Get a specific category",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Category details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

# Post endpoints documentation
post_list_schema = swagger_auto_schema(
    operation_description="List all blog posts",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of blog posts",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'title': openapi.Schema(type=openapi.TYPE_STRING),
                        'slug': openapi.Schema(type=openapi.TYPE_STRING),
                        'date_added': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                        'author': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'username': openapi.Schema(type=openapi.TYPE_STRING),
                                'email': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        ),
                        'category': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        ),
                    }
                )
            )
        )
    }
)

post_detail_schema = swagger_auto_schema(
    operation_description="Get a specific blog post by slug",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Blog post details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'meta_title': openapi.Schema(type=openapi.TYPE_STRING),
                    'meta_description': openapi.Schema(type=openapi.TYPE_STRING),
                    'title': openapi.Schema(type=openapi.TYPE_STRING),
                    'slug': openapi.Schema(type=openapi.TYPE_STRING),
                    'date_added': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                    'author': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'username': openapi.Schema(type=openapi.TYPE_STRING),
                            'email': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                    'featured_image': openapi.Schema(type=openapi.TYPE_STRING),
                    'category': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'name': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                    'intro': openapi.Schema(type=openapi.TYPE_STRING),
                    'body': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

# Form submission documentation
career_form_schema = swagger_auto_schema(
    operation_description="Submit a career application",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['first_name', 'last_name', 'email', 'phone_number', 'application_type', 'role_applied_for', 'current_location', 'resume', 'agreed_to_terms'],
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name of the applicant'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name of the applicant'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Email address'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
            'application_type': openapi.Schema(type=openapi.TYPE_STRING, description='Type of application'),
            'role_applied_for': openapi.Schema(type=openapi.TYPE_STRING, description='Role being applied for'),
            'current_location': openapi.Schema(type=openapi.TYPE_STRING, description='Current location'),
            'resume': openapi.Schema(type=openapi.TYPE_FILE, description='Resume file'),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Additional message'),
            'agreed_to_terms': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Agreement to terms and conditions')
        }
    ),
    responses={
        status.HTTP_201_CREATED: success_response,
        status.HTTP_400_BAD_REQUEST: error_response
    }
)

# Career form CRUD operations
career_form_list_schema = swagger_auto_schema(
    operation_description="List all career applications",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of career applications",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'count': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'next': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'previous': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'results': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                'email': openapi.Schema(type=openapi.TYPE_STRING),
                                'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
                                'application_type': openapi.Schema(type=openapi.TYPE_STRING),
                                'role_applied_for': openapi.Schema(type=openapi.TYPE_STRING),
                                'current_location': openapi.Schema(type=openapi.TYPE_STRING),
                                'resume': openapi.Schema(type=openapi.TYPE_STRING),
                                'message': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                                'agreed_to_terms': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            }
                        )
                    )
                }
            )
        )
    }
)

career_form_detail_schema = swagger_auto_schema(
    operation_description="Get a specific career application",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Career application details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
                    'application_type': openapi.Schema(type=openapi.TYPE_STRING),
                    'role_applied_for': openapi.Schema(type=openapi.TYPE_STRING),
                    'current_location': openapi.Schema(type=openapi.TYPE_STRING),
                    'resume': openapi.Schema(type=openapi.TYPE_STRING),
                    'message': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'agreed_to_terms': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

career_form_update_schema = swagger_auto_schema(
    operation_description="Update a career application",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name of the applicant'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name of the applicant'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Email address'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
            'application_type': openapi.Schema(type=openapi.TYPE_STRING, description='Type of application'),
            'role_applied_for': openapi.Schema(type=openapi.TYPE_STRING, description='Role being applied for'),
            'current_location': openapi.Schema(type=openapi.TYPE_STRING, description='Current location'),
            'resume': openapi.Schema(type=openapi.TYPE_FILE, description='Resume file'),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Additional message'),
            'agreed_to_terms': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Agreement to terms and conditions')
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Updated career application",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
                    'application_type': openapi.Schema(type=openapi.TYPE_STRING),
                    'role_applied_for': openapi.Schema(type=openapi.TYPE_STRING),
                    'current_location': openapi.Schema(type=openapi.TYPE_STRING),
                    'resume': openapi.Schema(type=openapi.TYPE_STRING),
                    'message': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'agreed_to_terms': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                }
            )
        ),
        status.HTTP_400_BAD_REQUEST: error_response,
        status.HTTP_404_NOT_FOUND: error_response
    }
)

career_form_delete_schema = swagger_auto_schema(
    operation_description="Delete a career application",
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(description="Career application deleted successfully"),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

contact_inquiry_schema = swagger_auto_schema(
    operation_description="Submit a contact inquiry",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'email', 'message'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the inquirer'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Email address'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number (optional)'),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Inquiry message')
        }
    ),
    responses={
        status.HTTP_201_CREATED: success_response,
        status.HTTP_400_BAD_REQUEST: error_response
    }
)

# Contact inquiry CRUD operations
contact_inquiry_list_schema = swagger_auto_schema(
    operation_description="List all contact inquiries",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of contact inquiries",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'count': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'next': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'previous': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'results': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                                'email': openapi.Schema(type=openapi.TYPE_STRING),
                                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                                'message': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    )
                }
            )
        )
    }
)

contact_inquiry_detail_schema = swagger_auto_schema(
    operation_description="Get a specific contact inquiry",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Contact inquiry details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

contact_inquiry_update_schema = swagger_auto_schema(
    operation_description="Update a contact inquiry",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the inquirer'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Email address'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number (optional)'),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Inquiry message')
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Updated contact inquiry",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_400_BAD_REQUEST: error_response,
        status.HTTP_404_NOT_FOUND: error_response
    }
)

contact_inquiry_delete_schema = swagger_auto_schema(
    operation_description="Delete a contact inquiry",
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(description="Contact inquiry deleted successfully"),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

aftermarket_form_schema = swagger_auto_schema(
    operation_description="Submit an aftermarket inquiry",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['first_name', 'last_name', 'email', 'country', 'message'],
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Email address'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number (optional)'),
            'company_name': openapi.Schema(type=openapi.TYPE_STRING, description='Company name (optional)'),
            'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Inquiry message')
        }
    ),
    responses={
        status.HTTP_201_CREATED: success_response,
        status.HTTP_400_BAD_REQUEST: error_response
    }
)

# Aftermarket form CRUD operations
aftermarket_form_list_schema = swagger_auto_schema(
    operation_description="List all aftermarket inquiries",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of aftermarket inquiries",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'count': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'next': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'previous': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'results': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                                'email': openapi.Schema(type=openapi.TYPE_STRING),
                                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                                'company_name': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                                'country': openapi.Schema(type=openapi.TYPE_STRING),
                                'message': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    )
                }
            )
        )
    }
)

aftermarket_form_detail_schema = swagger_auto_schema(
    operation_description="Get a specific aftermarket inquiry",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Aftermarket inquiry details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'company_name': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'country': openapi.Schema(type=openapi.TYPE_STRING),
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

aftermarket_form_update_schema = swagger_auto_schema(
    operation_description="Update an aftermarket inquiry",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', description='Email address'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number (optional)'),
            'company_name': openapi.Schema(type=openapi.TYPE_STRING, description='Company name (optional)'),
            'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Inquiry message')
        }
    ),
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Updated aftermarket inquiry",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'company_name': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    'country': openapi.Schema(type=openapi.TYPE_STRING),
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_400_BAD_REQUEST: error_response,
        status.HTTP_404_NOT_FOUND: error_response
    }
)

aftermarket_form_delete_schema = swagger_auto_schema(
    operation_description="Delete an aftermarket inquiry",
    responses={
        status.HTTP_204_NO_CONTENT: openapi.Response(description="Aftermarket inquiry deleted successfully"),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

# Product-related schemas
vehicle_category_list_schema = swagger_auto_schema(
    operation_description="List all vehicle categories",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of vehicle categories",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'img': openapi.Schema(type=openapi.TYPE_STRING),
                        'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        )
    }
)

vehicle_category_detail_schema = swagger_auto_schema(
    operation_description="Get a specific vehicle category",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Vehicle category details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'img': openapi.Schema(type=openapi.TYPE_STRING),
                    'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

product_type_list_schema = swagger_auto_schema(
    operation_description="List all product types",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of product types",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'img': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        )
    }
)

product_type_detail_schema = swagger_auto_schema(
    operation_description="Get a specific product type",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Product type details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'img': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

product_list_schema = swagger_auto_schema(
    operation_description="List all products",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of products",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'type': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                                'img': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        ),
                        'vehicle_categories': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'img': openapi.Schema(type=openapi.TYPE_STRING),
                                    'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        'image': openapi.Schema(type=openapi.TYPE_STRING),
                        'specifications': openapi.Schema(type=openapi.TYPE_OBJECT),
                        'features': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_STRING)
                        ),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        )
    }
)

product_detail_schema = swagger_auto_schema(
    operation_description="Get a specific product",
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="Product details",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'type': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'name': openapi.Schema(type=openapi.TYPE_STRING),
                            'img': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                    'vehicle_categories': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                                'img': openapi.Schema(type=openapi.TYPE_STRING),
                                'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    ),
                    'image': openapi.Schema(type=openapi.TYPE_STRING),
                    'specifications': openapi.Schema(type=openapi.TYPE_OBJECT),
                    'features': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING)
                    ),
                    'description': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: error_response
    }
)

product_create_schema = swagger_auto_schema(
    operation_description="Create a new product",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['id', 'name', 'type', 'vehicle_categories', 'image', 'specifications', 'features', 'description'],
        properties={
            'id': openapi.Schema(type=openapi.TYPE_STRING, description='Product ID'),
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Product name'),
            'type': openapi.Schema(type=openapi.TYPE_INTEGER, description='Product type ID'),
            'vehicle_categories': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_INTEGER),
                description='List of vehicle category IDs'
            ),
            'image': openapi.Schema(type=openapi.TYPE_FILE, description='Product image'),
            'specifications': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                description='Product specifications',
                properties={
                    'voltage': openapi.Schema(type=openapi.TYPE_STRING),
                    'current': openapi.Schema(type=openapi.TYPE_STRING),
                    'power': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
            'features': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(type=openapi.TYPE_STRING),
                description='Product features'
            ),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Product description')
        }
    ),
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description="Product created successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'type': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'name': openapi.Schema(type=openapi.TYPE_STRING),
                            'img': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                    'vehicle_categories': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                                'img': openapi.Schema(type=openapi.TYPE_STRING),
                                'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    ),
                    'image': openapi.Schema(type=openapi.TYPE_STRING),
                    'specifications': openapi.Schema(type=openapi.TYPE_OBJECT),
                    'features': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING)
                    ),
                    'description': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        status.HTTP_400_BAD_REQUEST: error_response
    }
)

product_by_type_schema = swagger_auto_schema(
    operation_description="Get products by type",
    manual_parameters=[
        openapi.Parameter(
            'type_id',
            openapi.IN_QUERY,
            description="Product type ID",
            type=openapi.TYPE_INTEGER,
            required=True
        )
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of products by type",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'type': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                                'img': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        ),
                        'vehicle_categories': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'img': openapi.Schema(type=openapi.TYPE_STRING),
                                    'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        'image': openapi.Schema(type=openapi.TYPE_STRING),
                        'specifications': openapi.Schema(type=openapi.TYPE_OBJECT),
                        'features': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_STRING)
                        ),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Type ID is required",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Product type not found",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        )
    }
)

product_by_category_schema = swagger_auto_schema(
    operation_description="Get products by vehicle category",
    manual_parameters=[
        openapi.Parameter(
            'category_id',
            openapi.IN_QUERY,
            description="Vehicle category ID",
            type=openapi.TYPE_INTEGER,
            required=True
        )
    ],
    responses={
        status.HTTP_200_OK: openapi.Response(
            description="List of products by category",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'type': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'name': openapi.Schema(type=openapi.TYPE_STRING),
                                'img': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        ),
                        'vehicle_categories': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                                    'img': openapi.Schema(type=openapi.TYPE_STRING),
                                    'short_name': openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        'image': openapi.Schema(type=openapi.TYPE_STRING),
                        'specifications': openapi.Schema(type=openapi.TYPE_OBJECT),
                        'features': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(type=openapi.TYPE_STRING)
                        ),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="Category ID is required",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="Vehicle category not found",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        )
    }
) 