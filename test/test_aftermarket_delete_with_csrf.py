import requests
import json
import sys
import re

def get_csrf_token(base_url):
    """
    Get the CSRF token from the server.
    
    Args:
        base_url (str): The base URL of the API.
        
    Returns:
        str: The CSRF token, or None if it couldn't be retrieved.
    """
    try:
        # First, get the CSRF token by making a GET request
        response = requests.get(f"{base_url}/api/docs/")
        
        # Extract the CSRF token from the response
        csrf_token_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
        if csrf_token_match:
            csrf_token = csrf_token_match.group(1)
            print(f"CSRF token retrieved: {csrf_token}")
            return csrf_token
        else:
            print("Could not find CSRF token in the response.")
            return None
    except Exception as e:
        print(f"Error getting CSRF token: {str(e)}")
        return None

def create_test_aftermarket_form(base_url, csrf_token=None):
    """
    Create a test aftermarket form to be used for deletion testing.
    
    Args:
        base_url (str): The base URL of the API.
        csrf_token (str, optional): The CSRF token to use in the request.
        
    Returns:
        int: The ID of the created aftermarket form, or None if creation failed.
    """
    # Endpoint for aftermarket create
    endpoint = "/api/aftermarket"
    
    # Headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    # Add CSRF token if provided
    if csrf_token:
        headers['X-CSRFToken'] = csrf_token
    
    # Test data with all required fields
    data = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "phone": "1234567890",
        "company": "Test Company",
        "country": "United States",
        "message": "This is a test message for deletion testing",
        "product_interest": "Test Product"
    }
    
    try:
        # Create the aftermarket form
        response = requests.post(f"{base_url}{endpoint}", headers=headers, json=data)
        
        # Check if the creation was successful
        if response.status_code in [200, 201]:
            print(f"Success: Test aftermarket form created successfully.")
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text}")
            
            # Since the server doesn't return the ID in the response,
            # we need to fetch the list of aftermarket forms and get the latest one
            print("Fetching list of aftermarket forms to find the ID of the newly created form...")
            list_response = requests.get(f"{base_url}/api/aftermarket", headers=headers)
            print(f"List response status code: {list_response.status_code}")
            print(f"List response content: {list_response.text[:200]}...")  # Print first 200 chars
            
            if list_response.status_code == 200:
                try:
                    # Parse the response as JSON
                    response_data = list_response.json()
                    
                    # Check if the response has a paginated format with "results" field
                    if isinstance(response_data, dict) and "results" in response_data:
                        forms = response_data["results"]
                        print(f"Number of forms found: {len(forms)}")
                        
                        if forms and len(forms) > 0:
                            # Get the ID of the most recently created form
                            latest_form = forms[0]  # Assuming the list is ordered with newest first
                            print(f"Latest form data: {latest_form}")
                            form_id = latest_form.get('id')
                            if form_id:
                                print(f"Found newly created form with ID: {form_id}")
                                return form_id
                        else:
                            print("No forms found in the results array.")
                    else:
                        print("Response does not have the expected paginated format with 'results' field.")
                        print(f"Response structure: {list(response_data.keys()) if isinstance(response_data, dict) else 'Not a dictionary'}")
                except Exception as e:
                    print(f"Error parsing aftermarket forms list: {str(e)}")
                    print(f"Raw response content: {list_response.text}")
            else:
                print(f"Failed to fetch aftermarket forms list. Status code: {list_response.status_code}")
            
            # If we couldn't get the ID from the list, try a different approach
            print("Trying alternative approach to find the form ID...")
            
            # Try to get the form by email (which should be unique)
            email = data["email"]
            print(f"Searching for form with email: {email}")
            
            # Try to filter by email using the correct query parameter format
            search_response = requests.get(f"{base_url}/api/aftermarket/?email={email}", headers=headers)
            print(f"Search response status code: {search_response.status_code}")
            print(f"Search response content: {search_response.text[:200]}...")
            
            if search_response.status_code == 200:
                try:
                    search_data = search_response.json()
                    if isinstance(search_data, dict) and "results" in search_data:
                        search_results = search_data["results"]
                        if search_results and len(search_results) > 0:
                            form_id = search_results[0].get('id')
                            if form_id:
                                print(f"Found form with ID: {form_id} using email search")
                                return form_id
                except Exception as e:
                    print(f"Error parsing search results: {str(e)}")
            
            print("Error: Could not find the ID of the created form.")
            return None
        else:
            print(f"Error: Failed to create test aftermarket form.")
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"Error creating aftermarket form: {str(e)}")
        return None

