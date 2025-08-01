import os

#    funcao normal
#   def somar(x, y):
#       result = x + y
#       return result
#   

# funcao lambda
somar = lambda x, y: x + y
limpar = lambda: os.sistem("cls" if os.name == "nt" else clear)

# algoritmo principal
if __name__ == "__main__":
    try:
        x = int(input("Informe o valor de x: "))
        y = int(input("Informe o valor de y: "))
        result = somar(x + y)

        print(f"O resultado da soma é {result}.")

    except Exception as e:
        print(f"Não foi possível somar. {e}.")