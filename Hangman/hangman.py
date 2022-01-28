
__author__ = "Elad Shoshani"
__version__ = "1.0"
__maintainer__ = "Elad Shoshani"
__email__ = "eladshoshani11@gmail.com"
# ---------------------------------------------------------------------------
"""A simple hangman game you can play, build as the final exercise of the self.py course"""
# ---------------------------------------------------------------------------

MAX_TRIES = 6

def start_screen(MAX_TRIES):
    """Print the Welcome Screen (and the Maximum number of failed tries below).
    :type MAX_TRIES: int
    :param MAX_TRIES: Maximum number of failed tries
    :return: None
    """
    HANGMAN_ASCII_ART = """
 _    _ 
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_| \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/"""
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


# ex6.4.1:

def is_valid_input(letter_guessed):
    """Checks whether a guessed letter is valid (a single character that is an English letter).
    :param letter_guessed: The letter the user guessed
    :type letter_guessed: str
    :return: True if the letter is valid
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


def check_valid_input(letter_guessed, old_letters_guessed):
    """The function checks two things:
     1. if the letter is valid
     2.if it is legal to guess this letter (i.e., the player has not guessed this signal before)
     returns true or false accordingly.

    :param letter_guessed: The letter the user guessed
    :param old_letters_guessed: List of letters the user had previously guessed
    :type letter_guessed: str
    :type old_letters_guessed: list (of str)
    :return: True if he letter is valid and it is legal to guess this letter and False otherwise
    :rtype: bool
    """

    letter_guessed = letter_guessed.lower()  # Large and lowercase letters are considered the same
    return is_valid_input(letter_guessed) and letter_guessed not in old_letters_guessed


# ex6.4.2:
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function uses the check_valid_input function to know if the character
     is valid and has not been guessed before, if the letter is valid and has not
     guessed it before then the function adds the letter to the old_letters_guessed list and returns True.
     Otherwise, the function prints the character X (as a large letter),
     below it the list of letters already guessed and returns false.

    :param letter_guessed: The letter the user guessed
    :param old_letters_guessed: List of letters the user had previously guessed
    :type letter_guessed: str
    :type old_letters_guessed: list (of str)
    :return: True if the letter is valid and has not been guessed before and False otherwise
    :rtype: bool
    """

    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True

    # The character is invalid or already on the guess list!
    print('X')

    # print the list as requested:
    old_letters_guessed.sort()
    old_letters_guessed_string = ' -> '.join(old_letters_guessed)
    print(old_letters_guessed_string)

    # Return false, meaning that the character cannot be added to the list of characters already guessed:
    return False


# ex7.3.1
def show_hidden_word(secret_word, old_letters_guessed):
    """A function that returns a string with of letters and underscores (only).
     The string displays the letters from the old_letters_guessed list that are
     in the secret_word string in their right positions, and the rest of
     the letters in the string (which the player has not guessed yet) as underscores (_).

    :param secret_word: The word the player need to guess (compared to old_letters_guessed list)
    :param old_letters_guessed: A list of all the letter the user has already guessed (compared to secret_word)
    :type secret_word: str
    :type old_letters_guessed: list (of str)
    :return: A string with all the guessed letters in the right positions and underscores in the other positions.
    :rtype: str
    """
    index = 0  # To put the letter in the right place in the returned word
    return_word = ['_'] * len(secret_word)  # Create underline string in the appropriate size

    for letter in secret_word:
        if letter in old_letters_guessed:  # The current _ should be replaced (by letter)
            return_word[index] = letter
        index += 1  # next position

    return ' '.join(return_word)  # to convert into string with spaces


# ex7.3.2:
def check_win(secret_word, old_letters_guessed):
    """Checks whether the user has won the game.
    :param secret_word: The word the player need to guess (compared to old_letters_guessed list)
    :param old_letters_guessed: A list of all the letter the user has already guessed (compared to secret_word)
    :type secret_word: str
    :type old_letters_guessed: list (of str)
    :return: True if the player wom the game (guessed all the letters in secret_word).
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:  # missing letter
            return False
    return True  # the player guessed all the letters


# ex8.4.1:

HANGMAN_PHOTOS = {0: """
x-------x""",
                  1: """
x-------x
|
|
|
|
|""",
                  2: """
x-------x
|       |
|       0
|
|
|""",
                  3: """
x-------x
|       |
|       0
|       |
|
|""",
                  4: """
x-------x
|       |
|       0
|      /|\\
|
|""",
                  5: """
x-------x
|       |
|       0
|      /|\\
|      /
|""",
                  6: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}


def print_hangman(num_of_tries):
    """prints the hangman according to the number of failed attempts by the user
    :param num_of_tries: The number of failed attempts by the user
    :type num_of_tries: int
    :return: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])  # find the right string in the HANGMAN_PHOTOS dictionary


# ex9.4.1:
def choose_word(file_path, index):
    """The function receives as parameters:
     1. A string representing a path to a text file containing words with space between them
     2. An index representing a particular word's placement in the file.
     The function returns the word in the index (which will be the secret word).

    :param file_path: The path to the file
    :param index: The word's placement in the file.
    :type file_path: str
    :type index: int
    :return: The word selected to be the secret word
    :rtype: str
    """
    file = open(file_path, 'r')

    words = file.read().split(' ')  # making a list of the words

    index %= len(words)  # Circular index

    choose = words[index - 1]  # index starts from 1

    return choose


def guess_letter(num_of_tries, secret_word, old_letters_guessed):
    """Performs the character guessing actions and updates the num_of_tries if necessary

    :param num_of_tries: The number of failed attempts so far
    :param secret_word: The secret word (the one the user need to guess)
    :param old_letters_guessed: A list of all the letter the user has already guessed
    :type num_of_tries: int
    :type secret_word: str
    :type old_letters_guessed: list (of str)
    :return: The updated num_of_tries
    :rtype: int
    """
    letter_guessed = input("Guess a letter: ")  # getting letter from the user

    if try_update_letter_guessed(letter_guessed, old_letters_guessed):
        if letter_guessed not in secret_word:
            num_of_tries += 1  # bad try
            print(':(')  # for the user
            print_hangman(num_of_tries)
    return num_of_tries


def hangman(secret_word):
    """Performs the course of the game a hangman (important method)
    :param secret_word: the word that the user need to guess
    :type secret_word: str
    :return: None

    """
    num_of_tries = 0
    old_letters_guessed = []

    print("Let’s start!")
    print_hangman(num_of_tries)

    # while the player did not lose
    while num_of_tries < MAX_TRIES:
        print(show_hidden_word(secret_word, old_letters_guessed))
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            return
        num_of_tries = guess_letter(num_of_tries, secret_word, old_letters_guessed)

    print(show_hidden_word(secret_word, old_letters_guessed))
    print("LOSE")


def main():
    """Performs the entire program from start to finish
    (Using the auxiliary functions of course)"""

    start_screen(MAX_TRIES)
    # getting the word from the user's file:
    file_path = input("Enter file path: ")
    index = input("Enter index: ")
    secret_word = choose_word(file_path, int(index))

    # print("secret_word is", secret_word) - for checking the game

    # start the game with the selected word:
    hangman(secret_word)


if __name__ == '__main__':
    main()
