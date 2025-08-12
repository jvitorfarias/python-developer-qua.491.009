class Aluno:
    def __init__(self, nomeAluno, matricula):
        self.__nomeAluno = nomeAluno
        self.__matricula = matricula
        self.cursosInscritos = []


    @property
    def nomeAluno(self):
        self.__nomeAluno

    @nomeAluno.setter
    def nomeAluno(self, nomeAluno):
        self.__nomeAluno = nomeAluno

    @property
    def matricula(self):
        self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    # metodos de acao
    def inscreverCurso(self, curso):
        if curso not in self.cursosInscritos:
            self.cursosInscritos.append(curso)
            curso.adicionarAluno(self) # Associa o aluno ao curso

    def listarCursos(self):
        lista = []
        for curso in self.cursosInscritos:
            lista.append(curso.nomeCurso)
        return lista