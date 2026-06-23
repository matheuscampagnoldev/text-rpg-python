print('════════ COMBATE ════════')
print('⚠ Um Troll da Floresta apareceu!')
print('═════════════════════════')

import random

jogador_vida = 100
jogador_atk = 25
jogador_def = 20

jogador_defTF = False

troll_vida = 100
troll_atk = 20
troll_def = 15


while True:

    print('════════ COMBATE ════════')
    print(f'Jogador: {jogador_vida}')
    print(f'Troll: {troll_vida}')
    print('════════════════════════')

    jogador = int(input('[ 1 ] Atacar \n[ 2 ] Defender \n[ 3 ] Fugir \n>>>> '))
    maquina = random.randint(1,4)

    if jogador == 1:
        print('⚔ Você avança contra o Troll!')
        print('Dano causado: {}'.format(jogador_atk))
        troll_vida -= jogador_atk
        print('Vida do Troll: {}'.format(troll_vida))

    elif jogador == 2:
        print('Você ergue sua guarda!')
        jogador_defTF = True

    elif jogador == 3:
        print('Você corre para longe do Troll!')
        print('Você escapou para a floresta.')
        print('Combate encerrado.')
        break

    if maquina == 1:
        if jogador_defTF == False:
            print('⚔ Troll da Floresta ataca!')
            print('Dano recebido: {}'.format(troll_atk))
            jogador_vida -= troll_atk
            print('Sua vida: {}'.format(jogador_vida))
        if jogador_defTF == True:
            print('⚔ Troll da Floresta ataca!')
            print('Dano recebido reduzido: {}'.format(troll_atk - 10))
            jogador_vida -= (troll_atk - 10)
            print('Sua vida: {}'.format(jogador_vida))
            jogador_defTF = False

    elif maquina == 2:
        if jogador == 1:
            print('O troll bloqueou seu ataque.')
            print('Dano recebido reduzido: {}'.format(jogador_atk - 10))
            troll_vida -= (jogador_atk - 10)
            print('Vida do troll: {}'.format(troll_vida))

    elif maquina == 3:
        print('O Troll recua assustado!')
        print('Ele desaparece entre as árvores da floresta.')
        print('Combate encerrado.')
        break

    if troll_vida <= 0:
        print('⚔ Você desfere um golpe poderoso!')
        print('Dano causado: {}'.format(jogador_atk))
        print('Vida do Troll: {}'.format(troll_vida))
        print('O Troll da Floresta foi derrotado!')
        print('Vitória!')
        break