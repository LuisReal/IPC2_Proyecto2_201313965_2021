import time
import os
class Cronometro:

    def __init__(self):
        pass

    def crono(self):

        for hora in range(24):
            for minuto in range(60):
                for segundo in range(60):
                    os.system('cls')
                    print(hora,":",minuto,":",segundo)
                    time.sleep(1)


