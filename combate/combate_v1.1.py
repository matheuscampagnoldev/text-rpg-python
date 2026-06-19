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

    usuario = int(input('\nO que deseja fazer? \n\n[ 1 ] Atacar \n[ 2 ] Defender\n[ 3 ] Fugir\n>>>>')) 

    maquina = random.randint(1,3) 
    
    if usuario == 1 and maquina == 1:
        print('Você ataca o Troll!')
        print('Dano causado: {}'.format(usuario_atk))
        troll_vida -= usuario_atk
        print('Vida do troll: {}'.format(troll_vida))
    elif usuario == 1 and maquina == 2:
        print('Você ataca o Troll!')
        print('Dano causado: {}'.format(usuario_atk))
        troll_vida -= usuario_atk
    elif usuario == 2:
        print('\nVocê entrou em modo de defesa')
        print('Voce ira receber -10 de dano!: {}'.format((troll_atk - 10) ))
        print('Vida do usuario: {}\n'.format(usuario_vida)) 
    elif usuario == 3:
        print('Voce fugiu do Troll da floresta, que ele nao te encontre!')
        break

    if troll_vida > 0:
        if maquina == 1 and usuario == 2:
            print('\nTroll atacou voce')
            print('Dano causado: {}'.format(troll_atk)) 
            usuario_vida -= (troll_atk - 10)
            print('Sua vida: {}\n'.format(usuario_vida))
        elif maquina == 1:
            print('\nTroll atacou voce')
            print('Dano causado: {}'.format(troll_atk)) 
            usuario_vida -= troll_atk
            print('Sua vida: {}\n'.format(usuario_vida))
        if maquina == 2 and usuario == 1:
            print('\nTroll defendeu teu ataque')
            print('\nDano causado foi reduzido: {}'.format(usuario_atk - 10))
            troll_vida += 10
            print('Vida do troll: {}'.format(troll_vida))
        if maquina == 3:
            print('O troll fugiu de volta a Floresta Sombria')
            break
    else:
        os.system('cls' or 'clear')
        print('Voce matou o troll!')
        break

    if usuario_vida <= 0:
        print('Voce perdeu')
        break