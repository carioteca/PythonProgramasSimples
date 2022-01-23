import os
import time

r = 0
while r == 0:
    pass
    nome = input(' Digite o nome: ')
    pos =  nome.find(' ')
    nome = nome[0:pos]
    nome = nome.capitalize()
    nome = nome +"."
    os.system('cls' if os.name == 'nt' else 'clear')
    print(nome)
    time.sleep(20)
    os.system('cls' if os.name == 'nt' else 'clear')
    