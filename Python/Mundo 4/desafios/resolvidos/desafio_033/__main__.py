from .lib import Aluno
from rich import inspect


def main():
    a1 = Aluno("João", 2007, "CC")
    a1.add_curso("SIN")
    inspect(a1)


if __name__ == "__main__":
    main()
