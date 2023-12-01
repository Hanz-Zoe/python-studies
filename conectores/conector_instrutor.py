from database.run_sql import run_sql
from classes.instrutor import Instrutor
from classes.atividade import Atividade

def get_all_instrutores():
    instrutores = []
    sql = "SELECT * FROM webuser.TB_INSTRUTORES"
    results = run_sql(sql)

    for row in results:
        instrutor = Instrutor(row["nome"],
                              row["sobrenome"],
                              row["data_nascimento"],
                              row["endereco"],
                              row["telefone"],
                              row["id"])
        instrutores.append(instrutor)

    return instrutores

def get_instrutor_by_id(instrutor_id):
    sql = "SELECT * FROM webuser.TB_INSTRUTORES WHERE id = %s"
    value = [instrutor_id]
    result = run_sql(sql, value)[0] if run_sql(sql, value) else None

    return Instrutor(result["nome"],
                     result["sobrenome"],
                     result["data_nascimento"],
                     result["endereco"],
                     result["telefone"],
                     result["id"]) if result else None

def get_activities_by_instrutor_id(instrutor_id):
    atividades = []
    sql = "SELECT * FROM webuser.TB_ATIVIDADES WHERE instrutor = %s"
    value = [instrutor_id]
    results = run_sql(sql, value)

    for row in results:
        atividade = Atividade(row["nome"],
                              row["instrutor"],
                              row["data"],
                              row["duracao"],
                              row["capacidade"],
                              row["tipo_plano"],
                              row["ativo"],
                              row["id"])
        atividades.append(atividade)

    return atividades

def insert_instrutor(instrutor):
    sql = "INSERT INTO webuser.TB_INSTRUTORES (nome, sobrenome, data_nascimento, endereco, telefone) VALUES (%s, %s, %s, %s, %s) RETURNING *;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone]
    result = run_sql(sql, values)
    instrutor.id = result[0]["id"] if result else None

    return instrutor

def delete_instrutor_by_id(instrutor_id):
    sql = "DELETE FROM webuser.TB_INSTRUTORES WHERE id = %s"
    value = [instrutor_id]
    run_sql(sql, value)

def edit_instrutor(instrutor):
    sql = "UPDATE webuser.TB_INSTRUTORES SET (nome, sobrenome, data_nascimento, endereco, telefone) = (%s, %s, %s, %s, %s) WHERE id = %s;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone, instrutor.id]
    run_sql(sql, values)