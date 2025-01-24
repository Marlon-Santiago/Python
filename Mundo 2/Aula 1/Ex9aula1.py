from random import randint
import time

print('Escolha uma opção')


print(f'Escolher [1] para PEDRA')
print(f'Escolher [2] para TESOURA')
print(f'Escolher [3] para PAPEL')

jogador = int(input('Escola entre pedra papael e tesoura: '))

maquina = randint(1,3)

print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO')

if jogador == 1 and maquina == 2:
    print(f'O jogador jogou {jogador} Pedra e a Maquina escolheu {maquina} Tesoura o vencedor foi o jogador')

elif jogador == 2 and maquina == 3:
    print(f'O jogador jogou {jogador} Tesoura e a Maquina escolheu {maquina} Papel o vencedor foi o jogador')

elif jogador == 3 and maquina == 1:
    print(f'O jogador jogou {jogador} Papel e a Maquina escolheu {maquina} Pedra o vencedor foi o jogador')

elif maquina == 1 and jogador == 2:
    print(f'O jogador jogou {jogador} Tesoura e A Maquina escolheu {maquina} Pedra o vencedor foi a Maquina')

elif maquina == 2 and jogador == 3:
    print(f'O jogador jogou {jogador} Papel e A Maquina escolheu {maquina} Tesoura o vencedor foi a maquina')

elif maquina == 3 and jogador == 1:
    print(f'O jogador jogou {jogador} Pedra e A Maquina escolheu {maquina} Papel o vencedor foi o jogador')

elif maquina == 1 and jogador == 1 or maquina == 2 and jogador == 2 or jogador == 3 and maquina == 3:
    print(f'O jogador jogou {jogador} e A Maquina escolheu {maquina} o jogo deu empate')

else:
    jogador == 4 
    print('Essa opção nao esxiste escolha uma opção existente')