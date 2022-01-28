
# def chocolate_maker(small, big, x):
#     copy = x
#     x -= big * 5  # מספר תבניות החמש שנכנסות כפול המקום שהם תופסות
#     if x > 0:  # אין מספיק 5 בשביל למלא הכל
#         return small >= x
#     return small >= copy % 5  # ה5 ממלא הכל , רק צריך שיהיה מספיק טנים בשביל ההפרש הקטן
#
#
# print(chocolate_maker(2, 0, 6))


def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2

#
# list1 = [0.6, 1, 2, 3]
# list2 = [3, 2, 0.6, 1]
# list3 = [9, 0, 5, 10.5]
# print(are_lists_equal(list1, list2))
#
# print(are_lists_equal(list1, list3))


# def longest(my_list):
#     return sorted(my_list, key=len)[-1]
#
#
# list1 = ["111", "234", "2000", "goru", "birthday", "09"]
# print(longest(list1))




# def numbers_letters_count(my_str):
#     numbers = [0, 0]
#     for letter in my_str:
#         if letter.isdigit():
#             numbers[0] += 1
#         else:
#             numbers[1] += 1
#     return numbers


# ex8.2.1:
# data = ("self", "py", 1.543)
# format_string = "Hello %s.%s learner, you have only %0.1f units left before you\nmaster the course!"
#
# print(format_string % data)


# ex8.2.2:

# Auxiliary function:
# def second_item(tuple):
#     return tuple[1]
#
#
# def sort_prices(list_of_tuples):
#     return sorted(list_of_tuples, key=second_item, reverse=True)


# products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
# print(sort_prices(products))

# 8.2.3:
# def mult_tuple(tuple1, tuple2):
#     mult_list = []
#     for i in tuple1:
#         for j in tuple2:
#             mult_list.append((i, j))
#             mult_list.append((j, i))
#     return tuple(mult_list)


# first_tuple = (1, 2)
# second_tuple = (4, 5)
# print(mult_tuple(first_tuple, second_tuple))
#
# first_tuple = (1, 2, 3)
# second_tuple = (4, 5, 6)
# print(mult_tuple(first_tuple, second_tuple))

# ex8.2.4 : עושים פונקציה שמוצאת אנרגומה של מילה בתוך הרשימה ,
# מוסיפה את זה לרשימה שלנו וגם מעלימה את זה מהרשימה שהועברה,
# משתמשים בפונקציית העזר הזאת על כל איברי הרשימה שהועברה

# ex8.3.3:
# def count_chars(my_str):
#     dictionary = {}
#     for char in my_str:
#         if char != ' ' and char != '\t':
#             dictionary[char] = my_str.count(char)
#     return dictionary
#
#
# magic_str = "abra cadabra"
# print(count_chars(magic_str))

# ex8.3.4:
# def inverse_dict(my_dict):
#     new_dict = {}
#     # Creating the empty lists we will add the keys to in the future:
#     for val in my_dict.values():
#         new_dict[val] = []
#
#     for item in my_dict.items():
#         new_dict[item[1]].append(item[0])
#
#     return new_dict
#
#
# course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
# print(inverse_dict(course_dict))


# ex9.2.2:
# def copy_file_content(source, destination):
#     file1 = open(source, 'r')
#     file2 = open(destination, 'w')
#     file2.write(file1.read())
#     file1.close()
#     file2.close()
#
#
# copy_file_content("C:\Practicefiles\copy.txt", "C:\Practicefiles\paste.txt")
# file = open("C:\Practicefiles\paste.txt", 'r')
# print(file.read())
# file.close()


# ex9.2.3:
# def who_is_missing(file_name):
#     with open(file_name, 'r') as file:
#         string_nums = file.read().split(',')
#
#         for i in range(1, len(string_nums) + 2):
#             if str(i) not in string_nums:
#                 return i
#
#
# print(who_is_missing(r"C:\Practicefiles\findMe.txt"))

# ex9.3.1:
def my_mp3_playlist(file_path):
    file = open(file_path, 'r')
    splitted = file.split("\n")
    songs = []
    for element in splitted:
        songs.append(element.split(";"))
    first = max(songs, key=songs.itemgetter(0))
    return first


print(my_mp3_playlist(r"C:\Practicefiles\songs.txt"))
