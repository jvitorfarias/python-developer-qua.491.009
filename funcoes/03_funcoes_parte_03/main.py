# importa modulo
import modulo as m

# algoritmo principal
if __name__ == "__main__":
    while True:
        print("1 - Calcular quadrado.")
        print("2 - Calcular retângulo.")
        print("3 - Calcular triângulo.")
        print("4 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()        
        m.limparTela()
        match opcao:
            case "1":
                try:
                    l = int(input("Informe o lado do quadrado: "))
                    a = m.areaQuadrado(l)

                    print(f"Área do quadrado: {a}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue 
            case "2":
                try:
                    b = int(input("Informe a base do retângulo: "))
                    h = int(input("Informe a altura do retângulo: "))
                    a = m.areaRetangulo(b, h)

                    print(f"Área do retângulo: {a}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                try: 
                    b = int(input("Informe a base do triangulo: "))
                    h = int(input("Informe a altura do triangulo: "))
                    a = m.areaTriangulo(b, h)
                    
                    print(f"Área do triângulo: {a}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "4":
                print("Programa encerrado!")
                break
            case _:
                print("Opção inválida!")
                continue