from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.treatment import Treatment
from models.owner import Owner
from models.vet import Vet
import repositories.treatment_repository as treatment_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route("/treatments/new/<pet_id>")
def new_treatment(pet_id):
    pet = pet_repository.select(pet_id)
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("treatments/new.html", pet=pet, pets=pets, vets=vets)

@treatments_blueprint.route("/treatments/new", methods=["POST"])
def create_treatment():
    name = request.form['name']
    cost = request.form['cost']
    note = request.form['note']   
    pet_id = request.form['pet_id'] 
    pet = pet_repository.select(pet_id)
    vet_id = request.form['vet_id']
    vet = vet_repository.select(vet_id)
    treatment = Treatment(name, cost, note, pet, vet)
    treatment_repository.save(treatment)
    
    vet.add_to_earnings(int(treatment.cost))
    vet_repository.update(vet)

    owner = owner_repository.select(pet.owner.id)
    owner.add_to_bill(int(treatment.cost))
    owner_repository.update(owner)
    return redirect("/pets")

