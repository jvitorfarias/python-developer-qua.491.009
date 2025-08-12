import Curso
import Aluno

def main():
    curso1 = Curso.Curso(nomeCurso = "Python")
    curso2 = Curso.Curso(nomeCurso = "Java")
    aluno1 = Aluno.Aluno(nomeAluno = "Harry", matricula = "1")
    aluno2 = Aluno.Aluno(nomeAluno = "Hermione", matricula = "2")
    aluno3 = Aluno.Aluno(nomeAluno = "Rony", matricula = "3")
    aluno4 = Aluno.Aluno(nomeAluno = "Sirius", matricula = "4")
    aluno5 = Aluno.Aluno(nomeAluno = "Tom", matricula = "5")
    aluno6 = Aluno.Aluno(nomeAluno = "Snape", matricula = "6")

    # inscrevendo alunos no curso2
    aluno1.inscreverCurso(curso2)
    aluno2.inscreverCurso(curso2)
    aluno3.inscreverCurso(curso2)
    aluno4.inscreverCurso(curso2)
    
    # inscrevendo alunos no curso1
    aluno5.inscreverCurso(curso1)
    aluno6.inscreverCurso(curso1)
    
    # lista de alunos no curso1
    print(f"Curso: {curso2.nomeCurso}")
    print("Lista de alunos: ")
    for aluno in curso2.listarAlunos():
        print(aluno)

if __name__ == "__main__":
    main()