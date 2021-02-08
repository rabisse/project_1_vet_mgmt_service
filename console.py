import pdb

from models.vet import Vet
from models.owner import Owner
from models.pet import Pet
from models.treatment import Treatment

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
import repositories.treatment_repository as treatment_repository

treatment_repository.delete_all()
pet_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet('Crocodile Dundee')
vet_repository.save(vet1)

vet2 = Vet('Dr. Dolittle')
vet_repository.save(vet2)

owner1 = Owner('Harrison Booth', '555-5555', 'harrisons-real-email@notreally.com')
owner_repository.save(owner1)

owner2 = Owner('Darth Vader', '456-123', 'dark-side@veryhotmail.com')
owner_repository.save(owner2)

pet1 = Pet('Jerry', 'Jaguar', '01 Jan 2021', owner1, vet1)
pet_repository.save(pet1)

pet2 = Pet('R2-D2', 'Droid', '25 May 1977', owner2, vet2)
pet_repository.save(pet2)

treatment1 = Treatment('Trim nails/claws', 50, 'Only got a few scratches', pet1, vet1)
treatment_repository.save(treatment1)

treatment2 = Treatment('Oil change', 20,'Definitely the droid I was looking for', pet2, vet2)
treatment_repository.save(treatment2)



pdb.set_trace()
