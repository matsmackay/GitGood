import unittest
from Git_Good.Git_Good.Classes import User, Order


class TestUser(unittest.TestCase):
    def test_user_not_defined(self):
        self.assertRaises(ValueError, User, 'test', "")