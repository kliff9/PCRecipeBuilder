"""
Test Custom Django management Commands
"""

from unittest.mock import patch  # mock the behavoir (stimilation )

#  might be a connection error?
from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command  # allow to call command
from django.db.utils import OperationalError  # Error #2?
from django.test import SimpleTestCase  # For Testing

# .check = mock object/ value


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""
    # patched checked because of @patch
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True  # when called return True Value

        call_command('wait_for_db')
        #  check if called with databases=['default']
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        # first 2 times call mock method, the next 3 times raise Oerror
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
