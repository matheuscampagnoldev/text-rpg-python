print('════════ COMBATE ════════')
print('⚠ Um Troll da Floresta apareceu!')
print('═════════════════════════')

import random
import os
import time

vida_jogador = 100
atk_jogador = 25
def_jogador = 20
jogador_defTF = False

vida_troll = 100
atk_troll = 20
def_troll = 15
troll_defTF = False

while True:
    print('════════ COMBATE ════════')
    print(f'Jogador: {vida_jogador}')
    print(f'Troll: {vida_troll}')
    print('════════════════════════')

    jogador = int(input('[ 1 ] Atacar \n[ 2 ] Defender \n[ 3 ] Fugir \n>>>> '))
    if jogador not in [1, 2, 3]:
        print('Opção inválida. Tente novamente.')
        continue
    troll = random.randint(1, 3)


    if jogador == 1:
        print('⚔ Você ergue sua espada e avança contra o Troll!')
    elif jogador == 2:
        print('Você ergue sua guarda!')
    elif jogador == 3:
        print('Você corre para longe do Troll!')
        print('Você escapou para a floresta.')
        print('Combate encerrado.')
        break

    if troll == 1:
            print('⚔ Troll da Floresta ataca!')    
    elif troll == 2:
        print('O Troll da Floresta bloqueou seu ataque.')
    elif troll == 3:
        print('O Troll da Floresta fugiu do combate! Você venceu!')
        break

    if jogador == 1 and troll == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Dano causado: {}'.format(atk_jogador))
        vida_troll -= atk_jogador
        print('Vida do Troll: {}'.format(vida_troll))
        print('Dano recebido: {}'.format(atk_troll))
        vida_jogador -= atk_troll
        print('Sua vida: {}'.format(vida_jogador))
        time.sleep(2)
    
    elif jogador == 1 and troll == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Dano causado: {}'.format(atk_jogador - def_troll))
        vida_troll -= (atk_jogador - def_troll)
        print('Vida do Troll: {}'.format(vida_troll))
        time.sleep(2)

    elif jogador == 2 and troll == 1:
        print('Dano recebido reduzido: {}'.format(atk_troll - def_jogador))
        vida_jogador -= (atk_troll - def_jogador)
        print('Sua vida: {}'.format(vida_jogador))
        time.sleep(2)

    elif jogador == 2 and troll == 2:
        print('O Troll da Floresta bloqueou seu ataque.')
        print('Você bloqueou o ataque do Troll da Floresta.')
        time.sleep(2)

    elif jogador == 1 and troll == 3:
        print('Dano causado: {}'.format(atk_jogador))
        vida_troll -= atk_jogador
        print('Vida do Troll: {}'.format(vida_troll))
        print('O Troll da Floresta fugiu do combate! Você venceu!')
        time.sleep(2)
        break

    elif vida_jogador <= 0:
        print('Você foi derrotado pelo Troll da Floresta!')
        break
    elif vida_troll <= 0:
        print('Você derrotou o Troll da Floresta!')
        break
    
    os.system('cls' if os.name == 'nt' else 'clear')