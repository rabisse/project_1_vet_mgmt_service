import unittest
from models.treatment import Treatment

class TestTreatment(unittest.TestCase):
    def setUp(self):
        self.treatment = Treatment("Trim nails/claws", 50, "Only got a few scratches", "Jerry", "Dr. Dolittle")
    
    def test_treatment_name(self):
        self.assertEqual("Trim nails/claws", self.treatment.name)

    def test_treatment_cost(self):
        self.assertEqual(50, self.treatment.cost)

    def test_treatment_note(self):
        self.assertEqual("Only got a few scratches", self.treatment.note)

    def test_treatment_pet(self):
        self.assertEqual("Jerry", self.treatment.pet)

    def test_treatment_vet(self):
        self.assertEqual("Dr. Dolittle", self.treatment.vet)

