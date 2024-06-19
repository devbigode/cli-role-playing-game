# Jogo de Batalha RPG

Bem-vindo ao repositório do Jogo de Batalha RPG! Este é um jogo de batalha simples onde um jogador enfrenta uma série de NPCs (Bots) em combates de turnos. O jogador pode escolher entre dois estilos de luta e usar habilidades especiais durante a batalha.

## Como Jogar

#### 1. Escolha do Jogador:

O jogo começa solicitando o nome do jogador.

Em seguida, o jogador escolhe entre dois estilos de luta: Conservador (dano menor, vida maior) ou Agressivo (dano maior, vida menor).

#### 2. Batalhas:

O jogador enfrenta 5 NPCs em sequência.

Cada batalha é dividida em rounds, onde o jogador e o NPC atacam alternadamente.

O jogador pode usar habilidades especiais durante a batalha, que têm diferentes efeitos dependendo do estilo de luta escolhido.

#### 3. Progresso:

Após cada batalha, o jogador ganha experiência (XP) e pode subir de nível, melhorando suas habilidades e atributos.

O objetivo é vencer todos os 5 NPCs.

## Requisitos

Python 3

Nenhuma biblioteca externa é necessária além da biblioteca padrão do Python.

## Como Executar

1. Clone o repositório para sua máquina local:

  git clone https://github.com/seu-usuario/cli-role-playing-game.git

2. Navegue até o diretório do projeto:

  cd cli-role-playing-game

3. Execute o jogo:

  python main.py

## Código Fonte

### Construção do Jogador

    from random import randint

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

### Criação dos NPCs

    def create_npcs(level):
        npc = {"nome": f"Bot {level}", "nível": level, "dano": 9 * level, "hp": 54 * level, "hp_max": 54 * level, "xp": 20 * level}
        return npc

    def make_npcs(n):
        npcs = []
        for i in range(1, n + 1):
            npc = create_npcs(i)
            npcs.append(npc)
        return npcs

### Mecânica de Batalha

    def attack_npc():
        npc['hp'] -= player['dano']

    def attack_player():
        player['hp'] -= npc['dano']

    def special():
        special = input("\nPressione [S] para usar a habilidade especial. Ou Enter para continuar...")
        spec = special.lower()
        if spec == "s":
            dice = randint(0, 3)
            if dice == 0:
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

### Informações e Progresso

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

### Inicialização do Jogo

    player = build_player()
    npcs = make_npcs(5)

    for x in range(5):
        npc = npcs[x]
        init(player, npc)

### Contribuição

Sinta-se à vontade para fazer fork deste repositório e enviar pull requests. Feedbacks e sugestões são bem-vindos!