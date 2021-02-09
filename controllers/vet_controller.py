from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    
    return render_template("vets/index.html", vets = vets)

# how do i list the pets registered to each vet?

@vets_blueprint.route("/vets", methods=["POST"])
def new_vet():
    new_vet = Vet(request.form['name'])
    vet_repository.save(new_vet)
    return redirect("/vets")


# @visits_blueprint.route("/visits",  methods=['POST'])
# def create_task():
#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)
#     return redirect('/visits')
