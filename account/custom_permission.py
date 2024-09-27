from rest_framework.permissions import BasePermission

# Custom permission class to check if the user is an admin (staff) and active
class IsAdmin(BasePermission):
    # Custom error message when permission is denied
    message = 'You are not a verified user'
    
    # Method to check if the user has permission to access the view
    def has_permission(self, request, view):
        # If the request method is one of GET, POST, PUT, PATCH, DELETE, or OPTIONS
        if request.method == 'GET' or 'POST' or 'PUT' or 'PATCH' or 'DELETE' or 'OPTIONS':
            # Check if the user is an admin (staff) and is active
            return request.user.is_staff and request.user.is_active
        # Return False if the request method is anything else
        return False
