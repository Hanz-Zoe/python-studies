from classes.plano import TipoPlano
from database.run_sql import run_sql

def get_all_tipos_planos():
    tipos_planos = []
    sql = "SELECT * FROM webuser.TB_PLANOS"
    results = run_sql(sql)

    for row in results:
        tipo_plano = TipoPlano(row["plano"], row["id"])
        tipos_planos.append(tipo_plano)

    return tipos_planos

def get_tipo_plano_by_id(tipo_plano_id):
    sql = "SELECT * FROM webuser.TB_PLANOS WHERE id = %s"
    value = [tipo_plano_id]
    result = run_sql(sql, value)[0] if run_sql(sql, value) else None

    return TipoPlano(result["plano"], result["id"]) if result else None

def insert_tipo_plano(tipo_plano):
    sql = "INSERT INTO webuser.TB_PLANOS (plano) VALUES (%s) RETURNING *;"
    values = [tipo_plano.plano]
    result = run_sql(sql, values)
    tipo_plano.id = result[0]["id"] if result else None

    return tipo_plano

def delete_tipo_plano_by_id(tipo_plano_id):
    sql = "DELETE FROM webuser.TB_PLANOS WHERE id = %s"
    value = [tipo_plano_id]
    run_sql(sql, value)

def edit_tipo_plano(tipo_plano):
    sql = "UPDATE webuser.TB_PLANOS SET (plano) = (%s) WHERE id = %s;"
    values = [tipo_plano.plano, tipo_plano.id]
    run_sql(sql, values)