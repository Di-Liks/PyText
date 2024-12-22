import random
import math

S_star = 22176 * 10**7

alphabet = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!\"#$%&'"
    "\u0410-\u042F\u0430-\u044F"
)
A = len(alphabet)

L = math.ceil(math.log(S_star, A))

def generate_password(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))

password = generate_password(L, alphabet)

# Вывод результатов
print(f"Мощность алфавита: {A}")
print(f"Минимальная длина пароля: {L}")
print(f"Сгенерированный пароль: {password}")
