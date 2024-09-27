from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from utils.encrypt import encrypt_message
from account.models import AdminSecret

class AdminAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Retrieve the API key from the request headers
        api_key = request.headers.get('X-IRCTC-API-KEY-SECRET')
        if not api_key:
            # Raise an authentication error if no API key is provided
            raise AuthenticationFailed('No API key provided')
        
        try:
            # Attempt to retrieve the user associated with the provided API key
            user = AdminSecret.objects.get(api_key=api_key).user
        except:
            # Raise an authentication error if the API key is invalid
            raise AuthenticationFailed('Authentication failed')

        # Return the authenticated user and None for the authentication context
        return (user, None)
