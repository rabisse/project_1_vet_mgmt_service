from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet

def save(vet):
    sql = "INSERT INTO vets (name), VALUES (%s) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['earnings'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        vet = Vet(result['name'], result['earnings'], result['id'])
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def update(vet):
    sql = "UPDATE vets SET (name, earnings) = (%s, %s) WHERE id = %s"
    values = [vet.name, vet.earnings, vet.id]
    run_sql(sql, values)

def pets(vet):
    pets = []
    sql = "SELECT * FROM pets WHERE vet_id = %s"
    value = [vet.id]
    results = run_sql(sql, value)
    for row in results:
        pet = Pet(row['name'], row['species'], row['breed'], row['dob'], row['owner_id'], row['vet_id'], row['id'])
        # is this the right way to put the owner into this? Can I still print out the owner name this way? same for the owners repo pet list
        pets.append(pet)
    return pets

