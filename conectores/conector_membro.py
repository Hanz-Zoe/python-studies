import conectores.conector_plano as plano
from database.run_sql import run_sql
from classes.membro import Membro
from classes.atividade import Atividade

def get_all_membros():
    membros = []
    sql = "SELECT * FROM webuser.TB_MEMBROS ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["tipo_plano"])
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])
        membros.append(membro)

    return membros

def get_membro_by_id(membro_id):
    sql = "SELECT * FROM webuser.TB_MEMBROS WHERE id = %s"
    value = [membro_id]
    result = run_sql(sql, value)[0] if run_sql(sql, value) else None

    return Membro(result["nome"],
                  result["sobrenome"],
                  result["data_nascimento"],
                  result["endereco"],
                  result["telefone"],
                  result["email"],
                  plano.get_one(result["tipo_plano"]),
                  result["data_inicio"],
                  result["ativo"],
                  result["id"]) if result else None

def get_activities_by_membro_id(membro_id):
    atividades = []
    sql = "SELECT webuser.TB_ATIVIDADES.* FROM webuser.TB_ATIVIDADES INNER JOIN webuser.TB_AGENDAMENTOS ON webuser.TB_ATIVIDADES.id = webuser.TB_AGENDAMENTOS.atividade WHERE webuser.TB_AGENDAMENTOS.membro = %s"
    value = [membro_id]
    results = run_sql(sql, value)

    for row in results:
        tipo_plano = plano.get_one(row["tipo_plano"])
        atividade = Atividade(row["nome"],
                              row["instrutor"],
                              row["data"],
                              row["duracao"],
                              row["capacidade"],
                              tipo_plano,
                              row["ativo"],
                              row["id"])
        atividades.append(atividade)

    return atividades

def get_all_active_membros():
    membros = []
    sql = "SELECT * FROM webuser.TB_MEMBROS WHERE ativo = true ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["tipo_plano"])
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])
        membros.append(membro)

    return membros

def get_all_inactive_membros():
    membros = []
    sql = "SELECT * FROM webuser.TB_MEMBROS WHERE ativo = false ORDER BY nome ASC"
    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["tipo_plano"])
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        tipo_plano,
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])
        membros.append(membro)

    return membros

def insert_membro(membro):
    sql = "INSERT INTO webuser.TB_MEMBROS (nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;"
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.tipo_plano.id, membro.data_inicio, membro.ativo]
    result = run_sql(sql, values)
    membro.id = result[0]["id"] if result else None

    return membro

def delete_membro_by_id(membro_id):
    sql = "DELETE FROM webuser.TB_MEMBROS WHERE id = %s"
    value = [membro_id]
    run_sql(sql, value)

def edit_membro(membro):
    sql = "UPDATE webuser.TB_MEMBROS SET (nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.tipo_plano.id, membro.data_inicio, membro.ativo, membro.id]
    run_sql(sql, values)