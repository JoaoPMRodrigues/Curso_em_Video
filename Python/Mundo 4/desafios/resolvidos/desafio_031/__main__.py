from .lib import Retangulo
from rich import print, inspect
from rich.traceback import install
install()


def main():
    try:
        ret = Retangulo(9, 9)
        ret.base = 14
        ret.altura = 10
        inspect(ret, private=True, methods=True)
        ret.medidas = (5, -2)
        print(ret.medidas)
        inspect(ret, private=True, methods=True)
    except Exception as e:
        print(f"[red]Ocorreu um erro do tipo: {type(e)}[/]")


if __name__ == "__main__":
    main()
