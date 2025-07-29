# imports
import os

# funcoes
def areaQuadrado(l):
    a = l**2
    return a

def areaRetangulo(b, h):
    a = b*h
    return a

def areaTriangulo(b, h):
    a = (b*h)/2
    return a

def limparTela():
    os.system("cls" if os.name == "nt" else "clear")