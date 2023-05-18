
def piedra_papel_tijeras(lista_jugadas):
    posibilidades = {
        ("🗿", "📄"): "📄",  # Piedra vs. Papel -> Papel
        ("🗿", "✂️"): "🗿",  # Piedra vs. Tijera -> Piedra
        ("🗿", "🦎"): "🗿",  # Piedra vs. Lagarto -> Piedra
        ("🗿", "🖖"): "🖖",  # Piedra vs. Spock -> Spock
        ("📄", "✂️"): "✂️",  # Papel vs. Tijera -> Tijera
        ("📄", "🦎"): "📄",  # Papel vs. Lagarto -> Papel
        ("📄", "🖖"): "📄",  # Papel vs. Spock -> Papel
        ("✂️", "🦎"): "🦎",  # Tijera vs. Lagarto -> Lagarto
        ("✂️", "🖖"): "✂️",  # Tijera vs. Spock -> Tijera
        ("🦎", "🖖"): "🦎"   # Lagarto vs. Spock -> Lagarto
    }

    player_1_points = 0
    player_2_points = 0
    
    for i in lista_jugadas:
        try:
            result = posibilidades[i]
        except KeyError:
            result = posibilidades[i[::-1]]

        if result == i[0]:
            player_1_points += 1
        else:
            player_2_points += 1
            
    return ("Player 1" if player_1_points > player_2_points else "Player 2") if player_1_points != player_2_points else "Tie"


print(piedra_papel_tijeras([("🗿","✂️"), ("✂️","🗿")]))
        