"""
Tests for models.
"""
from genericpath import samefile
from random import sample
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        print('User Model is Crrently Being Tested')
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.is_active, True)
        print('User Model Test has been completed')

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        single_emails = ['TEST334@EXAMPLE.com', 'TEST334@example.com']
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
            ['tesT5@exaMple.COM', 'tesT5@example.com'],
            ['teST6@EXample.COM', 'teST6@example.com'],

        ]
        print('User Model normalized is Crrently Being Tested')

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
        user = get_user_model().objects.create_user(single_emails[0], 'sample123')

        print(f'User Model normalized Test has been completed RESULT: {user.email}' )

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')
    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )
        print(f'User Model superuser Test has Started')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        print(f'User Model superuser Test has been completed, RESULT: {user.is_superuser}')
