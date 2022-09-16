from django.test import SimpleTestCase

from app import calctest

class Calculator_Test(SimpleTestCase):

    def test_add(self):
        res = calctest.add(5, 4)

        self.assertEqual(res, 9 )
    def test_sub(self):
        res = calctest.sub(5, 4)

        self.assertEqual(res, 1)
