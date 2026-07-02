from rich import print


class Termostato:
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura % 0.5:
            raise ValueError(
                f"\033[31mTemperatura de {temperatura}{chr(176)}C inválida!\033[0m")

        if 16 <= temperatura <= 30:
            self.__temperatura = temperatura
        elif temperatura < 16:
            self.__temperatura = 16
        else:
            self.__temperatura = 30

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"
