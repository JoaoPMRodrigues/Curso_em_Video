from rich import print
from hashlib import sha256
from pwinput import pwinput


class ContaBancaria:
    """
    Essa classe cria a conta bancária de uma pessoa. Para criar uma nova conta, faça: 
    variavel = ContaBancaria(id, nome, saldo, senha)
    """

    def __init__(self, id: int, nome: str = None, saldo: float = 0, senha: str = None):
        self._titular = nome
        self._id = id
        self.__saldo = saldo
        if senha is None:
            senha = self.pedirSenha()
        self._senha = sha256(senha.encode("utf-8")).hexdigest()

        print(
            f"[blue]Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}[/]")

    def pedirSenha(self):
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break

        return senha

    def validarSenha(self, chave: str):
        if chave is None:
            chave = self.pedirSenha()

        usuario = sha256(chave.encode("utf-8")).hexdigest()
        if usuario == self._senha:
            return True
        return False

    def depositar(self, valor=0):
        valor = abs(valor)
        print(
            f"[green]Depósito de R${valor:,.2f} autorizado na conta {self._id}![/]")
        self.__saldo += valor

    def sacar(self, valor: float):
        valor = abs(valor)

        chave = str(pwinput("Senha: "))
        if self.validarSenha(chave):
            if valor <= self.__saldo:
                print(
                    f"[green]Saque de R${valor:,.2f} autorizado na conta {self._id}.\033[/]")
                self.__saldo -= valor
            else:
                print(f"[red]Saldo insuficiente! Saque recusado.[/]")

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        chave = str(pwinput("Senha: "))
        if self.validarSenha(chave):
            self._senha = sha256(senha.encode("utf-8")).hexdigest()

    @property
    def saldo(self):
        chave = str(pwinput("Senha: "))
        if self.validarSenha(chave):
            return self.__saldo

    @saldo.setter
    def saldo(self):
        raise PermissionError("Você não tem permissão para mexer no saldo")

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        chave = str(pwinput("Senha: "))
        if self.validarSenha(chave):
            self._titular = titular
