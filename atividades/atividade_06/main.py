# TODO -- ativiadade: Crie um programa em que o usuário informa um ano e o programa exibe todo o calendário do ano informado pelo usuário.
# NOTE -- o usuário poderá informar qualquer ano a partir de 1900.
# NOTE -- use a biblioteca calendar.

import calendar
import os

# declarando variavel

anoInserido = int(input("Informe um ano a partir de 1900: "))

print(calendar.calendar(anoInserido))