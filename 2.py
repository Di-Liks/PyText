def encrypt_permutation_cipher(text, key):
    # Убираем пробелы из ключа и проверяем уникальность символов
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))

    # Определяем длину ключа
    key_length = len(key)

    # Делаем текст кратным длине ключа, заполняя пробелами
    padding_length = (key_length - len(text) % key_length) % key_length
    text += ' ' * padding_length

    # Разбиваем текст на блоки по длине ключа
    blocks = [text[i:i+key_length] for i in range(0, len(text), key_length)]

    # Создаем список для зашифрованного текста
    encrypted_text = []

    # Определяем порядок перестановки символов в соответствии с ключом
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Переставляем символы в каждом блоке
    for block in blocks:
        encrypted_block = ''.join([block[i] for i in key_order])
        encrypted_text.append(encrypted_block)

    return ''.join(encrypted_text)

def decrypt_permutation_cipher(encrypted_text, key):
    # Убираем пробелы из ключа и проверяем уникальность символов
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))

    # Определяем длину ключа
    key_length = len(key)

    # Разбиваем зашифрованный текст на блоки по длине ключа
    blocks = [encrypted_text[i:i+key_length] for i in range(0, len(encrypted_text), key_length)]

    # Создаем список для расшифрованного текста
    decrypted_text = []

    # Определяем порядок перестановки символов в соответствии с ключом
    key_order = sorted(range(len(key)), key=lambda k: key[k])

    # Определяем обратный порядок для расшифровки
    reverse_key_order = [0] * len(key_order)
    for i, pos in enumerate(key_order):
        reverse_key_order[pos] = i

    # Восстанавливаем символы в каждом блоке
    for block in blocks:
        decrypted_block = ''.join([block[i] for i in reverse_key_order])
        decrypted_text.append(decrypted_block)

    return ''.join(decrypted_text).rstrip()

# Ввод данных с клавиатуры
text = input("Введите текст для шифрования или оставьте пустым для расшифровки из файла: ")
key = input("Введите ключ: ")
choice = input("Выберите действие (1 - шифрование, 2 - расшифровка): ")

if choice == "1":
    encrypted_text = encrypt_permutation_cipher(text, key)
    print("Зашифрованный текст:", encrypted_text)

    # Запись зашифрованного текста в файл
    with open("encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)
    print("Зашифрованный текст записан в файл 'encrypted_text.txt'")

elif choice == "2":
    # Чтение зашифрованного текста из файла
    try:
        with open("encrypted_text.txt", "r", encoding="utf-8") as file:
            encrypted_text = file.read()
        print("Текст для расшифровки из файла:", encrypted_text)
        
        decrypted_text = decrypt_permutation_cipher(encrypted_text, key)
        print("Расшифрованный текст:", decrypted_text)
    except FileNotFoundError:
        print("Файл 'encrypted_text.txt' не найден.")
else:
    print("Некорректный выбор действия.")
