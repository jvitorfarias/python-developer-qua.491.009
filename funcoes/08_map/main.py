# lambda
pa = lambda x: x*2

# algoritmo principal
if __name__ == "__main__":
    # lista
    numeros = [1, 2, 3, 4, 5, 6]

    # exibe o pg
    print(f"Progressão aritmética: {list(map(pa, numeros))}")