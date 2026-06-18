print('=' * 30)
print('⚠ Um Troll da Floresta apareceu!')
print('=' * 30)

import os
import random

usuario_vida = 100
usuario_atk = 25
usuario_def = 20

troll_vida = 100
troll_atk = 20
troll_def = 15

print('Troll da floresta \nVida: {}'.format(troll_vida))

while troll_vida > 0:

    print('════════ COMBATE ═════════')
    print('')
    print('Jogador')
    print('Vida: {}'.format(usuario_vida))
    print('')
    print('Troll da Floresta')
    print('Vida: {}'.format(troll_vida))
    print(' ')
    print('══════════════════════════')

    usuario = int(input('\nO que deseja fazer? \n\n[ 1 ] Atacar \n[ 2 ] Defender\n[ 3 ] Inventario\n[ 4 ] Fugir\n>>>>'))

    maquina = random.randint(1,3)  

    if usuario == 1:
        os.system('cls' and 'clear')
        print('Você ataca o Troll!')
        print('Dano causado: {}'.format(usuario_atk))
        troll_vida -= usuario_atk
        print('Vida do troll: {}'.format(troll_vida))
        if maquina == 1:
            print('\nTroll atacou voce')
            print('Dano causado: {}'.format(troll_atk))
            usuario_vida -= troll_atk
            print('Sua vida: {}\n'.format(usuario_vida))

    if usuario == 2:
        os.system('cls' and 'clear')
        print('\nVocê defendeu o Troll!')
        print('Dano causado: {}'.format((troll_atk) - 10))
        usuario_vida -= troll_atk
        print('Vida do usuario: {}\n'.format(usuario_vida))
        if maquina == 2:
            print('\nTroll defendeu teu ataque')
            print('\nDano causado: {}'.format(usuario_atk) - 10)
            usuario_vida -= troll_atk
            print('\nSua vida: {}\n'.format(usuario_vida))

    elif usuario == 3:
        print('desenvolvendo')

    elif usuario == 4:
        print('Voce fugiun do Troll da floresta, que ele nao te encontre!')
        break


os.system('cls' and 'clear')
print('Parabens voce ganhou do Troll!')