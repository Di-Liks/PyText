import string

# Определяем русский алфавит, включая букву "ё"
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Функция для создания измененного алфавита на основе ключевого слова
def create_caesar_alphabet(keyword):
    keyword = keyword.lower()  # Приводим ключевое слово к нижнему регистру
    keyword_unique = ''.join(sorted(set(keyword), key=keyword.index))  # Убираем дубликаты символов

    # Создаем новый алфавит: ключевое слово + оставшиеся буквы русского алфавита
    new_alphabet = keyword_unique + ''.join([ch for ch in russian_alphabet if ch not in keyword_unique])
    
    return new_alphabet

# Функция шифрования шифром Цезаря с ключевым словом для русского алфавита
def encrypt_caesar_cipher(text, keyword):
    new_alphabet = create_caesar_alphabet(keyword)  # Измененный алфавит
    alphabet = russian_alphabet  # Оригинальный русский алфавит

    encrypted_text = []
    for char in text:
        if char.lower() in alphabet:  # Проверяем, если символ в алфавите
            is_upper = char.isupper()  # Проверяем регистр
            idx = alphabet.index(char.lower())  # Находим индекс символа в оригинальном алфавите
            encrypted_char = new_alphabet[idx].upper() if is_upper else new_alphabet[idx]  # Замена
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Символы вне алфавита (пробелы, знаки) не меняются

    return ''.join(encrypted_text)

# Функция расшифровки шифра Цезаря с ключевым словом для русского алфавита
def decrypt_caesar_cipher(text, keyword):
    new_alphabet = create_caesar_alphabet(keyword)  # Измененный алфавит
    alphabet = russian_alphabet  # Оригинальный алфавит

    decrypted_text = []
    for char in text:
        if char.lower() in new_alphabet:  # Проверяем, если символ в измененном алфавите
            is_upper = char.isupper()  # Проверяем регистр
            idx = new_alphabet.index(char.lower())  # Находим индекс символа в измененном алфавите
            decrypted_char = alphabet[idx].upper() if is_upper else alphabet[idx]  # Замена
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # Символы вне алфавита (пробелы, знаки) не меняются

    return ''.join(decrypted_text)

# Функция для записи текста в файл
def write_to_file(text, filename="Output.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Функция для чтения текста из файла
def read_from_file(filename="Output.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Основная программа
def main():
    print("Выберите тип шифрования:")
    print("1. Шифр Цезаря с ключевым словом (русский алфавит)")
    print("2. Шифр перестановки")

    cipher_type = input("Ваш выбор (1 или 2): ")  # Выбор типа шифрования
    key = input("Введите ключевое слово (на русском): ")  # Ввод ключа

    match cipher_type:
        case "1":
            # Шифр Цезаря с ключевым словом
            choice = input("Выберите действие (1 - шифрование, 2 - расшифровка из файла): ")
            if choice == "1":
                text = input("Введите текст для шифрования: ")  # Ввод текста
                encrypted_text = encrypt_caesar_cipher(text, key)
                write_to_file(encrypted_text)
                print("Зашифрованный текст записан в файл Output.txt")
            elif choice == "2":
                encrypted_text = read_from_file()
                decrypted_text = decrypt_caesar_cipher(encrypted_text, key)
                print("Расшифрованный текст:", decrypted_text)
            else:
                print("Некорректный выбор действия.")
        
        case "2":
            # Шифр перестановки
            choice = input("Выберите действие (1 - шифрование, 2 - расшифровка из файла): ")
            if choice == "1":
                text = input("Введите текст для шифрования: ")  # Ввод текста
                encrypted_text = encrypt_permutation_cipher(text, key)
                write_to_file(encrypted_text)
                print("Зашифрованный текст записан в файл Output.txt")
            elif choice == "2":
                encrypted_text = read_from_file()
                decrypted_text = decrypt_permutation_cipher(encrypted_text, key)
                print("Расшифрованный текст:", decrypted_text)
            else:
                print("Некорректный выбор действия.")
        
        case _:
            print("Некорректный выбор типа шифрования.")

if __name__ == "__main__":
    main()  # Запуск программы
