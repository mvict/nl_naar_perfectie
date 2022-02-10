# nl_naar_perfectie
I'll create my own exercises to practice Dutch here

# welk lidwoord.py
Looks up words requested by the user in woordvanvandaag.nl and keeps track of the words searched in searched_words.txt

# guess_the_gender.py (use to be called scraping_words.py) 
I wrote this program to practice some scraping using the suggested libraries in the book Automate the borings stuff with Python.

bs4.BeautifulSoup sees a text with html code as code and not as text:

    beautifulsoup_of_nouns = bs4.BeautifulSoup(page_with_nouns.text, features="lxml")
	Beautiful 

guess_the_gender.py ask the user to guess the gender of a word. Firstly it chooses at random a noun from www.woordvanvandaag.nl, and then looks up its gender in www.welklidwoord.nl. It then builds a question and gives feedback.

# learn_these_words.py
Builds questions up depending on the grammatical features of words.
* for verbs it wil ask the pastparticle and the preposition
* for nouns the plural and the gender

It ask the user the number of questions to be asked
It aks the user the file from which to get the words
It uses as default "de_fundatie_text.txt"
It checks the completeness of the text files to see if there are missing fields

mandatory arguments -l en -n
It is a bit complicated the way it is now. Using a db would have been a better option. 

### TODO 
1. move check number of fields to test file
1. in class question some properties depend on the category of word, it's not a nice starting point. would it not be better to have a class word with subclasses for noun and verb, and a class question, with subclasses for verb question and noun question.  

# write_this_vocabulary.py
a script to make lists of words to practise with learn_these_words.py

# learn_these_genders.py
Ask the genders of words stored in a given text file. It's a variation of learn_these_words.py
Gives a summary of the result: number of words asked, number of wrong and right words


# kijk ook naar deze bronnen van informatie
https://www.welklidwoord.be/<woord>

28/10/2021
## List of nouns
https://www.woordvanvandaag.nl/category/zelfstandig%20naamwoord

	<ul class="wordlist">
	<li>
	<i><a href="./word/2836">aalbes</a></i> <span class="date">(22-7-2017)</span>
	</li>

## inside the word page
	<p>(de) <span class="theword">aal·bes</span> (<a class="hidden" href="./category/zelfstandig%20naamwoord">zelfstandig naamwoord</a>)<br>
		= redcurrant</p>
