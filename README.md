# Mnemonic Passwords

Simple little Python module that creates strong, mnemonic passwords. Along with the password, you're provided with a
reminder phrase. For example, if your generated password is `82!FiteGako65`, then your reminder phrase would be 
`eighty-two bang fite gako sixty-five one`. As you can see, the reminder is pronounceable (well, kind of). Now let's
look at how to decipher the reminder.

Our passwords starts with two digits: `8` and `2` (or `82`). They are followed by an exclamation mark (see the list of 
used special characters and their respective names below). After that come two words (you can have as many words as you 
like). In our case, these words are `fite` and `gako`. After the words comes either another special character followed 
by one more number, or just another number. Finally, if you've chosen to capitalize some of the letters in the words, 
the very last number (in our case, that's the `one`) tells you, which letter of each word you have to capitalize. In 
our example, that would be the first letter in every word. Sometimes, the last number is greater than the word length. 
In this case, simply go back to the beginning of the word and resume counting until you've reached the last number. If, 
for example, the word length would be 4 and your last number would be 13, you would also capitalize the first letter of 
each word.

**Names of the Special Characters**

```
bang        !
star        *
pound       #
at          @
dot         .
dash        -
comma       ,
paragraph   §
```

## Installation

After downloading or cloning the repository, change into the downloaded directory (the one with the setup.py file in it)
and run

```
pip install .
```

This will install the module and also make the command-line tool `new-password` available.

## Usage

### Command Line

To generate a password on the command-line, simply type

```
new-password --words=3 --wordlen=4 --capitalize=yes
```

If you need a reminder what the arguments do or how to use `new-password`, simply type:

```
new-password --help

usage: new-password [-h] [--words WORDS] [--wordlen WORDLEN]
                    [--capitalize CAPITALIZE]  
  
Generate strong, easy to remember passwords
  
optional arguments:
  -h, --help            show this help message and exit
  --words WORDS, -w WORDS
                        The number of words in the password.
  --wordlen WORDLEN, -l WORDLEN
                        The length of each word.
  --capitalize CAPITALIZE, -c CAPITALIZE
                        Whether or not to add capital letters to the password.
```

All arguments are optional. The default values for the arguments are:

* words = 2
* wordlen = 4
* capitalize = yes

### In your Python code

If you want to use the password generator in your Python scripts, you can do the following:

```
from mnemonic_passwords import generate_password

password, reminder = generate_password(words=3, wordlen=5, capitalize=False)

print(password)
print(reminder)
```

This should result in an output like this:

```
d@kocavbesucxopob46
d at kocav besuc xopob forty-six
```

## Licensing

[MIT License](https://opensource.org/licenses/MIT)


### Acknowledgements

The idea for this little helper comes from the website [Bad Neighborhood - Tools for the Uncommon Webmaster](http://www.bad-neighborhood.com/password-generator.htm). 
