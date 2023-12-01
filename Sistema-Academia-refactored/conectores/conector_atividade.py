import conectores.conector_plano as plano
from database.run_sql import run_sql
from classes.atividade import Atividade
from classes.membro import Membro

def get_all_atividades():
    atividades = []
    sql = "SELECT * FROM webuser.TB_ATIVIDADES"
    results = run_sql(sql)

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

def get_members_by_atividade_id(atividade_id):
    membros = []
    sql = "SELECT webuser.TB_MEMBROS.* FROM webuser.TB_MEMBROS INNER JOIN webuser.TB_AGENDAMENTOS ON membros.id = webuser.TB_AGENDAMENTOS.membro WHERE webuser.TB_AGENDAMENTOS.atividade = %s"
    value = [atividade_id]
    results = run_sql(sql, value)

    for row in results:
        membro = Membro(row["nome"],
                        row["sobrenome"],
                        row["data_nascimento"],
                        row["endereco"],
                        row["telefone"],
                        row["email"],
                        row["tipo_plano"],
                        row["data_inicio"],
                        row["ativo"],
                        row["id"])
        membros.append(membro)

    return membros

def get_all_active_atividades():
    atividades = []
    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE ativo = true ORDER BY data ASC"
    results = run_sql(sql)

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

def get_all_inactive_atividades():
    atividades = []
    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE ativo = false ORDER BY data ASC"
    results = run_sql(sql)

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

def get_atividade_by_id(atividade_id):
    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE ativo = true AND id = %s"
    value = [atividade_id]
    result = run_sql(sql, value)[0] if run_sql(sql, value) else None

    return Atividade(result["nome"],
                     result["instrutor"],
                     result["data"],
                     result["duracao"],
                     result["capacidade"],
                     plano.get_one(result["tipo_plano"]),
                     result["ativo"],
                     result["id"]) if result else None

def insert_atividade(atividade):
    sql = "INSERT INTO webuser.TB_ATIVIDADES (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;"
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade, atividade.tipo_plano, atividade.ativo]
    result = run_sql(sql, values)
    atividade.id = result[0]["id"] if result else None

    return atividade

def delete_atividade_by_id(atividade_id):
    sql = "DELETE FROM webuser.TB_ATIVIDADES WHERE id = %s"
    value = [atividade_id]
    run_sql(sql, value)

def edit_atividade(atividade):
    sql = "UPDATE webuser.TB_ATIVIDADES SET (nome, instrutor, data, duracao, capacidade, tipo_plano, ativo) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s;"
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade, atividade.tipo_plano, atividade.ativo, atividade.id]
    run_sql(sql, values)