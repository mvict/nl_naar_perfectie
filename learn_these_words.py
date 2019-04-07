#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pandas as pd
# import nltk
import argparse
import codecs
import random


# complete_vocabulary = [0 "id", 1 "string", 2 "pos", 3 "meaning", 4 "english", 5 "opposite", 6 "regular", 7"reflexive",
#                                 8"trenbaar", 9"gender", 10"preposition", 11 "vervoeging", 12 plural_form]

class Question:
    def __init__(self, record):
        self._word = record[1]
        self._meaning = record[3]
        self._vragen = [["wat betekent {} >>> ".format(record[1]),record[3]]]

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
        question1 = "Wat is de meervoud form van {} >>> ".format(self._word)
        answer1 = self._plural
        self._vragen.append([question1, answer1])

        question2 = "Wat is het lidwoord van {} >>> ".format(self._word)
        answer2 = self._article
        self._vragen.append([question2, answer2])

    def question_answer(self):
        chosen_question = random.choice(self._vragen)
        print (self._vragen)
        question = chosen_question[0]
        answer = chosen_question[1]
        return question, answer


def build_exercise(number_of_tries, vocabulary_file, category):
        with codecs.open(vocabulary_file, 'r','UTF-8') as input_file:
            # complete vocabulary contains all records in file
            complete_vocabulary = [row.rstrip('\r\n').split('\t') for row in input_file]

            # todo write flow when no category is chosen

            # complete_set contains all records in file with the given category
            complete_set = [row for row in complete_vocabulary if row[2] == category]
            print(complete_set)

            # random.shuffle mixed the order of the elements of the list
            # random.shuffle(complete_set)

            while number_of_tries:
                this_record = random.choice(complete_set)
                q = Question(this_record)
                # q = Question(complete_set[number_of_tries])
                question, answer = q.question_answer()
                user_answer = input(question)
                if user_answer == answer:
                    print ("so far so good")
                else:
                    print("not yet there, the answer is {}".format(answer))
                number_of_tries -= 1


# todo move to test file

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

# todo write module to write new vocabulary file
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
    check_number_of_fields(vocabulary_file_name)
    build_exercise(number_of_tries, vocabulary_file_name, category)


if __name__ == "__main__":
    main()