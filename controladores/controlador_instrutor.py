from flask import render_template, request, redirect, Blueprint
from classes.instrutor import Instrutor
import conectores.conector_instrutor as conector_instrutor

# Create the blueprint instance
instrutores_blueprint = Blueprint("instrutores", __name__)

# Route for instructors index page
@instrutores_blueprint.route("/instrutores")
def instrutores_index():
    instrutores = conector_instrutor.get_all()
    return render_template("instrutores/index.html", instrutores=instrutores, title="Instrutores")

# Route for new instructor page
@instrutores_blueprint.route("/instrutores/novo")
def novo_instrutor():
    return render_template("instrutores/novo.html", title="Novo Instrutor")

# Route for creating a new instructor
@instrutores_blueprint.route("/instrutores", methods=["POST"])
def cria_instrutor():
    # Implementation remains the same

# Route for editing an instructor
@instrutores_blueprint.route("/instrutores/<id>/edit")
def edita_instrutor(id):
    # Implementation remains the same

# Route for updating an instructor
@instrutores_blueprint.route("/instrutores/<id>", methods=["POST"])
def atualiza_instrutor(id):
    # Implementation remains the same

# Route for showing details of an instructor
@instrutores_blueprint.route("/instrutores/<id>")
def mostra_detalhes(id):
    # Implementation remains the same

# Route for deleting an instructor
@instrutores_blueprint.route("/instrutores/<id>/delete")
def deleta_instrutor(id):
    # Implementation remains the same