import math

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect_square(num: int) -> bool:
    sqrt = int(math.sqrt(num))
    return sqrt * sqrt == num

def is_fibonacci(num: int) -> bool:
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def checker(num: int) -> str:
    is_even = num % 2 == 0
    is_prime_bool = is_prime(num)
    is_fibonacci_bool = is_fibonacci(num)
    
    string = f"{num} "
    string += "es primo, " if is_prime_bool else "no es primo, "
    string += "fibonacci, y " if is_fibonacci_bool else "no es fibonacci, y "
    string += "es par" if is_even else "es impar"

    return string

print(checker(2))
print(checker(7))
print(checker(3))
