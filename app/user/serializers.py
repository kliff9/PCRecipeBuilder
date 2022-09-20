"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)


from django.utils.translation import gettext as _

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

    def update(self, instance, validated_data):
        """Update and return user."""
        # instance = current model(object)
        password = validated_data.pop('password', None)  # remove password, NONE is default only password would "pop" ?
        user = super().update(instance, validated_data)  # add chage what we need to change

        if password:  # check password
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},  # text can be hidden
        trim_whitespace=False,  # prevent trim whitespace(take off)
    )

    def validate(self, attributes):  # make sure data is corrent
        """Validate and authenticate the user."""
        email = attributes.get('email')
        password = attributes.get('password')
        user = authenticate(  # check username and password
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attributes['user'] = user
        return attributes
