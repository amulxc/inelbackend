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
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'application_type': openapi.Schema(type=openapi.TYPE_STRING),
            'role_applied_for': openapi.Schema(type=openapi.TYPE_STRING),
            'current_location': openapi.Schema(type=openapi.TYPE_STRING),
            'resume': openapi.Schema(type=openapi.TYPE_FILE),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
            'agreed_to_terms': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        }
    ),
    responses={
        status.HTTP_201_CREATED: success_response,
        status.HTTP_400_BAD_REQUEST: error_response
    }
)

contact_inquiry_schema = swagger_auto_schema(
    operation_description="Submit a contact inquiry",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'email', 'message'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        status.HTTP_201_CREATED: success_response,
        status.HTTP_400_BAD_REQUEST: error_response
    }
)

aftermarket_form_schema = swagger_auto_schema(
    operation_description="Submit an aftermarket inquiry",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['first_name', 'last_name', 'email', 'country', 'message'],
        properties={
            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'company_name': openapi.Schema(type=openapi.TYPE_STRING),
            'country': openapi.Schema(type=openapi.TYPE_STRING),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={
        status.HTTP_201_CREATED: success_response,
        status.HTTP_400_BAD_REQUEST: error_response
    }
) 