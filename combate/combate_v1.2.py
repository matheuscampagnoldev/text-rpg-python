print('════════ COMBATE ════════')
print('⚠ Um Troll da Floresta apareceu!')
print('═════════════════════════')

import random

jogador_vida = 100
jogador_atk = 25
jogador_def = 20

troll_vida = 100
troll_atk = 20
troll_def = 15


while True:

    print('════════ COMBATE ════════')
    print(f'❤️ Jogador: {jogador_vida}')
    print(f'👹 Troll: {troll_vida}')
    print('════════════════════════')

    jogador = int(input('[ 1 ] Atacar \n[ 2 ] Defender \n[ 3 ] Fugir \n>>>> '))
    maquina = random.randint(1,4)

    if jogador == 1:
        print('⚔ Você avança contra o Troll!')
        print('💥 Dano causado: {}'.format(jogador_atk))
        troll_vida -= jogador_atk
        print('👹 Vida do Troll: {}'.format(troll_vida))
    if jogador == 2:
        troll_atk - 10
    if jogador == 3:
        print('🏃 Você corre para longe do Troll!')
        print('🌲 Você escapou para a floresta.')
        print('Combate encerrado.')
        break

    if maquina == 1:
        print('⚔ Troll da Floresta ataca!')
        print('💥 Dano recebido: {}'.format(troll_atk))
        jogador_vida -= troll_atk
        print('👹 Sua vida: {}'.format(jogador_vida))
    if maquina == 2:
        jogador_atk - 10
    if maquina == 3:
        print('👹 O Troll recua assustado!')
        print('🌲 Ele desaparece entre as árvores da floresta.')
        print('Combate encerrado.')
        break

    if troll_vida <= 0:
        print('⚔ Você desfere um golpe poderoso!')
        print('💥 Dano causado: {}'.format(jogador_atk))
        print('👹 Vida do Troll: {}'.format(troll_vida))
        print('☠ O Troll da Floresta foi derrotado!')
        print('🏆 Vitória!')
        break