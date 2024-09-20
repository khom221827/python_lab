from module.my_module1 import *

def main():
    text = "Як життя друзі?"
    src = "uk"
    dest = ""
    set = "all"


    detection_result = LangDetect(text, set=set)
    print(Fore.RED, detection_result)

    translated_text = TransLate(text, src=src, dest=dest)
    print(Fore.GREEN, translated_text)

    code = CodeLang(src)
    print(Fore.BLUE,code)

    # out = input("Виберіть метод виведення мови 'screen'  або 'txt' "  )
    out = "txt"
    LanguageList(out, text)

    print(Style.RESET_ALL)

if __name__ == '__main__':
    main()