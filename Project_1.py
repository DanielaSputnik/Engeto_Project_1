'''
author =
'''

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
    print_greetings()
    run_credentials_check()
    print_text_options(TEXT)
    analysis_ongoing = True
    while analysis_ongoing:
        analyzed_txt_number = user_txt_selection()
        if analyzed_txt_number > len(TEXT):
            print_txt_unavailable(TEXT)
            continue
        analyzed_txt = TEXT[analyzed_txt_number - 1]
        print_out_text(analyzed_txt)
        clean_txt = txt_preparation(analyzed_txt)
        print_txt_statistics(analyzed_txt_number, clean_txt)
        print_bar_chart(clean_txt)
        print_numeric_sum(clean_txt)

        if select_diff_text() != 'y':
            analysis_ongoing = False
            print_goodbye()


def linebreak() -> str:
    print('=' * 50)


def print_greetings() -> str:
    print("GREETINGS! WELCOME TO THE".center(50))
    print("|T|E|X|T| |A|N|A|L|Y|Z|E|R|".center(50))
    linebreak()


def run_credentials_check() -> None:
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


def print_text_options(texts: list) -> str:
    linebreak()
    print(f"WE HAVE {len(texts)} TEXTS FOR ANALYSIS.".center(50))
    linebreak()


def user_txt_selection() -> int:
    while True:
        try:
            selected_text = int(input('Select text number you wish to analyze:'))
        except ValueError:
            print('Invalid input! Please insert valid text number.')
            continue
        else:
            return selected_text


def print_out_text(selected_text: str) -> str:
    linebreak()
    print("YOUR SELECTED TEXT IS:".center(50))
    linebreak()
    print(selected_text)
    linebreak()


def print_txt_unavailable(avail_texts: list) -> str:
    print(f'Selected text is unavailable, please select text number 1 - {len(avail_texts)}.')


def txt_preparation(selected_text: str) -> list:
    txt_split = selected_text.split()
    word_list = []
    for word in txt_split:
        clean_word = word.strip(".,")
        word_list.append(clean_word)
    return word_list


def text_statistics(word_list: list) -> tuple:
    word_count = len(word_list)
    title_count = 0
    upper_count = 0
    lower_count = 0
    numeric_count = 0
    for word in word_list:
        if word.istitle():
            title_count += 1
        elif word.isupper():
            upper_count += 1
        elif word.islower():
            lower_count += 1
        elif word.isnumeric():
            numeric_count += 1
    return word_count, title_count, upper_count, lower_count, numeric_count


def print_txt_statistics(txt_no: int, word_list: list) -> str:
    print(f'''TEXT {txt_no} CONTAINS:
              WORDS  |  {text_statistics(word_list)[0]}
    TITLECASE WORDS  |  {text_statistics(word_list)[1]}
    UPPERCASE WORDS  |  {text_statistics(word_list)[2]}
    LOWERCASE WORDS  |  {text_statistics(word_list)[3]}
    NUMERIC STRINGS  |  {text_statistics(word_list)[4]}'''
          )


def bar_chart(word_list: list) -> str:
    word_list_copy = word_list.copy()
    word_dictionary = {}
    while word_list_copy:
        wordpop = word_list_copy.pop()
        if len(wordpop) not in word_dictionary:
            word_dictionary[len(wordpop)] = 0
        word_dictionary[len(wordpop)] = word_dictionary[len(wordpop)] + 1

    for i in sorted(word_dictionary):
        print(i, '*' * word_dictionary[i], word_dictionary[i])


def print_bar_chart(word_list: list) -> str:
    linebreak()
    print(f"WORD LENGTH FREQUENCIES:")
    bar_chart(word_list)


def numeric_sum(word_list: list) -> int:
    numeric_calc = []
    for word in word_list:
        if word.isnumeric():
            numeric_calc.append(int(word))
    return sum(numeric_calc)


def print_numeric_sum(word_list: list) -> str:
    linebreak()
    print(f"SUM OF ALL THE NUMBERS IN SELECTED TEXT IS:", numeric_sum(word_list))
    linebreak()


def select_diff_text() -> bool:
    check = input('Do you wish to select another text? [Y/N]').lower()
    return check


def print_goodbye() -> str:
    linebreak()
    print(f"GOODBYE!".center(50))
    linebreak()


main()
