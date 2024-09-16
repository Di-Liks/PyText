import string

# Шифр Цезаря с ключевым словом
def create_caesar_alphabet(keyword):
    """
    Создает измененный алфавит на основе ключевого слова:
    - Убираются повторяющиеся символы в ключевом слове.
    - Ключевое слово помещается в начало алфавита, затем добавляются оставшиеся символы алфавита.
    """
    keyword_unique = ''.join(sorted(set(keyword), key=lambda x: keyword.index(x)))  # Убираем дубликаты в ключе

    # Стандартный алфавит
    alphabet = string.ascii_lowercase

    # Создаем новый алфавит: ключевое слово + оставшиеся буквы алфавита
    new_alphabet = keyword_unique + ''.join([ch for ch in alphabet if ch not in keyword_unique])

    return new_alphabet

def encrypt_caesar_cipher(text, keyword):
    """
    Шифрует текст, используя шифр Цезаря с ключевым словом:
    - Создается измененный алфавит на основе ключевого слова.
    - Каждый символ исходного текста заменяется соответствующим символом нового алфавита.
    """
    new_alphabet = create_caesar_alphabet(keyword)
    alphabet = string.ascii_lowercase

    encrypted_text = []
    for char in text:
        if char.lower() in alphabet:  # Проверяем, что символ входит в алфавит
            is_upper = char.isupper()  # Сохраняем регистр символа
            idx = alphabet.index(char.lower())  # Ищем индекс символа в стандартном алфавите
            encrypted_char = new_alphabet[idx].upper() if is_upper else new_alphabet[idx]  # Заменяем на символ из нового алфавита
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Если символ не в алфавите (например, пробелы), оставляем как есть

    return ''.join(encrypted_text)

def decrypt_caesar_cipher(text, keyword):
    """
    Расшифровывает текст, зашифрованный шифром Цезаря с ключевым словом:
    - На основе ключевого слова восстанавливается измененный алфавит.
    - Каждый символ зашифрованного текста заменяется на символ из стандартного алфавита.
    """
    new_alphabet = create_caesar_alphabet(keyword)
    alphabet = string.ascii_lowercase

    decrypted_text = []
    for char in text:
        if char.lower() in new_alphabet:
            is_upper = char.isupper()  # Сохраняем регистр символа
            idx = new_alphabet.index(char.lower())  # Ищем индекс символа в измененном алфавите
            decrypted_char = alphabet[idx].upper() if is_upper else alphabet[idx]  # Заменяем на символ из стандартного алфавита
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Если символ не в алфавите, оставляем как есть

    return ''.join(decrypted_text)

# Шифр перестановки
def encrypt_permutation_cipher(text, key):
    """
    Шифрование методом перестановки:
    - Текст разбивается на блоки по длине ключа.
    - Символы каждого блока переставляются в порядке, заданном ключом.
    """
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Убираем дубликаты символов в ключе

    key_length = len(key)
    padding_length = (key_length - len(text) % key_length) % key_length  # Добавляем пробелы, чтобы текст был кратен длине ключа
    text += ' ' * padding_length

    # Разбиваем текст на блоки длиной ключа
    blocks = [text[i:i+key_length] for i in range(0, len(text), key_length)]

    encrypted_text = []
    key_order = sorted(range(len(key)), key=lambda k: key[k])  # Определяем порядок перестановки символов

    # Переставляем символы в каждом блоке
    for block in blocks:
        encrypted_block = ''.join([block[i] for i in key_order])
        encrypted_text.append(encrypted_block)

    return ''.join(encrypted_text)

def decrypt_permutation_cipher(encrypted_text, key):
    """
    Расшифровка текста, зашифрованного методом перестановки:
    - Восстанавливается порядок символов в каждом блоке на основе ключа.
    """
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Убираем дубликаты в ключе

    key_length = len(key)
    blocks = [encrypted_text[i:i+key_length] for i in range(0, len(encrypted_text), key_length)]

    decrypted_text = []
    key_order = sorted(range(len(key)), key=lambda k: key[k])  # Определяем порядок перестановки символов

    reverse_key_order = [0] * len(key_order)  # Создаем список для обратного порядка перестановки
    for i, pos in enumerate(key_order):
        reverse_key_order[pos] = i

    # Восстанавливаем символы в каждом блоке
    for block in blocks:
        decrypted_block = ''.join([block[i] for i in reverse_key_order])
        decrypted_text.append(decrypted_block)

    return ''.join(decrypted_text).rstrip()

# Основная программа
def main():
    text = input("Введите текст для шифрования или расшифровки: ")  # Ввод исходного текста
    key = input("Введите ключ или ключевое слово: ")  # Ввод ключа для шифрования

    print("Выберите тип шифрования:")
    print("1. Шифр Цезаря с ключевым словом")
    print("2. Шифр перестановки")

    cipher_type = input("Ваш выбор (1 или 2): ")  # Выбор типа шифрования

    if cipher_type == "1":
        # Шифр Цезаря с ключом
        choice = input("Выберите действие (1 - шифрование, 2 - расшифровка): ")
        if choice == "1":
            encrypted_text = encrypt_caesar_cipher(text, key)  # Шифрование
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            decrypted_text = decrypt_caesar_cipher(text, key)  # Расшифровка
            print("Расшифрованный текст:", decrypted_text)
        else:
            print("Некорректный выбор действия.")
    
    elif cipher_type == "2":
        # Шифр перестановки
        choice = input("Выберите действие (1 - шифрование, 2 - расшифровка): ")
        if choice == "1":
            encrypted_text = encrypt_permutation_cipher(text, key)  # Шифрование
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            decrypted_text = decrypt_permutation_cipher(text, key)  # Расшифровка
            print("Расшифрованный текст:", decrypted_text)
        else:
            print("Некорректный выбор действия.")
    else:
        print("Некорректный выбор типа шифрования.")

if __name__ == "__main__":
    main()  # Запуск программы
