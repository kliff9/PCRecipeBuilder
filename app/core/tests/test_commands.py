"""
Test Custom Django management Commands
"""

from unittest.mock import patch # mock the behavoir (stimilation )

from psycopg2 import OperationalError as Psycopg2OpError  # might be a connection error?

from django.core.management import call_command # allow to call command
from django.db.utils import OperationalError # Error #2?
from django.test import SimpleTestCase # For Testing
from app import calctest

class Calculator_Test(SimpleTestCase):

    def test_add(self):
        res = calctest.add(5, 4)

        self.assertEqual(res, 9 )
    def test_sub(self):
        res = calctest.sub(5, 4)

        self.assertEqual(res, 1)

@patch('core.management.commands.wait_for_db.Command.check') # .check = mock object/ value
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check): # patched checked because of @patch
        """Test waiting for database if database ready."""
        patched_check.return_value = True #when called return True Value

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default']) #check if called with databases=['default']

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
