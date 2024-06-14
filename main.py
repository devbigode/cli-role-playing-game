# %%
from random import randint

lista_npcs = []

jogador = {"nome": "Guilherme", 
           "nível": 1,
           "dano": 25,
           "xp": 0, 
           "xp_max": 50, 
           "hp": 100, 
           "hp_max": 100
           }

def criar_npcs(level):

    npc = {"nome": f"Bot {level}", 
           "nível": level, 
           "dano": 5 * level, 
           "hp": 50 * level,
           "hp_max": 50 * level,
           "xp": 7 * level
           }
    return npc
    
# def quantidade_npcs():
#     n = randint(1, 5)
#     return n

def gerar_npcs(n):

    # n = quantidade_npcs()
    
    for i in range(1, n + 1):
        
        npc = criar_npcs(i)
        lista_npcs.append(npc)

def atacar_npc():  
    npc['hp'] -= jogador['dano']

def atacar_jogador():       
    jogador['hp'] -= npc['dano']

def info_batalha():
    print(f"Vida atual de {jogador['nome']}: {jogador['hp']}/{jogador['hp_max']}")
    print(f"Vida atual de {npc['nome']}: {npc['hp']}/{npc['hp_max']} ")

def info_jogador():
    print(f"+ {npc['xp']} pontos de experiência.\nNível: {jogador['nível']} - {jogador['xp']}/{jogador['xp_max']}")
    print(f"\nNova vida: {jogador['hp_max']} | Novo dano: {jogador['dano']}")

def level_up():
    if jogador['xp'] >= jogador['xp_max']:
        jogador['nível'] += 1
        jogador['xp_max'] *= 2

def xp_obtido():
    jogador['xp'] += npc['xp']

def upgrade():
    jogador['dano'] += 2 * npc['nível']
    jogador['hp_max'] += 5 * npc['nível']     

def reset():
    npc['hp'] = npc['hp_max']
    jogador['hp'] = jogador['hp_max']

    print("\n_____\n")    

def winner():
    if jogador["hp"] > 0:
        print(f"\n{jogador['nome']} saiu como vencedor!")
        xp_obtido()
        level_up()
        upgrade()
        info_jogador()
    else:
        print(f"\n{jogador['nome']} perdeu!")


def init():
    r = []
    while npc['hp'] > 0 and jogador['hp'] > 0:
        r.append(1)
        print(f"\nRound: {sum(r)}")
        atacar_npc()
        atacar_jogador()
        info_batalha()
   
    winner()
    reset()

# def exibir_npcs():
#     for npc in lista_npcs:
#         print(
#             f"Nome: {npc['nome']} - Dano: {npc['dano']} - Vida: {npc['hp_max']}"
#         )

gerar_npcs(5)

for x in range(5):
    npc = lista_npcs[x]
    init()