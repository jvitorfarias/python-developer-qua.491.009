# atividade: crie um programa que calcule a área e circunferencia de um circulo utilizando lambda.
import math
import os

pi = math.pi
x = pi

# calculo area
area = lambda r: (r*r)*pi


# calculo circunferencia
circ = lambda x, r: (2*x)*r

print("O que você deseja calcular")
print("1 - Calcular a Área do círculo")
print("2 - Calcular a circunferência do círculo")
opcao = input("Digite o número da opção desejada: ")
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    try:
        match opcao:
            case "1":
                limpar()
                r = float(input("Qual o raio do círculo: ").replace(",", "."))
                a = area(r)

                print(f"A área do círculo com {r} de raio é: {a:.2f}")
            case "2":
                limpar()
                r = float(input("Qual o raio do círculo: ").replace(",", "."))
                c = circ(x, r)

                print(f"A circunferência do círculo com {r} de raio é: {c:.2f}")
    except Exception as e:
        print(f"Não foi possível realizar o calculo. {e}.")