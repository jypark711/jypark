# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sots the words. """
    return sorted(words)

def print_first_word(words):
    """Prints thefirst word after popping in off"""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print (word)

def sort_sentence(sentence):
    """Takes i a full seence andreturns the sorte words."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)