from num2words import num2words
from random import choice, randint

import sys


def pronounceable_string(str_len=4):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
    word = ''
    consonant_toggle = True

    while len(word) < str_len:
        if consonant_toggle:
            word += choice(consonants)
            consonant_toggle = False
        else:
            word += choice(vowels)
            consonant_toggle = True

    return word


def generate_password(words=2, word_len=4, capitalize=True):
    password = ''
    pronounceable = ''

    special_chars = ['*', '!', '#', '@', '.', '-', ',', '§']
    special_chars_mapping = {'*': 'star', '!': 'bang', '#': 'pound', '@': 'at', '.': 'dot', '-': 'dash', ',': 'comma',
                             '§': 'paragraph'}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

    # determine whether or not we start with a number
    start_with_number = randint(1, 99)
    if start_with_number <= 75:
        number = randint(0, 99)
        password += str(number)
        pronounceable += num2words(number) + ' '
    else:
        letter = choice(letters)
        password += letter
        pronounceable += letter + ' '
    # add our first special character to the password
    special_char = choice(special_chars)
    password += special_char
    pronounceable += special_chars_mapping[special_char] + ' '
    # determine which letter of every word should be capitalized (if any)
    capitalize_num = randint(0, 4) if capitalize else 0
    # now we create our 'pronounceable' words for the password
    for i in range(words):
        w = pronounceable_string(word_len)
        if capitalize_num == 0:
            password += w
            pronounceable += w + ' '
        else:
            tmp = list(w)
            index = capitalize_num - 1
            tmp[index] = tmp[index].upper()
            password += ''.join(tmp)
            pronounceable += w + ' '
    # determine if we want to add a second special character
    another_special_char = randint(1, 100)
    if another_special_char <= 25:
        special_char2 = choice(special_chars)
        password += special_char2
        pronounceable += special_chars_mapping[special_char2] + ' '
    # add the last number to the password
    last_number = randint(0, 99)
    password += str(last_number)
    pronounceable += num2words(last_number)
    # decide which letter to capitalize in each word (if applicable)
    if capitalize_num > 0:
        rnd = randint(0, 100)
        if rnd < 25:
            capitalize_num += 4
        elif rnd < 50:
            capitalize_num += 8
        elif rnd < 75:
            capitalize_num += 12
        pronounceable += ' ' + num2words(capitalize_num)
    return password, pronounceable
