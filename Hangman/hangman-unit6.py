# ex6.4.1:

def is_valid_input(letter_guessed):
    # A single character that is an English letter:
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    return is_valid_input(letter_guessed) and \
           letter_guessed not in old_letters_guessed


# old_letters = ['a', 'b', 'c']
#
# print(check_valid_input('C', old_letters))
#
# print(check_valid_input('ep', old_letters))
#
# print(check_valid_input('$', old_letters))
#
# print(check_valid_input('s', old_letters))


# ex6.4.2:

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    # The character is invalid or already on the guess list!
    print('X')

    #print the list as requested:
    old_letters_guessed.sort()
    old_letters_guessed_string = ' -> '.join(old_letters_guessed)
    print(old_letters_guessed_string)

    # Return false, meaning that the character cannot be added to the list of characters already guessed:
    return False

old_letters = ['a', 'p', 'c', 'f']
try_update_letter_guessed('A', old_letters)

try_update_letter_guessed('s', old_letters)

try_update_letter_guessed('$', old_letters)

try_update_letter_guessed('d', old_letters)

print(old_letters)
