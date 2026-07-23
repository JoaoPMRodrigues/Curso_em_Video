from hashlib import sha256


class Credencial:
    def __init__(self, senha):
        self.__hash = self.criarHash(senha)

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        valida = True
        if len(chave) < 1 or len(chave) > 12:
            valida = False
        if " " in chave:
            valida = False

        if valida:
            self.__hash = self.criarHash(chave)
        else:
            print("[red]Senha invalida![/]")
            raise ValueError()

    def validar(self, chave):
        usuario = sha256(chave.encode("utf-8")).hexdigest()
        if usuario == self.__hash:
            return True
        return False

    def criarHash(self, chave):
        codigo = sha256(chave.encode("utf-8"))
        return codigo.hexdigest()
