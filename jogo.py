#jogo da forca carlos
import os
import random
def forca(erro):
    os.system('cls')
    if erro == 0:
        print("  _____ ")
        print(' |      |')
        print( "   ","    |")
        print("   ","    |")
        print("   ","    |")
        print("________|")
    if erro == 1:
        print("  _____ ")
        print(' |      |')
        print(" o ", "    |")
        print("   ", "    |")
        print("   ", "    |")
        print("________|")
    if erro == 2:
        print("  _____ ")
        print(' |      |')
        print(" o ", "    |")
        print(" | ", "    |")
        print("   ", "    |")
        print("________|")
    if erro == 3:
        print("  _____ ")
        print(' |      |')
        print(" o ", "    |")
        print("/| ", "    |")
        print("   ", "    |")
        print("________|")
    if erro == 4:
        print("  _____ ")
        print(' |      |')
        print(" o ", "    |")
        print("/|\ ", "   |")
        print("   ", "    |")
        print("________|")
    if erro == 5:
        print("  _____ ")
        print(' |      |')
        print(" o ", "    |")
        print("/|\  ", "  |")
        print("/  ", "    |")
        print("________|")
    if erro == 6:
        print("  _____ ")
        print(' |      |')
        print(" o ", "    |")
        print("/|\ ", "   |")
        print("/ \  ", "  |")
        print("________|")
        print("GAME OVER")
        exit()
erro = 0
resul = []
xpala =[]
xnum =random.randrange(0,4)
arq =open("arquivo.txt",'r')
linha = arq.readline()
for linha in arq:
    linha = linha.strip()
    xpala.append(linha)
print(xpala)
var = xpala[xnum]
cont =len(var)
lerrada =[]
letra = ''
pa =[]
for t in range(0,cont):
    pa.append('_')
for x in var:
    resul.append(x)
while erro != 7:
    forca(erro)
    print("Letras certas")
    print(pa)
    print('Letra erradas')
    print(lerrada)
    letra = input('Qual e a letra:')
    p=''
    for y in range(0, cont):
        if letra == resul[y]:
            pa[y] = resul[y]
            p =True
    if pa == resul:
        print(pa)
        print('FIM DE JOGO VC GANHO')
        erro = 7
    if not p:
        erro += 1
        lerrada.append(letra)

