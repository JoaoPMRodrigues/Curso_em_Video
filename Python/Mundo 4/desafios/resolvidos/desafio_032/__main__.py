from .lib import ContaBancaria, Menu
from random import randint
from pwinput import pwinput
from rich import print
from rich.traceback import install
install()


def main():

    try:
        print("Olá, seja bem vindo ao banco Gafanhoto!")
        id = randint(100, 999)
        nome = str(input("Informe seu nome: "))
        saldo = float(input("Informe seu saldo: "))
        senha = str(pwinput("Informe sua senha: ")).strip()

        cc = ContaBancaria(id, nome, saldo, senha)
        menu = Menu(cc)

        while True:

            menu.criarMenu()
            if menu.fim:
                break

    except KeyboardInterrupt:
        print("[red]Código interrompido pelo usuário! =( [/]")


if __name__ == "__main__":
    main()
