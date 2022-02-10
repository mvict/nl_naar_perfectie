#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pandas as pd
# import nltk
import argparse
import codecs
import os
import random

# name of the directory for vocabularies
SOURCES = "vocabularies"

DEBUG = False

# two global variables for now
global_failures_counter = 0
global_success_counter = 0

# complete_vocabulary = {0: "id", 1: "string", 2: "pos", 3: "meaning",
#                        4: "english", 5: "opposite", 6: "regular",
#                        7: "reflexivo, 8: "trenbaar", 9: "gender",
#                        10: "preposition", 11:  "vervoeging",
#                        12:  plural_form}

ARTICLE = "Wat is het lidwoord van {} >>> "
CORRECT_ANSWERS = "You answered {} questions correctly."
HOWDOYOUSAY = "Hoe zegt je {} in Nederlands? >>> "
MEANING = "Wat betekent {}? >>> "
NUMBER_OF_QUESTIONS = "You got {} questions."
PAST_PASTPARTICLE = "Wat is de verleden tijd en vooltooid deelwoord van {} >> "
PLURAL = "Wat is de meervoud form van {} {} >>> "
PREPOSITION = "Welk voorzetsel gebruik je met {} >>> "
RESULT = "This is your result: "
WRONG_ANSWERS = "You answered {} questions wrongly."
WRONGNUMBEROFFIELDS = "Number of fields in line number {} is not as expected"


class Question:
    def __init__(self, record):
        self._word = record[1]
        self._category = record[2]
        self._meaning = record[3]
        self._vragen = [[MEANING.format(self._word), self._meaning],
                        [HOWDOYOUSAY.format(self._meaning), self._word]]

        if self._category == 'verb':
            self._is_regular = record[6]
            self._preposition = record[10]
            self._declination = record[11]
            self._verb_question()

        if self._category == 'noun':
            self._plural = record[12]
            self._article = record[9]
            self._noun_question()

    def _verb_question(self):
        # todo match boolean and not string
        if self._is_regular == 'FALSE':
            question1 = PAST_PASTPARTICLE.format(self._word)
            answer1 = self._declination
            self._vragen.append([question1, answer1])

        if self._preposition != 'n/a':
            question2 = PREPOSITION.format(self._word)
            answer2 = self._preposition
            self._vragen.append([question2, answer2])

    def _noun_question(self):
        question1 = PLURAL.format(self._article, self._word)
        answer1 = self._plural
        self._vragen.append([question1, answer1])

        question2 = ARTICLE.format(self._word)
        answer2 = self._article
        self._vragen.append([question2, answer2])

    def question_answer(self):
        chosen_question = random.choice(self._vragen)
        # print (self._vragen)
        question = chosen_question[0]
        answer = chosen_question[1]
        return question, answer


def give_feedback_on_result(answer, user_answer):
    global global_failures_counter
    global global_success_counter

    if user_answer == answer:
        print("So far so good\n")
        global_success_counter += 1
    else:
        print("Not yet there, the answer is {}\n".format(answer))
        global_failures_counter += 1


def build_exercise(number_of_tries, vocabulary):
    while number_of_tries:
        this_record = random.choice(vocabulary)
        q = Question(this_record)
        question, answer = q.question_answer()
        user_answer = input(question)
        give_feedback_on_result(answer, user_answer)
        number_of_tries -= 1


# control function to check that the data file is correct
def check_number_of_fields(vocabulary_file):
    vocabulary_file = os.path.join(SOURCES, vocabulary_file)
    with codecs.open(vocabulary_file, 'r', 'UTF-8') as input_file:
        line_number = 0
        for row in input_file:
            line_list = row.rstrip('\r\n').split('\t')
            line_number += 1
            try:
                assert(len(line_list) == 13)
            except AssertionError:
                print (WRONGNUMBEROFFIELDS.format(line_number))
    return True


def chose_vocabulary(file_name, category):
    file_name = os.path.join(SOURCES, file_name)
    with codecs.open(file_name, 'r', 'UTF-8') as input_file:
        # all_vocabulary contains all records in file
        all_vocabulary = [row.rstrip('\r\n').split('\t') for row in input_file]
        # if no category is given as argument
        if category is None:
            return all_vocabulary
        else:
            return [row for row in all_vocabulary if row[2] == category]


def summarize_performance(number_of_tries):
    print("\n" + 45 * "#" + "\n")
    print(RESULT)
    print(NUMBER_OF_QUESTIONS.format(str(number_of_tries)))
    print(CORRECT_ANSWERS.format(str(global_success_counter)))
    print(WRONG_ANSWERS.format(str(global_failures_counter)))
    print("\n" + 45 * "#" + "\n")


def main():
    parser = argparse.ArgumentParser(description='Learn vocabulary lists')
    parser.add_argument('-n', dest='number_of_words',
                        help='number of words to practice', type=int)
    parser.add_argument('-c', dest='category', help='Grammar category')
    # parser.add_argument('-t', dest='type', help='Type of exercise')
    parser.add_argument('-l', dest='list', help='Name of the list to practice',
                        default='de_fundatie_text.txt')

    args = parser.parse_args()

    vocabulary_file_name = args.list
    number_of_tries = args.number_of_words
    category = args.category

    # check number of fields
    if DEBUG:
        check_number_of_fields(vocabulary_file_name)

    chosen_vocabulary = chose_vocabulary(vocabulary_file_name, category)
    build_exercise(number_of_tries, chosen_vocabulary)
    summarize_performance(number_of_tries)


if __name__ == "__main__":
    main()
