# import webbrowser
import bs4
import requests
import sys


def look_up(word):
    # look up gender in www.welklidwoord.nl
    try:
        url_gender_guesser = 'https://www.welklidwoord.nl/' + word
        gender_guesser_page = requests.get(url_gender_guesser)
        
        if gender_guesser_page.status_code == requests.codes.ok:
            beautifulsoup_of_genderpage = bs4.BeautifulSoup(gender_guesser_page.text, features='lxml')
            gender = beautifulsoup_of_genderpage.select('h1 span')[0].getText()

            if len(gender) > 3:
                print(f"Sorry, ik weet het lidwoord van {word} niet")
            # print gender to screen
            else: 
                print(f"Het lidwoord van {word} is \'{gender.lower()}\'")
    
    except(IndexError):
        print("Please, write a complete word")

# TODO: convert program to a class to be able to store 
# the words with the gender

def keep_track_of_search(word):
    sw = open("saught_words.txt",'a')
    sw.write(word + "\n")
    sw.close()

while(True):
    try:
        word = input("Welk woord zoek je? >>> ")
        look_up(word)
        keep_track_of_search(word)
    except(KeyboardInterrupt):
        print("\n####### You have stopped the program, bye, bye") 
        sys.exit()
