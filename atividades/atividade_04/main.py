# bibliotecas
import os
import time
import datetime

# declaracao de variaveis



# exibe a hora atual
while True:
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Hora atual: {hora}")
    time.sleep(1)
