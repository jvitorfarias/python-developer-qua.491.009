class Curso:
    def __init__(self, nomeCurso):
        self.__nomeCurso = nomeCurso
        self.alunosInscritos = []

    @property
    def nomeCurso(self):
        return self.__nomeCurso

    @nomeCurso.setter
    def nomeCurso(self, nomeCurso):
        self.__nomeCurso = nomeCurso

    #metodos de acao
    def adicionarAluno(self, aluno):
        if aluno not in self.alunosInscritos:
            self.alunosInscritos.append(aluno)
    
    def listarAlunos(self):
        lista = []
        for aluno in self.alunosInscritos:
            lista.append(aluno.nomeAluno)
        return lista