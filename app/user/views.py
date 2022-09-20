"""
Views for the user API.
"""
from rest_framework import generics

# Create your views here.
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):  # Handles Post request for ya
    """Create a new user in the system."""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken): # use customize serializer (to use email and password not username)
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # uses default rendering?
