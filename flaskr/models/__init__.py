from peewee import *

db = SqliteDatabase("./flaskr/database.db")

class BaseModel(Model):
    class Meta:
        database = db

class Proprietario(BaseModel):
    nome = CharField()
    cpf = CharField(unique=True)
    email = CharField(unique=True)
    telefone = CharField()
    endereco = TextField(null=True)

class Tipo(BaseModel):
    descricao = CharField(unique=True)

class Cor(BaseModel):
    descricao = CharField(unique=True)

class Veiculo(BaseModel):
    placa = CharField(unique=True)
    modelo = CharField()
    tipo = ForeignKeyField(Tipo, backref="veiculos")
    cor = ForeignKeyField(Cor, backref="veiculos")
    proprietario = ForeignKeyField(Proprietario, backref="veiculos")

class Movimentacao(BaseModel):
    veiculo = ForeignKeyField(Veiculo, backref="movimentacoes")
    data_entrada = DateTimeField()
    data_saida = DateTimeField(null=True)
    total = DecimalField(null=True)

class TabelaPreco(BaseModel):
    descricao = CharField()
    tipo = ForeignKeyField(Tipo, backref="tabela_precos")
    primeira_hora = DecimalField()
    demais_horas = DecimalField()
