#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pandas as pd
# import nltk
import argparse
import codecs
import random

# two global variables for now
global_failures_counter = 0
global_success_counter = 0

# complete_vocabulary = [0 "id", 1 "string", 2 "pos", 3 "meaning", 4 "english", 5 "opposite", 6 "regular", 7"reflexive",
#                                 8"trenbaar", 9"gender", 10"preposition", 11 "vervoeging", 12 plural_form]

class Question:
    def __init__(self, record):
        self._word = record[1]
        self._meaning = record[3]
        self._vragen = [["wat betekent {} >>> ".format(record[1]),record[3]],
                        ["Hoe zeg je '{}' in Nederlands >>> ".format(record[3]),record[1]]]

        if record[2] == 'verb':
            self._is_regular = record[6]
            self._preposition = record[10]
            self._declination = record[11]
            self.__verb_question()

        if record[2] == 'noun':
            self._plural = record[12]
            self._article = record[9]
            self.__noun_question()

    def __verb_question(self):
        # todo match boolean and not string
        if self._is_regular == 'FALSE':
            question1 = "Wat is de verleden tijd en vooltooid deelwoord van {} >>> ".format(self._word)
            answer1 = self._declination
            self._vragen.append([question1, answer1])

        if self._preposition != 'n/a':
            question2 = "Welk voorzetsel gebruik je met {} >>> ".format(self._word)
            answer2 = self._preposition
            self._vragen.append([question2, answer2])

    def __noun_question(self):
        question1 = "Wat is de meervoud form van {} {} >>> ".format(self._article,self._word)
        answer1 = self._plural
        self._vragen.append([question1, answer1])

        question2 = "Wat is het lidwoord van {} >>> ".format(self._word)
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


def check_number_of_fields(vocabulary_file):
        with codecs.open(vocabulary_file, 'r','UTF-8') as input_file:
            line_number = 0
            for row in input_file:
                line_list = row.rstrip('\r\n').split('\t')
                line_number += 1
                try:
                    assert(len(line_list) == 13)
                except AssertionError:
                    print ("Number of fields in line number {} is not as expected".format(line_number))
        return True


def chose_vocabulary(file_name, category):
    with codecs.open(file_name, 'r', 'UTF-8') as input_file:
        # complete vocabulary contains all records in file
        complete_vocabulary = [row.rstrip('\r\n').split('\t') for row in input_file]
        # if no category is given as argument
        if category is None:
            return complete_vocabulary
        else:
            return [row for row in complete_vocabulary if row[2] == category]


def summarize_performance(number_of_tries):
    print("\n############################################\n")
    print("This is your result: ")
    print("You got {} questions.".format(str(number_of_tries)))
    print("You answered {} questions correctly.".format(str(global_success_counter)))
    print("You answered {} questions wrongly.".format(str(global_failures_counter)))
    print("\n############################################\n")

# todo move check number of fields to test file
# todo change strings to ask question to constants, no magic questions.

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', dest='number_of_words', help='number of words to practice', type=int)
    parser.add_argument('-c', dest='category', help='Grammar category or part of speech')
    # parser.add_argument('-t', dest='type', help='Type of exercise')
    parser.add_argument('-l', dest='list', help='Name of the list to practice')

    args = parser.parse_args()

    vocabulary_file_name = args.list
    number_of_tries = args.number_of_words
    category = args.category

    # check number of fields
    check_number_of_fields(vocabulary_file_name)
    chosen_vocabulary = chose_vocabulary(vocabulary_file_name,category)
    build_exercise(number_of_tries, chosen_vocabulary)
    summarize_performance(number_of_tries)

if __name__ == "__main__":
    main()