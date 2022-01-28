# ex9.4.1:
def choose_word(file_path, index):
    file = open(file_path, 'r')

    words = file.read().split(' ')  # making a list of the words

    index %= len(words)  # Circular index

    choose = words[index - 1]  # index starts from 1

    return len(dict.fromkeys(words)), choose  # remove duplicates from counting


print(choose_word(r"C:\Practicefiles\words.txt", 3))
print(choose_word(r"C:\Practicefiles\words.txt", 15))
