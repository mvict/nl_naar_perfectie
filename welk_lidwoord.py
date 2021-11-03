# import webbrowser
import bs4
import requests
import sys

SEARCHED_WORDS = []

class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return f"{self.word}"

    def gender(self):
        # look up gender in www.welklidwoord.nl
        try:
            url_gender_guesser = 'https://www.welklidwoord.nl/' + self.word
            gender_guesser_page = requests.get(url_gender_guesser)
            
            if gender_guesser_page.status_code == requests.codes.ok:
                beautifulsoup_of_genderpage = bs4.BeautifulSoup(gender_guesser_page.text, features='lxml')
                gender = beautifulsoup_of_genderpage.select('h1 span')[0].getText()

                if len(gender) > 3:
                    return ""
                else:
                    return gender.lower()             
        except(IndexError):
            print("Please, write a complete word")

def keep_track_of_search(gender, word):
    SEARCHED_WORDS.append((gender, word))    

def keep_search_history():
    with open("searched_words.txt",'a') as output_file:
        for gender, word  in SEARCHED_WORDS: 
            output_file.write(gender + "\t" + word + "\n")
    
while(True):
    try:
        word = input("Welk woord zoek je? >>> ")
        w = Word(word)
        g = w.gender()
        if g:
            print(f"Het lidwoord van {word} is \'{w.gender()}\'")
            # adds tuple to SEARCHED_WORDS
            keep_track_of_search(g, word)
        else:
            print(f"Ik weet niet welk lidwoord wordt gebruikt met {w}")
    except(KeyboardInterrupt):
        # all searched words are written in once
        keep_search_history()
        print("\n####### You have stopped the program, bye, bye") 
        sys.exit()
