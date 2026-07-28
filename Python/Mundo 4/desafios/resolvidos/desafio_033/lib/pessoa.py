from rich import print
from abc import ABC
from datetime import date


class Pessoa(ABC):
    ano = date.today().year

    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        if 1915 <= self.nascimento <= Pessoa.ano:
            self._nascimento = nascimento
            self.idade = Pessoa.ano - self._nascimento
        else:
            raise ValueError(f"\033[31mAno {nascimento} é inválido!\033[0m")

    @property
    def idade(self):
        return Pessoa.ano - self.nascimento

    @idade.setter
    def idade(self, idade=None):
        raise PermissionError(
            "\033[31mVocê não tem permição de alterar a idade\033[0m")
