"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers  # checks inpput and converts to python object(data) / model


class UserSerializer(serializers.ModelSerializer):  # automatically save things to a spefic Model
    """Serializer for the user object."""

    class Meta:  # tell django which model and fields to pass to the serializer that is being represented
        model = get_user_model()
        fields = ['email', 'password', 'name', 'bio']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}  # extra data or specifications

    def create(self, validated_data):  # create method
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
