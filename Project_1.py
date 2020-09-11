'''
author =
'''
from unicodedata import numeric

TEXT = ['''
'Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',
        '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
        '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
        ]

credentials = {
    'me': "ni",
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}


def main():
    print("GREETINGS! WELCOME TO THE".center(50))
    print("|T|E|X|T| |A|N|A|L|Y|Z|E|R|".center(50))
    linebreak()
    credentials_check()
    linebreak()
    print(f"WE HAVE {len(TEXT)} TEXTS FOR ANALYSIS.".center(50))
    linebreak()

    recursion = True
    while recursion:
        text_number = text_selection()
        if text_number > len(TEXT):
            print(f'Selected text is unavailable, please select text number 1 - {len(TEXT)}.')
            continue
        selected_text = TEXT[text_number - 1]
        text_printing(selected_text)
        clean_txt = text_preparation(selected_text)
        print(f'''TEXT {text_number} CONTAINS:
                  WORDS  |  {text_statistics(clean_txt)[0]}
        TITLECASE WORDS  |  {text_statistics(clean_txt)[1]}
        UPPERCASE WORDS  |  {text_statistics(clean_txt)[2]}
        LOWERCASE WORDS  |  {text_statistics(clean_txt)[3]}
        NUMERIC STRINGS  |  {text_statistics(clean_txt)[4]}'''
              )
        linebreak()
        print(f"WORD LENGTH FREQUENCIES:")
        bar_chart(clean_txt)
        linebreak()
        print(f"SUM OF ALL THE NUMBERS IN SELECTED TEXT IS:", numeric_sum(clean_txt))
        linebreak()

        recursion_check = input('Do you wish to select another text? [Y/N]').lower()
        if recursion_check == 'y':
            recursion = True
        else:
            print(f"GOODBYE!".center(50))
            recursion = False


def linebreak():
    print('=' * 50)


def credentials_check():
    checking = True
    while checking:
        user_name = input('Please enter username:').lower()
        password = input('Please enter password:')
        if credentials.get(user_name) != password:
            print('USERNAME OR PASSWORD IS INCORRECT! PLEASE TRY AGAIN.')
            continue
        else:
            checking = False
            print(f"WELCOME {user_name.upper()}!".center(50))


def text_selection():
    while True:
        try:
            selected_text = int(input('Select text number you wish to analyze:'))
        except ValueError:
            print('Invalid input! Please insert valid text number.')
            continue
        else:
            return selected_text


def text_printing(selected_text):
    linebreak()
    print("YOUR SELECTED TEXT IS:".center(50))
    linebreak()
    print(selected_text)
    linebreak()


def text_preparation(selected_text):
    txt_split = selected_text.split()
    clean_txt = []
    for word in txt_split:
        clean_word = word.strip(".,")
        clean_txt.append(clean_word)
    return clean_txt


def text_statistics(cleaned_text):
    word_count = len(cleaned_text)
    title_count = 0
    upper_count = 0
    lower_count = 0
    numeric_count = 0
    for word in cleaned_text:
        if word.istitle():
            title_count += 1
        elif word.isupper():
            upper_count += 1
        elif word.islower():
            lower_count += 1
        elif word.isnumeric():
            numeric_count += 1
    return word_count, title_count, upper_count, lower_count, numeric_count


def bar_chart(clean_txt):
    clean_txt_copy = clean_txt.copy()
    word_pop_dictionary = {}
    while clean_txt_copy:
        wordpop = clean_txt_copy.pop()
        if len(wordpop) not in word_pop_dictionary:
            word_pop_dictionary[len(wordpop)] = 0
        word_pop_dictionary[len(wordpop)] = word_pop_dictionary[len(wordpop)] + 1

    for i in sorted(word_pop_dictionary):
        print(i, '*' * word_pop_dictionary[i], word_pop_dictionary[i])


def numeric_sum(txt_split):
    numeric_calc = []
    for word in txt_split:
        if word.isnumeric():
            numeric_calc.append(int(word))
    return sum(numeric_calc)


main()
