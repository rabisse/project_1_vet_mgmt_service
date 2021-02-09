from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    all_pets = []
    for vet in vets:
        found_pet = vet_repository.pets(vet.id)
        all_pets.append(found_pet)
    return render_template("vets/index.html", vets = vets, all_pets=all_pets)


@vets_blueprint.route("/vets", methods=["POST"])
def new_vet():
    new_vet = Vet(request.form['name'])
    vet_repository.save(new_vet)
    return redirect("/vets")

@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/vets")
