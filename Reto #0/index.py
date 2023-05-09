#!/usr/bin/pyton3

def fizzbuzz(num: int) -> None:
    """
    Recibe un argumento de tipo int, que es el numero hasta el cual se ejecutara ek FIZZBUZZ
    Los numeros se imprimiran iniciando en el numero 1, por lo tanto el numero como argumento
    debe ser un numero mayor a 1
    """
    for i in range(1, num + 1):
        result = f'{"fizz" if i % 3 == 0 else ""}{"buzz" if i % 5 == 0 else ""}'
        print(result or i)
        

fizzbuzz(100)