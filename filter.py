import os
from deep_translator import GoogleTranslator
from pathlib import Path

def analyze_text(text):
    words = text.split()
    sentences = text.split('.')
    return len(words), len(sentences)

config_file = 'config.txt'

if os.path.exists(config_file):
    with open(config_file, 'r', encoding='utf-8') as config:
        text_file_name = config.readline().strip()
        target_language = config.readline().strip()
        output_destination = config.readline().strip()
        max_chars = int(config.readline().strip())
        max_words = int(config.readline().strip())
        max_sentences = int(config.readline().strip())

    if os.path.exists(text_file_name):
        with open(text_file_name, 'r', encoding='utf-8') as text_file:
            text = text_file.read()

        char_count = len(text)
        word_count, sentence_count = analyze_text(text)

        print(f"Назва файлу: {text_file_name}")
        print(f"Розмір файлу: {os.path.getsize(text_file_name)} байт")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")
        print(f"Мова тексту: {target_language}")

        translator = GoogleTranslator(source='auto', target=target_language)
        translated_text = translator.translate(text)

        if char_count > max_chars or word_count > max_words or sentence_count > max_sentences:
            print("Досягнуті обмеження кількості символів, слів або речень.")
        else:
            if output_destination == 'txt':
                output_file_name = f"{Path(text_file_name).stem}_{target_language}.txt"
                with open(output_file_name, 'w', encoding='utf-8') as output_file:
                    output_file.write(translated_text)
                print("Ok")
            elif output_destination == 'screen':
                print(f"Мова перекладу: {target_language}")
                print(translated_text)
            else:
                print("Невідоме призначення для виведення результатів.")
    else:
        print(f"Файл '{text_file_name}' не знайдено.")
else:
    print(f"Файл конфігурації '{config_file}' не знайдено.")
