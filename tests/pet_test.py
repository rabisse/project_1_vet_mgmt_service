import unittest
from models.pet import Pet

class TestPet(unittest.TestCase):
    def setUp(self):
        self.pet = Pet("Jerry", "Jaguar", "01 Jan 2021", "Darth Vader", "Dr. Dolittle")
    
    def test_pet_name(self):
        self.assertEqual("Jerry", self.pet.name)

    def test_pet_species(self):
        self.assertEqual("Jaguar", self.pet.species)

    def test_pet_dob(self):
        self.assertEqual("01 Jan 2021", self.pet.dob)

    def test_pet_owner(self):
        self.assertEqual("Darth Vader", self.pet.owner)

    def test_pet_vet(self):
        self.assertEqual("Dr. Dolittle", self.pet.vet)