def test_aftermarket_delete_with_csrf(id=1, csrf_token=None):
    """
    Test the DELETE functionality for the aftermarket endpoint with CSRF token.
    
    Args:
        id (int): The ID of the aftermarket form to delete.
        csrf_token (str): The CSRF token to use in the request.
        
    Returns:
        bool: True if the test passed, False otherwise.
    """
    # Base URL for the API
    base_url = "https://inelbackend-fccmbmfjbhewhbhh.centralindia-01.azurewebsites.net"
    
    # Endpoint for aftermarket delete - no trailing slash
    endpoint = f"/api/aftermarket/{id}"
    
    # Headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    # Add CSRF token if provided
    if csrf_token:
        headers['X-CSRFToken'] = csrf_token
    
    # First, try to get the aftermarket form to verify it exists
    try:
        get_response = requests.get(f"{base_url}{endpoint}", headers=headers)
        if get_response.status_code != 200:
            print(f"Error: Aftermarket form with ID {id} not found.")
            print(f"Status code: {get_response.status_code}")
            print(f"Response: {get_response.text}")
            return False
    except Exception as e:
        print(f"Error getting aftermarket form: {str(e)}")
        return False
    
    # Now try to delete the aftermarket form
    try:
        delete_response = requests.delete(f"{base_url}{endpoint}", headers=headers)
        
        # Check if the delete was successful
        if delete_response.status_code in [200, 204]:
            print(f"Success: Aftermarket form with ID {id} deleted successfully.")
            print(f"Status code: {delete_response.status_code}")
            return True
        else:
            print(f"Error: Failed to delete aftermarket form with ID {id}.")
            print(f"Status code: {delete_response.status_code}")
            print(f"Response: {delete_response.text}")
            return False
    except Exception as e:
        print(f"Error deleting aftermarket form: {str(e)}")
        return False

def test_aftermarket_delete_with_csrf_and_trailing_slash(id=1, csrf_token=None):
    """
    Test the DELETE functionality for the aftermarket endpoint with CSRF token and trailing slash.
    
    Args:
        id (int): The ID of the aftermarket form to delete.
        csrf_token (str): The CSRF token to use in the request.
        
    Returns:
        bool: True if the test passed, False otherwise.
    """
    # Base URL for the API
    base_url = "https://inelbackend-fccmbmfjbhewhbhh.centralindia-01.azurewebsites.net"
    
    # Endpoint for aftermarket delete with trailing slash
    endpoint = f"/api/aftermarket/{id}/"
    
    # Headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    # Add CSRF token if provided
    if csrf_token:
        headers['X-CSRFToken'] = csrf_token
    
    # Try to delete the aftermarket form with trailing slash
    try:
        delete_response = requests.delete(f"{base_url}{endpoint}", headers=headers)
        
        # Check if the delete was successful
        if delete_response.status_code in [200, 204]:
            print(f"Success: Aftermarket form with ID {id} deleted successfully (with trailing slash).")
            print(f"Status code: {delete_response.status_code}")
            return True
        else:
            print(f"Error: Failed to delete aftermarket form with ID {id} (with trailing slash).")
            print(f"Status code: {delete_response.status_code}")
            print(f"Response: {delete_response.text}")
            return False
    except Exception as e:
        print(f"Error deleting aftermarket form: {str(e)}")
        return False

if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://inelbackend-fccmbmfjbhewhbhh.centralindia-01.azurewebsites.net"
    
    # Get the ID from command line arguments if provided
    id = None
    if len(sys.argv) > 1:
        try:
            id = int(sys.argv[1])
        except ValueError:
            print(f"Error: Invalid ID '{sys.argv[1]}'. Creating a new test form.")
    
    # Get the CSRF token
    csrf_token = get_csrf_token(base_url)
    
    # If we couldn't get the CSRF token, ask the user to provide it
    if not csrf_token:
        csrf_token = input("Please enter the CSRF token manually: ")
    
    # If no ID was provided or it was invalid, create a test form
    if id is None:
        print("Creating a test aftermarket form for deletion testing...")
        id = create_test_aftermarket_form(base_url, csrf_token)
        if id is None:
            print("Failed to create a test form. Exiting.")
            sys.exit(1)
        print(f"Created test form with ID: {id}")
    
    print("\nTesting DELETE without trailing slash:")
    test_aftermarket_delete_with_csrf(id, csrf_token)
    
    print("\nTesting DELETE with trailing slash:")
    test_aftermarket_delete_with_csrf_and_trailing_slash(id, csrf_token) 