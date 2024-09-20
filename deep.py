from module.my_module2 import *

def main():
    text = "Привіт як життя мої друзі?"
    src = "uk"
    dest = "en"
    set = "all"

    detection_result = LangDetect(text, set=set)
    print(detection_result)

    translated_text = TransLate(text, src=src, dest=dest)
    print(translated_text)

    code = CodeLang(src)
    print(code)

    # out = input("Виберіть метод виведення мови 'screen'  або 'txt' "  )
    out = "screen"
    LanguageList(out, text)
    print(Style.RESET_ALL)
    

if __name__ == '__main__':
    main()