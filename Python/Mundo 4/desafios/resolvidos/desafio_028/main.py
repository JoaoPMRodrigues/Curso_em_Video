from classes import Termostato
from rich import print, inspect


def main():
    termostato = Termostato()
    termostato.temperatura = 16.5
    inspect(termostato, private=True, methods=True)

    print(f"A sua temperatura é de: {termostato.ftemperatura}")
    try:
        termostato.ftemperatura = 10
    except Exception as e:
        print(f"Houve um problema: \n{e}")


if __name__ == "__main__":
    main()
