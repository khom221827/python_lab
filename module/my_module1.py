from colorama import Fore,Style
from googletrans import Translator, LANGUAGES
from tabulate import tabulate

translator = Translator()

def CodeLang(lang: str) -> str:
    language_code = lang
    language_name = LANGUAGES.get(language_code)
    return(f"Назва мови для коду '{language_code}': {language_name}")

def LangDetect(text : str, set : str) -> str:
    try:
        detected_lang = translator.detect(text).lang
        if set == "lang":   
            return detected_lang
        elif set == "confidence":
            detection_result = translator.detect(text)
            confidence = detection_result.confidence
            if confidence is not None:
                return str(confidence)
        elif set == "all":
            confidence = translator.detect(text).confidence
            return f"Language: {detected_lang}, Confidence: {confidence}"
        else:
            return "Invalid 'set' parameter. Use 'lang', 'confidence', or 'all'."
    except Exception as e:
        return str(e)


def TransLate(text : str, src : str, dest : str) -> str:
    try:
        src_lang = LANGUAGES.get(src, src)
        dest_lang = LANGUAGES.get(dest, dest)
        translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated_text.text

    except Exception as e:
        return str(e)


def LanguageList(out: str, text: str = None, limit=11) -> str:
    languages = LANGUAGES
    filename = "LANGUAGES.txt"
    
    if out == 'screen':
        table_data = []
        count = 1
        for code, language in languages.items():
            if text:
                translator = Translator()
                translation = translator.translate(text, dest=code)
                table_data.append([count, language, code, translation.text])
            else:
                table_data.append([count, language, code])
            count += 1
            if count >= limit:
                break
        
        table_headers = ["N", "Language", "ISO-639 code", "Text"]
        formatted_table = tabulate(table_data, headers=table_headers, tablefmt="grid")
        print(formatted_table)
        print(Fore.GREEN + "Ok")

    elif out == 'txt' and filename:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str("Language  ISO-639 code Text gt\n----------------------------------\n"))
            count = 1
            for code, language in languages.items():
                if text:
                    translator = Translator()
                    translation = translator.translate(text, dest=code)
                    file.write(f"{language:<5} {code} {translation.text}\n")
                else:
                    file.write(f"{code} {language:<12}\n")
                count += 1
                if count >= limit:
                    print("Готово загляньте у ваш файл '-'")
                    break
