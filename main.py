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
    
    new_sentences = []
    
    for sentence in sentences:
        words = sentence.split()
        if words:
            first_word = words[0]  # первое слово в предложении
            new_sentence = []
            
            for word in words:
                new_sentence.append(word)
                # Если слово является местоимением, вставляем первое слово
                if word.lower() in pronouns:
                    new_sentence.append(first_word)
            
            new_sentences.append(' '.join(new_sentence))
    
    # Объединяем обработанные предложения в текст
    new_text = ' '.join(new_sentences)
    
    # Записываем новый текст в выходной файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_text)

# Указываем имена входного и выходного файла
input_filename = 'input.txt'
output_filename = 'output.txt'

# Вызываем функцию обработки текста
process_text(input_filename, output_filename)
