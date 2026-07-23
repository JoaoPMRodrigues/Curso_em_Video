from rich import print
from .credencial import Credencial


class Diario:
    def __init__(self, senha="senha"):
        self.__segredos = []
        self.__senha = Credencial(senha)

    def escrever(self, mensagem, senha):
        if self.__senha.validar(senha):
            self.__segredos.append(mensagem)
        else:
            print("[red]Você não tem permissão para ler![/]")
            raise PermissionError()

    def ler(self, senha=""):
        if self.__senha.validar(senha):
            for segredo in self.__segredos:
                print(f"- {segredo}")
        else:
            print("[red]Você não tem permissão para ler![/]")
            raise PermissionError()

    @property
    def senha(self):
        return self.__senha.senha

    @senha.setter
    def senha(self, senha):
        if self.__senha.validar(senha):
            self.senha.__hash__ = senha
