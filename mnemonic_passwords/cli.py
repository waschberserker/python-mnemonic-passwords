from . import pronounceable_string, generate_password

import argparse
import pyperclip


def one_password():
    parser = argparse.ArgumentParser(description='Generate a strong, easy to remember password')
    parser.add_argument('--words', '-w', type=int, help='The number of words in the password.')
    parser.add_argument('--wordlen', '-l', type=int, help='The length of each word.')
    parser.add_argument('--capitalize', '-c', type=str, help='Whether or not to add capital letters to the password.')

    args = parser.parse_args()

    words_num = args.words if args.words else 2
    word_len = args.wordlen if args.wordlen else 4
    capitalize = False
    capitalize_str = args.capitalize if args.capitalize else 'y'

    if capitalize_str.lower() == 'y' or capitalize_str.lower() == 'yes':
        capitalize = True

    password, pronounceable = generate_password(words=words_num, word_len=word_len, capitalize=capitalize)

    print('-' * 80)
    print('Here is your brand new password! Have a nice day and be safe!')
    print('-' * 80)
    print('Password: ' + password)
    print('Reminder: ' + pronounceable)
    print('-' * 80)

    pyperclip.copy(password)


def many_passwords():
    parser = argparse.ArgumentParser(description='Generate a number of strong, easy to remember passwords')
    parser.add_argument('--words', '-w', type=int, help='The number of words in the password.')
    parser.add_argument('--wordlen', '-l', type=int, help='The length of each word.')
    parser.add_argument('--capitalize', '-c', type=str, help='Whether or not to add capital letters to the password.')
    parser.add_argument('--number', '-n', type=int, help='The number of passwords to generate')

    args = parser.parse_args()

    passwords_num = args.number if args.number else 1
    words_num = args.words if args.words else 2
    word_len = args.wordlen if args.wordlen else 4
    capitalize = False
    capitalize_str = args.capitalize if args.capitalize else 'y'

    if capitalize_str.lower() == 'y' or capitalize_str.lower() == 'yes':
        capitalize = True

    output = ''
    clipboard = ''

    for i in range(passwords_num):
        password, reminder = generate_password(words=words_num, word_len=word_len, capitalize=capitalize)
        output += 'Password: ' + password + '\n' + 'Reminder: ' + reminder + '\n' + ('-' * 80) + '\n'
        clipboard += password + '\n'

    if passwords_num == 1:
        message = 'Here is your brand new password!'
    else:
        message = 'Here are your brand new passwords!'

    print('-' * 80)
    print(message, 'Have a nice day and be safe!')
    print('-' * 80)
    print(output)

    pyperclip.copy(clipboard)
