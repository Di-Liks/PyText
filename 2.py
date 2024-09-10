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

# Ввод текста и ключа с клавиатуры
text = input("Введите текст для шифрования: ")
key = input("Введите ключ для шифрования: ")

encrypted_text = encrypt_permutation_cipher(text, key)
print("Зашифрованный текст:", encrypted_text)
