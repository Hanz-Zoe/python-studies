from flask import render_template, request, redirect, Blueprint
from classes.agendamento import Agendamento
import conectores.conector_agendamento as conector_agendamento
import conectores.conector_membro as conector_membro
import conectores.conector_atividade as conector_atividade
import conectores.conector_plano as conector_plano

# Create the blueprint instance
agendamentos_blueprint = Blueprint("agendamentos", __name__)

# Route for the index page
@agendamentos_blueprint.route("/agendamentos")
def agendamentos_index():
    agendamentos = conector_agendamento.get_all()
    return render_template("agendamentos/index.html", agendamentos=agendamentos, title="agendamentos")

# Route for a new member
@agendamentos_blueprint.route("/agendamentos/novo/membro/<id>")
def novo_membro_agendamento(id):
    membro = conector_membro.get_one(id)
    atividades = conector_atividade.get_all_active()
    return render_template("agendamentos/novo-membro.html", membro=membro, atividades=atividades, title="Novo Agendamento")

# Route for a new activity
@agendamentos_blueprint.route("/agendamentos/novo/atividade/<id>")
def nova_atividade_agendamento(id):
    atividade = conector_atividade.get_one(id)
    membros = conector_membro.get_all_active()
    return render_template("agendamentos/nova-atividade.html", atividade=atividade, membros=membros, title="Novo Agendamento")

# Route to create an appointment from an activity
@agendamentos_blueprint.route("/agendamentos/atividade", methods=["POST"])
def cria_agendamento_from_atividade():
    # Implementation remains the same

# Route to create an appointment from a member
@agendamentos_blueprint.route("/agendamentos/membro", methods=["POST"])
def cria_agendamento_from_membro():
    # Implementation remains the same

# Route for deletion
@agendamentos_blueprint.route("/agendamentos/<id>/delete")
def deleta_agendamento(id):
    conector_agendamento.delete_one(id)
    return redirect("/agendamentos")

# Route to delete member appointment
@agendamentos_blueprint.route("/agendamentos/delete/membro/<membro_id>/<atividade_id>")
def deleta_agendamento_membro(membro_id, atividade_id):
    # Implementation remains the same

# Route to delete activity appointment
@agendamentos_blueprint.route("/agendamentos/delete/atividade/<membro_id>/<atividade_id>")
def deleta_agendamento_atividade(membro_id, atividade_id):
    # Implementation remains the same