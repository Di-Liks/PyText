import re

def process_text(input_file, output_file):
    # Считываем текст из входного файла
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Разбиваем текст на предложения с помощью регулярного выражения
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Список русских местоимений
    pronouns = {'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они',
                'меня', 'тебя', 'его', 'её', 'нас', 'вас', 'их',
                'мне', 'тебе', 'ему', 'ей', 'нам', 'вам', 'им',
                'мной', 'тобой', 'им', 'ей', 'нами', 'вами', 'ими',
                'мой', 'твой', 'его', 'её', 'наш', 'ваш', 'их'}
    
    # Словарь для подсчета местоимений
    pronoun_count = {pronoun: 0 for pronoun in pronouns}
    
    # Переменная с текстом и подсчет количества слов
    additional_text = "Я люблю ходить на пары"
    additional_words = additional_text.split()
    additional_word_count = len(additional_words)
    
    new_sentences = []
    pronoun_counter = 0  # Счетчик всех местоимений
    
    for sentence in sentences:
        words = sentence.split()
        if words:
            first_word = words[0]  # первое слово в предложении
            new_sentence = []
            
            for word in words:
                new_sentence.append(word)
                # Если слово является местоимением, вставляем первое слово и считаем его
                lower_word = word.lower()
                if lower_word in pronouns:
                    pronoun_count[lower_word] += 1
                    pronoun_counter += 1
                    new_sentence.append(first_word)
                    # Если количество местоимений равно количеству слов в переменной, вставляем слово из переменной
                    if pronoun_counter % additional_word_count == 0:
                        index = (pronoun_counter // additional_word_count) % additional_word_count
                        new_sentence.append(additional_words[index - 1])  # Извлекаем слово по индексу
                    
            new_sentences.append(' '.join(new_sentence))
    
    # Объединяем обработанные предложения в текст
    new_text = ' '.join(new_sentences)
    
    # Записываем новый текст в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_text)
    
    # Подсчитываем общее количество местоимений
    total_pronouns = sum(pronoun_count.values())
    
    # Выводим количество местоимений в начальном тексте
    print("Подсчет местоимений в тексте:")
    for pronoun, count in pronoun_count.items():
        if count > 0:
            print(f"{pronoun}: {count}")
    
    # Выводим общее количество местоимений
    print(f"\nОбщее количество местоимений: {total_pronouns}")
    
    # Выводим количество слов в переменной
    print(f"Количество слов в переменной: {additional_word_count}")

# Указываем имена входного и выходного файла
input_filename = 'input.txt'
output_filename = 'output.txt'

# Вызываем функцию обработки текста
process_text(input_filename, output_filename)
