from . import pronounceable_string, generate_password

import argparse
import pyperclip


def main():
    parser = argparse.ArgumentParser(description='Generate strong, easy to remember passwords')
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
