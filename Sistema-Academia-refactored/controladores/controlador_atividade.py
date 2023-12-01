from flask import render_template, request, redirect, Blueprint
from classes.atividade import Atividade
import conectores.conector_atividade as conector_atividade
import conectores.conector_instrutor as conector_instrutor
import conectores.conector_plano as conector_plano

# Create the blueprint instance
atividades_blueprint = Blueprint("atividades", __name__)

# Route for active activities index
@atividades_blueprint.route("/atividades")
def atividades_index():
    atividades = conector_atividade.get_all_active()
    return render_template("atividades/index.html", atividades=atividades, title="atividades")

# Route for inactive activities index
@atividades_blueprint.route("/atividades/inativo")
def inactive_atividades():
    atividades = conector_atividade.get_all_inactive()
    return render_template("atividades/index.html", atividades=atividades, title="atividades")

# Route for new activity
@atividades_blueprint.route("/atividades/novo")
def nova_atividade():
    instrutores = conector_instrutor.get_all()
    tipos_planos = conector_plano.get_all()
    return render_template("atividades/novo.html", instrutores=instrutores, tipos_planos=tipos_planos, title="Nova Atividade")

# Route for activity creation
@atividades_blueprint.route("/atividades", methods=["POST"])
def cadastra_atividade():
    # Implementation remains the same

# Route for activity editing
@atividades_blueprint.route("/atividades/<id>/edit")
def edita_atividade(id):
    # Implementation remains the same

# Route for updating activity
@atividades_blueprint.route("/atividades/<id>", methods=["POST"])
def atualiza_atividade(id):
    # Implementation remains the same

# Route for showing activity details
@atividades_blueprint.route("/atividades/<id>")
def mostra_detalhes(id):
    # Implementation remains the same

# Route for deleting activity
@atividades_blueprint.route("/atividades/<id>/delete")
def delet_actividade(id):
    # Implementation remains the same