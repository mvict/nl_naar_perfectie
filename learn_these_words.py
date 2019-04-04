#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import nltk
import argparse
import codecs
import random


class Question:
    def __init__(self, record):
        self._word = record[1]
        self._meaning = record[3]
        self._default_question = "Wat betekent {} >>>".format(record[1])
    #
    #     if record[2] == 'verb':
    #         self.__verb_question()
    #         self._is_regular = record[6]
    #
    #     if record[2] == 'noun':
    #         self.__noun_question()
    #
    #     if record[2] == 'adjective':
    #         self.__noun_question()
    #
    # def __verb_question(self):
    #     question1 = "Wat betekenis de vervoeging van %s".format()
    #     question2 = "welke "
    #
    # def __noun_question(self):
    #     question1 = "meervoud:"
    #     question2 = "lidwoord:"
    #
    # def __adjective_question(self):
    #     question1 = "meervoud:"
    #     question2 = "lidwoord:"

    def question_answer(self):
        question = self._default_question
        answer = self._meaning
        return question, answer


def build_exercise(number_of_tries, vocabulary_file, category):
        with codecs.open(vocabulary_file, 'r','UTF-8') as input_file:
            complete_vocabulary = [row.rstrip('\r\n').split('\t') for row in input_file]
            if category == "":
                main_routine(number_of_tries, complete_vocabulary)
            else:
                complete_set = [row for row in complete_vocabulary if row[2] == category]
                print(complete_set)

                random.shuffle(complete_set) #[:number_of_tries]
                print(complete_set)

                while number_of_tries:
                    q = Question(complete_set[number_of_tries])
                    question, answer = q.question_answer()
                    user_answer = input(question)
                    if user_answer == answer:
                        print ("so far so good")
                    else:
                        print("not yet there, it was {}".format(answer))
                    number_of_tries -= 1

        # complete_vocabulary = ["id", "string", "pos", "meaning", "english", "opposite", "regular", "reflexive",
        #                                 "trenbaar", "gender", "preposition"]


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

    build_exercise(number_of_tries, vocabulary_file_name, category)

if __name__ == "__main__":
    main()