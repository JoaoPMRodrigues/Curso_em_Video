from rich import print


class Diario:
    def __init__(self, senha="senha"):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, mensagem):
        if isinstance(mensagem, str) and len(mensagem) > 0:
            self.__segredos.append(mensagem)

    def ler(self, senha=""):
        if senha != self.__senha:
            raise PermissionError(
                "\033[31mVocê não tem permissão para ler!\033[0m")
        for segredo in self.__segredos:
            print(f"- {segredo}")

    @property
    def senha(self):
        raise PermissionError(
            f"\033[31mNinguém tem permissão de ver a senha!\033[0m")

    @senha.setter
    def senha(self, senhas=("", "")):
        senha_antiga, senha_nova = senhas
        if (senha_antiga != self.__senha):
            raise PermissionError(
                "\033[31mSenha errada!\033[0m")
        else:
            self.__senha = senha_nova
