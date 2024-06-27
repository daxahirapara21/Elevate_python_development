import argparse
from googletrans import Translator, LANGUAGES

def translate(text, source_language, dest_language):
    translator = Translator()

    try:
        translated = translator.translate(text, src=source_language, dest=dest_language)
        print(f'{LANGUAGES[source_language]}: {text}')
        print(f'{LANGUAGES[dest_language]}: {translated.text}')
    except ValueError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Language Translator')
    parser.add_argument('text', type=str, help='Text to translate')
    parser.add_argument('source_lang', type=str, help='Source language code (e.g., en)')
    parser.add_argument('dest_lang', type=str, help='Destination language code (e.g., fr)')
    
    args = parser.parse_args()
    
    if args.source_lang not in LANGUAGES or args.dest_lang not in LANGUAGES:
        print("Invalid language code. Supported language codes:")
        for code, language in LANGUAGES.items():
            print(f"{code}: {language}")
        return
    
    translate(args.text, args.source_lang, args.dest_lang)

if __name__ == '__main__':
    main()
