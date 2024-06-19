from random import randint

# Definindo o Jogador: Coletando nome e estilo de jogo.
def build_player():

    name = input("Quem jogará hoje? ")

    print("\nLogo abaixo, decida entre o combatente conservador ou o combatente agressivo.\n")

    while True:
        melee_weapon = int(input("[1] para Conservador ou [2] para Agressivo: "))

        if melee_weapon == 1:
            damage = 22
            life = 115
            break
        elif melee_weapon == 2:
            damage = 34
            life = 90
            break
        else:
            print("Informe um valor válido.\n")       
    
    player = {"nome": name, "nível": 1, "estilo_luta": melee_weapon, "habilidade": 1, "dano": damage, "xp": 0, "xp_max": 50, "hp": life, "hp_max": life}
        
    return player

# Criando NPC's
def create_npcs(level):
    npc = {"nome": f"Bot {level}", "nível": level, "dano": 9 * level, "hp": 54 * level, "hp_max": 54 * level, "xp": 20 * level}
    return npc

def make_npcs(n):
    npcs = []
    for i in range(1, n + 1):   
        npc = create_npcs(i)
        npcs.append(npc)
    return npcs
        
# Jogador atacando NPC e vice-versa.
def attack_npc():  
    npc['hp'] -= player['dano']

def attack_player():       
    player['hp'] -= npc['dano']

# Habilidades especiais de cada estilo de luta.
def special():
    special = input("\nPressione [S] para usar a habilidade especial. Ou Enter para continuar...")
    spec = special.lower()

    if spec == "s":
        dice = randint(0, 3) # 25% de chance de fracasso.
        if dice == 0: # Perdeu
            player['habilidade'] -= 1
            print(f"\n{player['nome']} falhou em usar a habilidade especial. n° de habilidades restante: {player['habilidade']}")
        else:
            player['habilidade'] -= 1
            if player['estilo_luta'] == 1:
                shield()
            else:     
                sword() 

def sword():
    npc['hp'] -= player['dano']
    
def shield():
    player['hp'] += npc['dano'] * 1.75
    
# Informações pré e pós batalhas e atualizações por rounds.
def info_before_battle():
    print(f"\n{player['nome']} - Vida atual: {player['hp']} | Dano: {player['dano']} | n° de habilidade(s): {player['habilidade']}")
    print(f"{npc['nome']} - Vida: {npc['hp']} | Dano: {npc['dano']}")

def info_round():
    print(f"\nSua vida: {player['hp']}/{player['hp_max']}")
    print(f"Vida atual de {npc['nome']}: {npc['hp']}/{npc['hp_max']}")

def info_player():
    print(f"\n+ {npc['xp']} pontos de experiência. Nível: {player['nível']} - {player['xp']}/{player['xp_max']}")

def level_up():
    if player['xp'] >= player['xp_max']:
        player['nível'] += 1
        player['xp_max'] *= 2
        player['habilidade'] += 1

def xp_get():
    player['xp'] += npc['xp']

def upgrade():
    player['dano'] += 2 * npc['nível']
    player['hp_max'] += 5 * npc['nível']

def winner():
    if player["hp"] > 0:
        print(f"\n{player['nome']} saiu como vencedor!")
        xp_get()
        level_up()
        upgrade()
        info_player()
    else:
        print(f"\n{player['nome']} perdeu!")

def reset():
    npc['hp'] = npc['hp_max']
    player['hp'] = player['hp_max']

def division():
    print(f"\n----------\n{npc['nível']}ª batalha\n----------")

def init(player, npc):
    r = []
    division()
    info_before_battle()
    while npc['hp'] > 0 and player['hp'] > 0:
        r.append(1)
        print(f"\n*Round: {sum(r)}")
        attack_npc()

        if player['habilidade'] > 0:
           special()
        
        if npc['hp'] > 0: 
            attack_player()
                        
        info_round()
   
    winner()
    reset()

# Criando jogador principal e bots, respectivamente.
player = build_player()
npcs = make_npcs(5)

for x in range(5):
    npc = npcs[x]
    init(player, npc)