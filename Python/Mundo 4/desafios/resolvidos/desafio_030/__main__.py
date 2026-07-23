from .lib import Diario
from rich import inspect
from rich.traceback import install
install()


def main():

    d = Diario("rayan")
    d.escrever("Oi", "rayan")
    d.escrever("Boa noite", "rayan")
    d.escrever("Será que vai ter gol do Rayan hoje", "rayan")

    d.ler("rayan")
    inspect(d, methods=True, private=True)


if __name__ == "__main__":
    main()
