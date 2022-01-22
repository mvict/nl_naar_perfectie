# import webbrowser
import requests
import bs4
import random



# # webbrowser.open('https://www.woordvanvandaag.nl/category/zelfstandig%20naamwoord' )
# page = requests.get('https://www.woordvanvandaag.nl/word/2836')
# if page.status_code == requests.codes.ok:
#     print(len(page.text))
#     #print(page.text[:250])
#     noStarchSoup = bs4.BeautifulSoup(page.text, features="lxml")
#     print(noStarchSoup.select('p span[class="theword"]'))

# page_with_nouns.text will contain the whole html of the page given as argument in a list
page_with_nouns = requests.get('https://www.woordvanvandaag.nl/category/zelfstandig%20naamwoord')
if page_with_nouns.status_code == requests.codes.ok:
    # BeautifulSoup converts the text to lxml    
    beautifulsoup_of_nouns = bs4.BeautifulSoup(page_with_nouns.text, features="lxml")

    # select all <a> elements tha apppear after a <i> tag, for example:
    # <i><a href="./word/2836">aalbes</a></i> <span class="date">(22-7-2017)</span>
    nouns = beautifulsoup_of_nouns.select('i a')

    # select at random one element from the list to build the question
    random_index = random.randint(0,len(nouns))
    chosen_word = nouns[random_index].getText()
    
    # look up gender in www.welklidwoord.nl
    url_gender_guesser = 'https://www.welklidwoord.nl/' + chosen_word
    gender_guesser_page = requests.get(url_gender_guesser)
    if gender_guesser_page.status_code == requests.codes.ok:
        beautifulsoup_of_genderpage = bs4.BeautifulSoup(gender_guesser_page.text, features='lxml')
        gender = beautifulsoup_of_genderpage.select('h1 span')[0].getText()

        if len(gender) > 3:
            print(f"Sorry, ik weet het lidwoord van {chosen_word} niet")

        # test user's knowledge
        else: 
            guessed_by_user = input(f"Wat is the gender of {chosen_word}? >> ")

            if gender.lower() == guessed_by_user.lower():
                print("YEAH!")
            else:
                print("Nope")

    # tag = nouns.div
    

    # zoek het lidwoord van een woord
    # zoek in je bestanden
    # staat het woord niet in?
    #   zoek online
    #
    # is een het-woord ? 
        # bewaar het in het.txt
    # is het een de-woord?
        # bewaar het in de.txt
    # else: bewaar het in ongedefineerd.txt

    
    # zoek online
    # is een het-woord ? 
        # bewaar het in het.txt (niet bewaren als het al in zit)
    # is het een de-woord?
        # bewaar het in de.txt
    # else: bewaar het in ongedefineerd.txt (niet bewaren als het al in zit)
