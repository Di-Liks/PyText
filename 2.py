import string

# Шифр Цезаря с ключевым словом
def create_caesar_alphabet(keyword):
    # Убираем повторяющиеся символы в ключевом слове
    keyword_unique = ''.join(sorted(set(keyword), key=lambda x: keyword.index(x)))

    # Создаем стандартный алфавит
    alphabet = string.ascii_lowercase

    # Формируем новый алфавит: сначала идут символы из ключевого слова, затем оставшиеся символы
    new_alphabet = keyword_unique + ''.join([ch for ch in alphabet if ch not in keyword_unique])

    return new_alphabet

def encrypt_caesar_cipher(text, keyword):
    new_alphabet = create_caesar_alphabet(keyword)
    alphabet = string.ascii_lowercase

    encrypted_text = []
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            idx = alphabet.index(char.lower())
            encrypted_char = new_alphabet[idx].upper() if is_upper else new_alphabet[idx]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Пропускаем символы, которых нет в алфавите (например, пробелы)

    return ''.join(encrypted_text)

def decrypt_caesar_cipher(text, keyword):
    new_alphabet = create_caesar_alphabet(keyword)
    alphabet = string.ascii_lowercase

    decrypted_text = []
    for char in text:
        if char.lower() in new_alphabet:
            is_upper = char.isupper()
            idx = new_alphabet.index(char.lower())
            decrypted_char = alphabet[idx].upper() if is_upper else alphabet[idx]
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Пропускаем символы, которых нет в алфавите

    return ''.join(decrypted_text)

# Шифр перестановки
def encrypt_permutation_cipher(text, key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))

    key_length = len(key)
    padding_length = (key_length - len(text) % key_length) % key_length
    text += ' ' * padding_length

    blocks = [text[i:i+key_length] for i in range(0, len(text), key_length)]

    encrypted_text = []
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    for block in blocks:
        encrypted_block = ''.join([block[i] for i in key_order])
        encrypted_text.append(encrypted_block)

    return ''.join(encrypted_text)

def decrypt_permutation_cipher(encrypted_text, key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))

    key_length = len(key)
    blocks = [encrypted_text[i:i+key_length] for i in range(0, len(encrypted_text), key_length)]

    decrypted_text = []
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    reverse_key_order = [0] * len(key_order)
    for i, pos in enumerate(key_order):
        reverse_key_order[pos] = i

    for block in blocks:
        decrypted_block = ''.join([block[i] for i in reverse_key_order])
        decrypted_text.append(decrypted_block)

    return ''.join(decrypted_text).rstrip()

# Основная программа
def main():
    text = input("Введите текст для шифрования или расшифровки: ")
    key = input("Введите ключ или ключевое слово: ")

    print("Выберите тип шифрования:")
    print("1. Шифр Цезаря с ключевым словом")
    print("2. Шифр перестановки")

    cipher_type = input("Ваш выбор (1 или 2): ")

    if cipher_type == "1":
        choice = input("Выберите действие (1 - шифрование, 2 - расшифровка): ")
        if choice == "1":
            encrypted_text = encrypt_caesar_cipher(text, key)
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            decrypted_text = decrypt_caesar_cipher(text, key)
            print("Расшифрованный текст:", decrypted_text)
        else:
            print("Некорректный выбор действия.")
    
    elif cipher_type == "2":
        choice = input("Выберите действие (1 - шифрование, 2 - расшифровка): ")
        if choice == "1":
            encrypted_text = encrypt_permutation_cipher(text, key)
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            decrypted_text = decrypt_permutation_cipher(text, key)
            print("Расшифрованный текст:", decrypted_text)
        else:
            print("Некорректный выбор действия.")
    else:
        print("Некорректный выбор типа шифрования.")

if __name__ == "__main__":
    main()
