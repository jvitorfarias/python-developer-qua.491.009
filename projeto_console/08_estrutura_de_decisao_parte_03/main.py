# declaracao de variaveis
aluno = input("Informe o nome do aluno: ")
media = float(input("Informe a media do aluno: ").replace(',', '.'))

# estrutura de decisao
if media >= 0 and media <= 10:
    if media >= 7:
        print(f"{aluno} está aprovado.")
    elif media >= 5:
        print(f"{aluno} está de recuperação.")
    else:
        print(f"{aluno} está reprovado.") 
else:
    print("Nota inválida.")