# ex7.3.1
def show_hidden_word(secret_word, old_letters_guessed):
    index = 0  # To put the letter in the right place in the returned word
    return_word = ['_'] * len(secret_word)

    # secret_word_list = list(secret_word)
    for letter in secret_word:
        if letter in old_letters_guessed:  # The corresponding letter should be replaced
            return_word[index] = letter
        index += 1

    return ' '.join(return_word)  # to convert into string with spaces


# secret_word = "mammals"
# old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
# print(show_hidden_word(secret_word, old_letters_guessed))

print(show_hidden_word("broadly", []))


# ex7.3.2:
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:  # missing letter
            return False
    return True  # the player guessed all the letters


# secret_word = "yes"
# old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
# print(check_win(secret_word, old_letters_guessed))
