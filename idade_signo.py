#calcula idade

#=> Mostra a idade e signo

dia = input("Digite o dia do seu nascimento\n")
mes = input("Digite o mês do seu nascimento\n")
nascimento = input("Digite o ano do seu nascimento\n")
atual = input("Digite o ano atual\n")


def Calcula(atual, nascimento):
    calc = int(atual) - int(nascimento)
    print("\n Sua idade é "+ str(calc))
Calcula(atual, nascimento)


def BuscaSigno(dia, mes):   
    if(dia >="21" and mes == "1") or (dia >="18" and mes == "2"):
            print("\n Seu signo é aquário")
    elif(dia >="19" and mes == "2") or (dia >="20" and mes == "3")
            print("\n Seu signo é peixes")
    elif(dia >="21" and mes == "3") or (dia >="20" and mes == "4")
            print("\n Seu signo é áries")
    elif(dia >="21" and mes == "4") or (dia >="20" and mes == "5")
            print("\n Seu signo é touro")
    elif(dia >="21" and mes == "6") or (dia >="20" and mes == "7")
            print("\n Seu signo é gêmeos")
    elif(dia >="23" and mes == "7") or (dia >="22" and mes == "8")
            print("\n Seu signo é câncer")
            
    
BuscaSigno(dia,mes)
