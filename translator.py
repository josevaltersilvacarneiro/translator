import argparse

from translate import Translator

def push(data : str, filename : str = 'translation.txt') -> None:

    with open(filename, 'a', encoding='UTF8') as fil:
        fil.write(data + '\n');

def store_translation(translation : str) -> int:

    push(translation);

    return 0;

def main(message : str, from_lang : str = 'pt-br') -> int:

    translator = Translator(from_lang=from_lang, to_lang='en');

    translation = translator.translate(message);
    
    return store_translation(translation);

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                description='This program translates sentences said by person'
            );

    parser.add_argument(
                '--text',
                type=str,
                help='It receives the setences that you want to translate',
                required=True
            );

    parser.add_argument(
                '--from-lang',
                type=str,
                help='It receives the the language that the original text was written',
                default='pt-br'
            );

    args = parser.parse_args();
     
    message   : str = args.text;
    from_lang : str = args.from_lang

    exit(main(message, from_lang));

