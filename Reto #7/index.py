def sombrero_seleccionador():
    posibles_respuestas = {"a": "Gryffindor", "b": "Hufflepuff", "c": "Ravenclaw", "d": "Slytherin"}

    preguntas = [
        "¿Qué valor consideras más importante? a) Valentía b) Lealtad c) Intelecto d) Astucia\n",
        "¿Cuál es tu mayor fortaleza? a) Coraje b) Empatía c) Creatividad d) Ambición\n",
        "¿Qué tipo de tarea prefieres? a) Una aventura emocionante b) Ayudar a los demás c) Resolver un acertijo complicado d) Alcanzar tus metas personales\n",
        "¿Cómo te describes a ti mismo/a? a) Audaz b) Amigable c) Curioso/a d) Determinado/a\n",
        "¿Cuál de estas mascotas te gustaría tener? a) León b) Perro c) Búho d) Serpiente\n"
    ]

    respuestas = [input(pregunta).lower() for pregunta in preguntas]
    if any(respuesta not in posibles_respuestas for respuesta in respuestas):
        raise ValueError("La respuesta debe ser A, B, C o D")

    valor_mas_repetido = max(respuestas, key=respuestas.count)
    casa_seleccionada = posibles_respuestas[valor_mas_repetido]

    return casa_seleccionada

print(sombrero_seleccionador())
