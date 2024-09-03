import re  # Импортируем модуль регулярных выражений для работы с текстом

def process_text(input_file, output_file):
    # Считываем текст из входного файла
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Разбиваем текст на предложения с помощью регулярного выражения
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Список русских местоимений для поиска в тексте
    pronouns = {'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они',
                'меня', 'тебя', 'его', 'её', 'нас', 'вас', 'их',
                'мне', 'тебе', 'ему', 'ей', 'нам', 'вам', 'им',
                'мной', 'тобой', 'им', 'ей', 'нами', 'вами', 'ими',
                'мой', 'твой', 'его', 'её', 'наш', 'ваш', 'их'}
    
    # Словарь для подсчета количества каждого местоимения
    pronoun_count = {pronoun: 0 for pronoun in pronouns}
    
    # Переменная с текстом, слова из которой будем вставлять
    additional_text = "Я люблю ходить на пары"
    additional_words = additional_text.split()  # Разбиваем строку на отдельные слова
    
    new_sentences = []  # Список для хранения новых предложений
    pronoun_counter = 0  # Счетчик всех встреченных местоимений
    
    # Обрабатываем каждое предложение по отдельности
    for sentence in sentences:
        words = sentence.split()  # Разбиваем предложение на слова
        if words:
            new_sentence = []  # Список для хранения слов нового предложения
            
            for word in words:
                new_sentence.append(word)  # Добавляем текущее слово в новое предложение
                # Проверяем, является ли слово местоимением
                lower_word = word.lower()  # Преобразуем слово к нижнему регистру для сравнения
                if lower_word in pronouns:
                    pronoun_count[lower_word] += 1  # Увеличиваем счетчик для этого местоимения
                    pronoun_counter += 1  # Увеличиваем общий счетчик местоимений
                    # Вставляем слова из additional_text только для первых пяти местоимений
                    if pronoun_counter <= len(additional_words):
                        # Вставляем слово из additional_words по индексу, соответствующему количеству местоимений
                        new_sentence.append(additional_words[pronoun_counter - 1])
            
            # Добавляем обработанное предложение в список новых предложений
            new_sentences.append(' '.join(new_sentence))
    
    # Объединяем обработанные предложения в один текст
    new_text = ' '.join(new_sentences)
    
    # Записываем новый текст в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_text)
    
    # Подсчитываем общее количество всех местоимений
    total_pronouns = sum(pronoun_count.values())
    
    # Выводим количество каждого местоимения, которое встречалось в тексте
    print("Подсчет местоимений в тексте:")
    for pronoun, count in pronoun_count.items():
        if count > 0:  # Выводим только те местоимения, которые были найдены
            print(f"{pronoun}: {count}")
    
    # Выводим общее количество местоимений
    print(f"\nОбщее количество местоимений: {total_pronouns}")
    
    # Выводим количество слов в переменной additional_text
    print(f"Количество слов в переменной: {len(additional_words)}")

# Указываем имена входного и выходного файла
input_filename = 'input.txt'  # Имя файла с исходным текстом
output_filename = 'output.txt'  # Имя файла для сохранения измененного текста

# Вызываем функцию обработки текста
process_text(input_filename, output_filename)
