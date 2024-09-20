from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs
from colorama import Fore,Style
from tabulate import tabulate


translator = GoogleTranslator()

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=src, target=dest)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return str(e)
    
def LangDetect(text: str, set: str) -> str:
    try:
        lang_info = detect_langs(text)
        if set == "lang":
            return lang_info[0].lang
        elif set == "confidence":
            return lang_info[0].prob
        elif set == "all":
            return f"Language: {lang_info[0].lang}, Confidence: {lang_info[0].prob}"
        else:
            return "Invalid 'set' parameter. Use 'lang', 'confidence', or 'all'."
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    try:
        detected_lang = detect(lang)
        supported_languages = translator.get_supported_languages(as_dict=True)

        if detected_lang in supported_languages:
            return supported_languages[detected_lang]
        elif lang in supported_languages.values():
            for code, language in supported_languages.items():
                if language == lang:
                    return f"Код мови для назви '{lang}': {code}"
        else:
            return "Invalid language input. Please provide a valid language name or code."
    except Exception as e:
        return str(e)

def LanguageList(out: str, text: str , limit=11):
    language_codes = translator.get_supported_languages(as_dict=True)
    
    
    if out == 'screen':
        table_data = []
        count = 1
        for  language,code in language_codes.items():
            try:
                translated = GoogleTranslator(source='auto', target=code).translate(text)
                table_data.append([count, code, language, translated])
                count += 1
                if count >= limit:
                    break
            except Exception as e:
                print(f"Error detecting language: {str(e)}")
        
        table_headers = ["N", "ISO-639 code", "Language", "Translated Text"]
        formatted_table = tabulate(table_data, headers=table_headers, tablefmt="grid")
        print(formatted_table)
        print(Fore.GREEN + "Ok")

    elif out == 'txt':
        filename = "LANGUAGES.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str("Language  ISO-639 code Translated Text tr \n----------------------------------\n"))
            count = 1
            for  language,code in language_codes.items():
                try:
                    translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                    file.write(f"{language:<5} {code} {translated_text}\n")
                    count += 1
                    if count >= limit:
                        print("Готово загляньте у ваш файл '-'")
                        break
                except Exception as e:
                    print(f"Error detecting language: {str(e)}")