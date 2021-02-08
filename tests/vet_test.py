import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):
    
    def setUp(self):
        self.vet = Vet("Dr. Dolittle")
    
    def test_vet_name(self):
        self.assertEqual("Dr. Dolittle", self.vet.name)

    def test_vet_earnings(self):
        self.assertEqual(0, self.vet.earnings)
