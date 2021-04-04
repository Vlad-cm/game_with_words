import random

word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
             'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА',
             'СКОВОРОДА',
             'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ',
             'МАК',
             'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА',
             'БАНАН',
             'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН',
             'ТЕЛЕФОН',
             'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР',
             'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК',
             'ТЮБИК',
             'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ',
             'ПИЦЦА',
             'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ',
             'ДИСК']


def get_word():
    return random.choice(word_list)


def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def play(word):
    word_completion = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    while True:
        word_input = input('Введите букву или слово: ').upper()
        if not word_input.isalpha():
            print('Вы ошиблись, попробуйте ещё')
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print('Уже было')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'Не верно, осталось попыток {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'Вы не смогли угадать слово: {word}')
                    break
                continue

        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print('Угадали букву')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'Не верно, осталось попыток {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'Вы не смогли угадать слово: {word}')
            break


def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


play(get_word().upper())