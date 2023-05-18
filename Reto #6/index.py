
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

    player_1_points = sum(1 for jugada in lista_jugadas if posibilidades.get(jugada) == jugada[0])
    player_2_points = len(lista_jugadas) - player_1_points
            
    return ("Player 1" if player_1_points > player_2_points else "Player 2") if player_1_points != player_2_points else "Tie"


print(piedra_papel_tijeras([("🗿","✂️"), ("✂️","🗿")]))
        