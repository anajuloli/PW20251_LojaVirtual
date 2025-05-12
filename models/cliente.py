from dataclasses import dataclasses
import datetime

@dataclasses
class Cliente:
    id: int
    nome: str
    cpf: str
    telefone: str
    email: str
    data_nascimento: datetime