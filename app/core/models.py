"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""
    #
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        # extra_fileds is extra fields
        user = self.model(email=self.normalize_email(email), **extra_fields)  # same as New User()
        user.set_password(password)  # set encrpyed password
        user.save(using=self._db)  # incase you have manny databases, Best practice

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# abstract base User -> functionality of auth system, and permissions for perrmissions and fields
# hook in the New Manager to our Model


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=275)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # define the user manager class for User
    objects = UserManager()
    # field for auth and replace with username
    USERNAME_FIELD = 'email'
