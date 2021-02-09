from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

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

