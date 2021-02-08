from db.run_sql import run_sql

from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets (name, species, breed, dob, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.species, pet.breed, pet.dob, pet.owner.id, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['user_id'])
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['species'], row['breed'], row['dob'], owner, vet, row['id'])
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        owner = owner_repository.select(result['user_id'])
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['name'], result['species'], result['breed'], result['dob'], owner, vet, result['id'])
    return pet

def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, species, breed, dob, owner_id, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.species, pet.breed, pet.dob, pet.owner.id, pet.vet.id, pet.id]
    run_sql(sql, values)

def treatments(pet):
    treatments = []
    sql = "SELECT * FROM treatments WHERE pet_id = %s"
    value = [pet.id]
    results = run_sql(sql, value)
    for row in results:
        treatment = Treatment(row['name'], row['cost'], row['note'], row['pet_id'], row['vet_id'], row['id'])
        treatments.append(treatment)
    return treatments

