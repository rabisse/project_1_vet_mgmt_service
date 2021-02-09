from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    all_pets = []
    for owner in owners:
        found_pet = owner_repository.pets(owner.id)
        all_pets.append(found_pet)
    return render_template("owners/index.html", owners = owners, all_pets=all_pets)


@owners_blueprint.route("/owners", methods=["POST"])
def new_owner():
    new_owner = Owner(request.form['name'], request.form['phone'], request.form['email'])
    owner_repository.save(new_owner)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect("/owners")
