from .pessoa import Pessoa
from rich import print


class Aluno(Pessoa):
    cursos_oficiais = ["ADM", "CC", "ENG", "CONT"]

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = curso

    def add_curso(self, curso):
        curso = curso.upper()
        if 3 <= len(curso) < 6 and curso not in Aluno.cursos_oficiais:
            Aluno.cursos_oficiais.append(curso)
        else:
            print("[red]Curso inválido![/]")

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, materia):
        if materia not in self.cursos_oficiais:
            print(f"[red]{materia} não é um curso oficial![/]")
        else:
            self._curso = materia
