class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        self._area = base*altura
        self._medidas = (base, altura)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, int) and not isinstance(base, float):
            raise TypeError("O valor da base deve ser um número!")
        if base < 0:
            raise TypeError("Valor Inválido para base!")

        self._base = base
        self._area = self._base*self._altura
        self._medidas = (self._base, self._altura)

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, int) and not isinstance(altura, float):
            raise TypeError(
                "mO valor da altura deve ser um número!")

        if altura < 0:
            raise TypeError("Valor Inválido para altura!")

        self._altura = altura
        self._area = self._base*self._altura
        self._medidas = (self._base, self._altura)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self):
        raise PermissionError(
            "Não é possível mexer na área isoladamente!")

    @property
    def medidas(self):
        mensagem = f"Base = {self._base}\nAltura = {self._altura}\nÁrea = {self._area}"
        return mensagem

    @medidas.setter
    def medidas(self, medidas: tuple):
        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem ser informadas em tupla")
        if len(medidas) != 2:
            raise SyntaxError("Informe a tupla com apenas 2 valores numéricos")

        self.base = medidas[0]
        self.altura = medidas[1]
