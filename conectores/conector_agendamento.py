from database.run_sql import run_sql
from classes.agendamento import Agendamento

def get_all_agendamentos():
    agendamentos = []
    sql = "SELECT * FROM webuser.TB_AGENDAMENTOS"
    results = run_sql(sql)

    for row in results:
        agendamento = Agendamento(row["atividade"], row["membro"], row["id"])
        agendamentos.append(agendamento)

    return agendamentos

def get_agendamento_by_id(agendamento_id):
    sql = "SELECT * FROM webuser.TB_AGENDAMENTOS WHERE id = %s"
    value = [agendamento_id]
    result = run_sql(sql, value)[0] if run_sql(sql, value) else None

    return Agendamento(result["atividade"], result["membro"], result["id"]) if result else None

def insert_agendamento(agendamento):
    sql = "INSERT INTO webuser.TB_AGENDAMENTOS (atividade, membro) VALUES (%s, %s) RETURNING *;"
    values = [agendamento.atividade.id, agendamento.membro.id]
    result = run_sql(sql, values)
    agendamento.id = result[0]["id"] if result else None

    return agendamento

def delete_agendamento_by_id(agendamento_id):
    sql = "DELETE FROM webuser.TB_AGENDAMENTOS WHERE id = %s"
    value = [agendamento_id]
    run_sql(sql, value)

def agendamento_exists(atividade, membro):
    sql = "SELECT * FROM webuser.TB_AGENDAMENTOS WHERE atividade = %s AND membro = %s"
    values = [atividade, membro]
    results = run_sql(sql, values)

    return bool(results)

def delete_agendamento_by_membro_atividade(membro, atividade):
    sql = "DELETE FROM webuser.TB_AGENDAMENTOS WHERE membro = %s AND atividade = %s"
    values = [membro, atividade]
    run_sql(sql, values)