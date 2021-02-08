from db.run_sql import run_sql

from models.treatment import Treatment

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

def save(treatment):
    sql = "INSERT INTO treatments (name, cost, note, pet_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [treatment.name, treatment.cost, treatment.note, treatment.pet.id, treatment.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatment.id = id
    return treatment

def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    results = run_sql(sql)
    for row in results:
        pet = pet_repository.select(row['pet_id'])
        vet = vet_repository.select(row['vet_id'])
        treatment = Treatment(row['name'], row['cost'], row['note'], pet, vet, row['id'])
        treatments.append(treatment)
    return treatments

def select(id):
    treatment = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        pet = pet_repository.select(result['pet_id'])
        vet = vet_repository.select(result['vet_id'])
        treatment = Treatment(result['name'], result['cost'], result['note'], pet, vet, result['id'])
    return treatment

def delete_all():
    sql = "DELETE  FROM treatments"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(treatment):
    sql = "UPDATE treatments SET (name, cost, note, pet_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [treatment.name, treatment.cost, treatment.note, treatment.pet.id, treatment.vet.id, treatment.id]
    run_sql(sql, values)

