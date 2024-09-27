from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from account.custom_permission import IsAdmin  # Custom permission to restrict access to admin users
from account.custom_authentication_classes import AdminAuthentication  # Custom authentication for admin users

# PublicViewSet: Open to both authenticated and unauthenticated users, with rate limiting
class PublicViewSet(viewsets.ViewSet):
    # Rate limiting for both authenticated and unauthenticated users
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # No permissions required; open to everyone
    permission_classes = []

# UserViewSet: Restricted to authenticated users using JWT for authentication
class UserViewSet(viewsets.ViewSet):
    # Rate limiting for authenticated and unauthenticated users
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # Only authenticated users can access this viewset
    permission_classes = [IsAuthenticated]
    # JWT-based authentication for users
    authentication_classes = [JWTAuthentication]

# AdminViewSet: Restricted to authenticated users with admin privileges
class AdminViewSet(viewsets.ViewSet):
    # Rate limiting for both authenticated and unauthenticated users
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # Only authenticated users with admin permissions can access this viewset
    permission_classes = [IsAuthenticated, IsAdmin]
    # Custom authentication for admin users
    authentication_classes = [AdminAuthentication]
