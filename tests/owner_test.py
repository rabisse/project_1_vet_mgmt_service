import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Darth Vader", "456-123", "dark-side@veryhotmail.com")
    
    def test_owner_name(self):
        self.assertEqual("Darth Vader", self.owner.name)

    def test_owner_phone(self):
        self.assertEqual("456-123", self.owner.phone)

    def test_owner_email(self):
        self.assertEqual("dark-side@veryhotmail.com", self.owner.email)

    def test_owner_bill(self):
        self.assertEqual(0, self.owner.bill)
