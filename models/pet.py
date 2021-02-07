class Pet:
    def __init__(self, name, species, breed, dob, owner, vet, id = None):
        self.name = name
        self.species = species
        self.breed = breed
        self.dob = dob
        self.owner = owner
        self.vet = vet
        self.id = id
        self.treatments = []
