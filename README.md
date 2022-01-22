# nl_naar_perfectie
I'll create my own exercises to practice Dutch here

# welk lidwoord.py
Looks up words requested by the user in woordvanvandaag.nl and keeps track of the words searched in searched_words.txt

# guess_the_gender.py (use to be called scraping_words.py) 
I wrote this program to practice some scraping using the suggested libraries in the book ...
bs4.BeautifulSoup sees a text with html code as code and not as text:

    beautifulsoup_of_nouns = bs4.BeautifulSoup(page_with_nouns.text, features="lxml")
	Beautiful 

guess_the_geder.py ask the user to guess the gender of a word, firstly it looks for a random noun in www.woordvanvandaag.nl, and then looks up it's gender in www.welklidwoord.nl. It then builds a question and gives feedback.

# learn_these_words.py
Builds questions up depending on the grammatical features of words.
* for verbs it wil ask the pastparticle and the preposition
* for nouns the plural and the gender

It ask the user the number of questions to be asked
It aks the user the file from which to get the words
It uses as default "de_fundatie_text.txt"
It checks the completeness of the text files to see if there are missing fields

verplichte argumenten -l en -n

# learn_these_genders.py
Ask the genders of words stored in a given text file. It's a variation of learn_these_words.py
Gives a summary of the result: number of words asked, number of wrong and right words















# kijk ook naar deze bronnen van informatie
https://www.welklidwoord.be/<woord>

1. esto
24. aquello
3. lo de más allá

* esto
* aquello
* lo de más allá

28/10/2021

https://www.woordvanvandaag.nl/category/zelfstandig%20naamwoord

</div>

		<ul class="wordlist">

		<li>
		– <i><a href="./word/2836">aalbes</a></i> <span class="date">(22-7-2017)</span>
		</li>

inside the word

	<p>(de) <span class="theword">aal·bes</span> (<a class="hidden" href="./category/zelfstandig%20naamwoord">zelfstandig naamwoord</a>)<br>
		= redcurrant</p>
