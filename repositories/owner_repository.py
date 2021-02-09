from db.run_sql import run_sql
from models.owner import Owner
from models.pet import Pet

def save(owner):
    sql = "INSERT INTO owners (name, phone, email, bill) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [owner.name, owner.phone, owner.email, owner.bill]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['phone'], row['email'], row['bill'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        owner = Owner(result['name'], result['phone'], result['email'], result['bill'], result['id'])
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def update(owner):
    sql = "UPDATE owners SET (name, phone, email, bill) = (%s, %s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.phone, owner.email, owner.bill, owner.id]
    run_sql(sql, values)

def pets(id):
    pets = []
    sql = "SELECT * FROM pets WHERE owner_id = %s"
    value = [id]
    results = run_sql(sql, value)
    for row in results:
        pet = Pet(row['name'], row['species'], row['dob'], row['owner_id'], row['vet_id'], row['id'])
        pets.append(pet)
    return pets

