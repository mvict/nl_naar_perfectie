#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [0 "id", 1 "string", 2 "pos", 3 "meaning", 4 "english", 5 "opposite", 6 "regular", 7"reflexive",
# 8"trenbaar", 9"gender", 10"preposition", 11 "vervoeging", 12 plural_form]

# TODO PRINT THE RESULT TO A FILE

class GiveMeYourWord:
    def __init__(self,number):
        self._number = number
        self._word_in_list = []
        self._word = input("Your new word, please >>> ")
        self._category = input("What is the category of {}? >>> ".format(self._word))
        self._meaning = input("What is the meaning of {} in your target language? >>> ".format(self._word))
        self._english = input("What is the English word for {}? >>> ".format(self._word))

        if self._category == 'noun':
            self._fill_in_noun()
        elif self._category == 'verb':
            self._fill_in_verb()
        elif self._category == 'adjective':
            self._fill_in_adjective()

    def _fill_in_noun(self):
        gender = input("What is the gender of {}? >>> ".format(self._word))
        plural = input("What is the plural of {}? >>> ".format(self._word))
        self._word_in_list = [self._number, self._word, self._category, self._meaning, self._english,
                              "n/a", "n/a", "n/a", "n/a", gender, "n/a", "n/a", plural]
    def _fill_in_verb(self):
        preposition = input("Which preposition does {} require? (or 'n/a' otherwise) >>> ".format(self._word))
        reflexive = input("Is this verb reflexive? (answer TRUE or FALSE) >>> ".format(self._word))
        separable = input("Is this verb separable? (answer TRUE or FALSE) >>> ".format(self._word))
        regular = input("Is this verb regular? (answer TRUE or FALSE) >>> ".format(self._word))

        if regular == 'TRUE':
            declination = input("What is the past and past particle of {} >>> ".format(self._word))
        else:
            declination = 'n/a'

        self._word_in_list = [self._number, self._word, self._category, self._meaning, self._english,
                              "n/a", regular, reflexive, separable, "n/a", preposition, declination,
                              "n/a"]
    def _fill_in_adjective(self):
        self._word_in_list = [self._number, self._word, self._category, self._meaning, self._english,
                              "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a"]

    def print_to_file(self):
        print(self._word_in_list)


def main():

    number = input("How many words do you want to add to your list? >>> ")
    number_of_words = int(number)

    while number_of_words:
        word = GiveMeYourWord(number_of_words)
        word.print_to_file()
        number_of_words -= 1


if __name__ == "__main__":
    main()