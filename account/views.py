from account.custom_viewset import PublicViewSet
from account.serializers import AccountSerializer, LoginSerializer
from account.services.account import AccountService

from rest_framework import status
from utils.response import error_response, success_response

# Create your views here.
class AccountViewSet(PublicViewSet):
    
    def create_account(self, request):
        """Register user view"""
        # Deserialize the incoming data
        serializer = AccountSerializer(data=request.data)
        # Check if the data is valid
        if not serializer.is_valid():
            # Return an error response if the data is invalid
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new user using the validated data
        user, message = AccountService.create_user(**serializer.validated_data)
        
        # If user creation failed, return an error response
        if not user:
            return error_response(msg=message, data={}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return a success response if the user was created successfully
        return success_response(status=status.HTTP_201_CREATED, msg=message, data={})

    def login(self, request):
        """Login user view"""
        # Deserialize the incoming data
        serializer = LoginSerializer(data=request.data)
        # Check if the data is valid
        if not serializer.is_valid():
            # Return an error response if the data is invalid
            return error_response(data=serializer.errors, msg="", status=status.HTTP_400_BAD_REQUEST)
        
        # Verify the user credentials
        response = AccountService.verify_user(**serializer.validated_data)
        
        # If verification failed, return an error response
        if not response:
            return error_response(msg="Invalid credentials", data={}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return a success response if the user was verified successfully
        return success_response(status=status.HTTP_200_OK, msg="User logged in successfully", data=response)
