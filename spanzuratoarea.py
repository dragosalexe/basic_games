import random

def checkCuvant(litera):
    gasit = 0
    for i,item in enumerate(cuvant):
        if item == litera:
            copie_lista[i]=item
            print('Litera se gaseste in pozitia ', i)
            gasit = 1
    if gasit:
        return 1
    else:
        return 0


def checkGameOver():
    if copie_lista == list(cuvant):
        print('Felicitari. Ai ghicit cuvantul.')
        return 1
    else:
        return 0

print("Bun venit la spanzuratoarea. Cuvantul va fi ales random dintr-o lista.")

lista_totala_cuvinte = ['ghicitoare','canapea','televizor','monosilabic','masa','casa','cer','dinozaur','sarpe']
cuvant = lista_totala_cuvinte[random.randint(0,len(lista_totala_cuvinte))]
cuvant.lower()
lungime_cuvant = len(cuvant)


copie = '*' * lungime_cuvant
copie_lista = list(copie)


print(copie, 'sal')
nr_incercari = 5
gameOver = 0

while(nr_incercari !=0 and gameOver==0):
    allowed_letters = 'abcdefghifjklmnopqrstuvwxyz'
    litera = input('Introdu o litera: ')

    while len(litera)!=1 or litera not in allowed_letters:
        litera = input('Reincearca: ')

    if checkCuvant(litera):
        print(''.join(copie_lista))
        if checkGameOver():
            gameOver=1
    else:
        nr_incercari-=1
        print(f'Litera nu se gaseste. Mai ai {nr_incercari} incercari')

if nr_incercari == 0:
    print('game over, ai pierdut')

exita = input('Press any key to exit')