from PIL import Image
import os

# => Ele mostra o tamanho da imagem

#Limpa tela
os.system('cls') 

#Diretório da imagem, aqui pode ser colocado diretório que costuma está imagens. 
#Exemplos: download ou desktop.
dire = input("\n\n  Cole o diretório do arquivo:   ")
#Nome da imagem
img_nome = input("  Digite o nome da imagem:  ")
#Separador do diretorio e imagem "local\img"
separador = "\\"
#Formato da imagem, pode ser alterado.
formato = "JPG"

#Caminho da imagem 
img = dire + separador + img_nome +"." +formato

#Selecione a imagem e guardar numa variável
im = Image.open(img)

#Função
#Mostrar a largura, altura e formato da imagem


def MostraTamanho(im):
    #Tamanho da imagem
    tamanho = im.size
    #Mostra altura e largura da imagem
    print("\n\n     Formato -", im.format)
    print("     Largura:", tamanho[0])
    print("     Altura:", tamanho[1])

MostraTamanho(im)


