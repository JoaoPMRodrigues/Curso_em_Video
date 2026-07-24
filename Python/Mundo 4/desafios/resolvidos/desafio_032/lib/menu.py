from .contabancaria import ContaBancaria
from rich.table import Table
from rich import print, inspect
from pwinput import pwinput


class Menu:
    def __init__(self, conta: ContaBancaria):
        self.opcao = 0
        self.conta = conta
        self.fim = False

    def criarMenu(self):
        tabela = Table(title="[blue]Banco Master[/]", style="blue")
        tabela.add_column("[bold]#[/]", justify="left")
        tabela.add_column("[bold]Opção[/]")
        tabela.add_row("1.", "Mostrar saldo")
        tabela.add_row("2.", "Depósito")
        tabela.add_row("3.", "Saque")
        tabela.add_row("4.", "Trocar Titular")
        tabela.add_row("5.", "Trocar senha")
        tabela.add_row("6.", "Inspecionar conta")
        tabela.add_row("7.", "Sair")
        print(tabela)
        self.opcao = int(input("Qual opção você deseja? "))
        self.realizaOpção()

    def realizaOpção(self):
        match self.opcao:
            case 1:
                mensagem = f"Olá {self.conta.titular}, seu saldo é de [blue]R${self.conta.saldo:.2f}[/]"
                print(mensagem)
            case 2:
                deposito = int(input("Quanto você quer depositar? "))
                self.conta.depositar(deposito)
            case 3:
                saque = int(input("Quanto você quer sacar? "))
                self.conta.sacar(saque)
            case 4:
                novoTitular = str(input("Quem será o novo titular da conta? "))
                self.conta.titular = novoTitular
            case 5:
                novaSenha = str(pwinput("Qual será a nova senha? "))
                self.conta.senha = novaSenha
            case 6:
                inspect(self.conta, title=f"Conta do {self.conta.titular}")
            case 7:
                print("[green]Obrigado e volte sempre![/]")
                self.fim = True
            case _:
                print("[red]Opção inválida[/]")
