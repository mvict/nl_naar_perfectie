# import webbrowser

import bs4
import os
import requests
import sys

SOURCES = "vocabularies"
VOCABULARY_FILE = os.path.join(SOURCES, "searched_words.txt")
SEARCHED_WORDS = {}

class Word:
    def __init__(self, word):
        self.word = word
        self._read_searched_words()

    def __str__(self):
        return f"{self.word}"

    def _read_searched_words(self):
        with open(VOCABULARY_FILE) as already_searched:
            searched_words = already_searched.readlines()
         
            for line in searched_words:
                if line != '':
                    word, article = line.split('\t')
                    SEARCHED_WORDS[word] = article.strip('\n')
            print(SEARCHED_WORDS)
                
    def gender(self):
        if self.word in SEARCHED_WORDS.keys():
            return SEARCHED_WORDS[self.word]
        else:
            return self._look_in_www() 

    def _look_in_www(self):
        # look up gender in www.welklidwoord.nl
        try:
            url_gender_guesser = 'https://www.welklidwoord.nl/' + self.word
            gender_guesser_page = requests.get(url_gender_guesser)
            
            if gender_guesser_page.status_code == requests.codes.ok:
                beautifulsoup_of_genderpage = bs4.BeautifulSoup(gender_guesser_page.text, features='lxml')
                gender = beautifulsoup_of_genderpage.select('h2 span')[0].getText()

                if len(gender) > 3:
                    return ""
                else:
                    SEARCHED_WORDS[self.word] = gender.lower()
                    return gender.lower()             
        except(IndexError):
            print("Please, write a complete word")


def keep_search_history():
    with open(VOCABULARY_FILE,'w') as output_file:
        for word in SEARCHED_WORDS.keys(): 
            output_file.write(word + '\t' + SEARCHED_WORDS[word] + '\n')
    
while(True):
    try:
        word = input("Which word do you want to look up? >>> ")
        w = Word(word)
        g = w.gender()
        if g:
            print(f"The grammatical gender of {word} is '{g}'")
        else:
            print(f"I don't know which article belongs to {w}")
    except(KeyboardInterrupt):
        # all searched words are written in once
        keep_search_history()
        print("\n####### You have stopped the program, bye, bye") 
        sys.exit()
