import argparse
import codecs
import random

# this program uses a vocabulary table to extract a word an its gender and
# makes a question to the user, keeps tracks of the amount of failures and 
# successes
# thought: there are many ways to solve this, I make a dct with an entry per word
# would it be better to make a dicctionary like {'het': [w1, w3], 'de': [w2]}?

# UI strings
# TODO: use only one ui language
ARTICLE = "Wat is het lidwoord van {} >>> "
CORRECT_ANSWERS = "You answered {} questions correctly."
NUMBER_OF_QUESTIONS = "You got {} questions."
RESULT = "This is your result: "
WRONG_ANSWERS = "You answered {} questions wrongly."
WRONGNUMBEROFFIELDS = "Number of fields in line number {} is not as expected"


def chose_vocabulary(file_name):
    with codecs.open(file_name, 'r', 'UTF-8') as input_file:
        # all_vocabulary contains all records in file
        all_vocabulary = [row.rstrip('\r\n').split('\t') for row in input_file]
        return {row[1]: row[9] for row in all_vocabulary if row[2] == 'noun'}


def summarize_performance(right, wrong, number_of_tries):
    print("\n############################################\n")
    print(RESULT)
    print(NUMBER_OF_QUESTIONS.format(str(number_of_tries)))
    print(CORRECT_ANSWERS.format(right))
    print(WRONG_ANSWERS.format(wrong))
    print("\n############################################\n")


def make_questions(times, questions):
    success_counter = 0
    failures_counter = 0

    while(times):
        word = random.choice([key for key in questions.keys()])
        answer = input(ARTICLE.format(word))
        article = questions[word]

        if answer == article:
            success_counter += 1
            print(f'Precies, een {article}-woord')
        else:
            failures_counter += 1
            print(f'Nee hoor, het juiste lidwoord is \'{article}\'.')
        times -= 1
    return success_counter, failures_counter

def main():
    parser = argparse.ArgumentParser(description='Learn de/het words')
    parser.add_argument('-n', dest='number_of_words',
                        help='number of words to practice', type=int)
    parser.add_argument('-l', dest='list', help='Name of the list to practice')

    args = parser.parse_args()

    vocabulary_file_name = args.list
    number_of_tries = args.number_of_words

    # check number of fields
    # check_number_of_fields(vocabulary_file_name)
    #
    chosen_vocabulary = chose_vocabulary(vocabulary_file_name)
    print(f"available words are: {len(chosen_vocabulary)}")
    right, wrong = make_questions(number_of_tries, chosen_vocabulary)
    summarize_performance(right, wrong, number_of_tries)



if __name__ == "__main__":
    main()