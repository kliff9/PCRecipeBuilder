"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions

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


class CreateTokenView(ObtainAuthToken):  # use customize serializer (to use email and password not username)
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # uses default rendering?


class ManageUserView(generics.RetrieveUpdateAPIView):  # retrieve and update (patch)
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]  # if verifed
    permission_classes = [permissions.IsAuthenticated]  # if allowed, must be authenticates

    def get_object(self):  # override
        """Retrieve and return the authenticated user."""
        return self.request.user  # Http request will call this? return user
