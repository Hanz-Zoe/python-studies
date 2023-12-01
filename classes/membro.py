class Membro:
    def __init__(self, nome, sobrenome, data_nascimento, endereco, telefone, email, tipo_plano, data_inicio, ativo, id=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d') if data_nascimento else None
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.tipo_plano = tipo_plano
        self.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d') if data_inicio else None
        self.ativo = ativo
        self.id = id