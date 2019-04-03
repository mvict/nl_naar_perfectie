#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import nltk
import argparse


# parameters --n number of words to practice
# category --c pos of the words to learn
# type --t  exercise type
# list --l list of words to practice

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', dest='number_of_words', help='number of words to practice', type=int)
    # parser.add_argument('-c', dest='category', help='Grammar category or part of speech')
    # parser.add_argument('-t', dest='type', help='Type of exercise')
    parser.add_argument('-l', dest='list', help='Name of the list to practice')

    args = parser.parse_args()
    vocabulary = pd.read_csv(args.list, sep='\t')
    # First line is always taken as column name and can be overwriten as:
    vocabulary.columns = ["id","string","pos","meaning","english","opposite","regular","reflexive","trenbaar","gender","preposition"]
    # print(read_file.head())
#    print(read_file["id"][0])

    good_answer = 0
    bad_answer = 0
    length = len(vocabulary) - 1
    number_of_tries = args.number_of_words

    while number_of_tries > 0:
        first_input = input('What is the meaning of %s >>> ' %vocabulary['string'][number_of_tries])
        if first_input == vocabulary['meaning'][number_of_tries]:
            print("Yes")
            good_answer += 1
        else:
            print("No, burro, it's %s!!!" %vocabulary['meaning'][number_of_tries])
            bad_answer += 1
        number_of_tries -= 1
    print("Número de aciertos %d" %number_of_tries)
    print("Número de aciertos %d" %good_answer)
    print("Número de fallos %d" %bad_answer)

    


if __name__ == "__main__":
     main()