import argparse
import codecs
import random
import os

# this program uses a vocabulary table to extract a word an its gender and
# makes a question to the user, keeps tracks of the amount of failures and 
# successes
# thought: there are many ways to solve this, I make a dct with an entry per word
# Other possible ways: {'het': [w1, w3], 'de': [w2]}?
# or even better het = [w1, w3, w4], de = [w2]

# UI strings
ARTICLE = "Wat is het lidwoord van {} >>> "
CORRECT_ANSWERS = "{} antwoorden waren correct"
NUMBER_OF_QUESTIONS = "Je hebt {} vragen geantwoord."
RESULT = "Dit is je resultaat "
RIGHT_GUESS = "Precies, een {}-woord"
WRONG_ANSWERS = "{} antwoorden waren fout"
WRONG_GUESS = 'Nee hoor, het juiste lidwoord is \'{}\'.'
WRONGNUMBEROFFIELDS = "Number of fields in line number {} is not as expected"

# name of the directory for vocabularies
SOURCES = "vocabularies"

def chose_vocabulary(file_name):
    file_name = os.path.join(SOURCES, file_name)
    print(f'file_name is: {file_name}')
    with codecs.open(file_name, 'r', 'UTF-8') as input_file:
        # all_vocabulary contains all records in file
        all_vocabulary = [row.rstrip('\r\n').split('\t') for row in input_file]
        # it returns a dictionary, index is the word, value is the gender
        return {row[1]: row[9] for row in all_vocabulary if row[2] == 'noun'}


def summarize_performance(right, wrong, number_of_tries):
    print("\n" + 45 * "#" + "\n")
    print(RESULT)
    print(NUMBER_OF_QUESTIONS.format(str(number_of_tries)))
    print(CORRECT_ANSWERS.format(right))
    print(WRONG_ANSWERS.format(wrong))
    print("\n" + 45 * "#" + "\n")


def make_questions(tries, nouns_dct):
    success_counter = 0
    failures_counter = 0

    while(tries):
        word = random.choice([key for key in nouns_dct.keys()])
        # ask user for article used with word
        answer = input(ARTICLE.format(word))
        article = nouns_dct[word]

        # give user feedback about answer
        if answer == article:
            success_counter += 1
            print(RIGHT_GUESS.format(article))
        else:
            failures_counter += 1
            print(WRONG_GUESS.format(article))

        tries -= 1
    return success_counter, failures_counter

def main():
    parser = argparse.ArgumentParser(description='Learn de/het words')
    parser.add_argument('-n', dest='number_of_words', default=10,
                        help='Number of words to practice', type=int)
    parser.add_argument('-l', dest='list', help='Name of the list to practice',
                        default='de_fundatie_text.txt')

    args = parser.parse_args()

    vocabulary_file_name = args.list
    number_of_tries = args.number_of_words

    chosen_vocabulary = chose_vocabulary(vocabulary_file_name)
    print(f"Beschikbare woorden: {len(chosen_vocabulary)}")
    right, wrong = make_questions(number_of_tries, chosen_vocabulary)
    summarize_performance(right, wrong, number_of_tries)


if __name__ == "__main__":
    main()