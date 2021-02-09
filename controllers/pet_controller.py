from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)


@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    treatments = pet_repository.treatments(pet)
    return render_template("pets/show.html", pet=pet, treatments=treatments)

@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect("/pets")

@pets_blueprint.route("/pets/new")
def new_pet():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("pets/new.html", owners=owners, vets=vets)

@pets_blueprint.route("/pets", methods=["POST"])
def create_pet():
    name = request.form['name']
    species = request.form['species']
    dob = request.form['dob']
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    pet = Pet(name, species, dob, owner, vet)
    pet_repository.save(pet)
    return redirect('/pets')
    
