# Question 1

# def string(team):
#     last_index = len(team) - 1
#     last_letter = team[last_index]
#     first_index = team[0]
#     add_them = first_index + last_letter
#     print(add_them)


# string("Packers")

# Question 2


# def numbers(number_one, number_two):
#     for all_numbers in range(number_one, number_two):
#         if all_numbers % 3 == 0 and all_numbers % 5 == 0:
#             print("peanut butter jelly")
#         elif all_numbers % 3 == 0:
#             print("peanut butter")
#         elif all_numbers % 5 == 0:
#             print("jelly")


# numbers(0, 101)

# Question 3
# loop over the letters in word = for loop
# append the letters of the word and the index to the final word +=?
# print the final_result


# def question_three_function(word):
#     final_result = " "
#     for letters in range(len(word)):
#         print(word[letters])
#         print(letters)


# question_three_function("world peace")


# Question 4
# ingredient_list = ["sugar", "flour", "water", "milk", "egg"]


# def question_four(ingredients):
#     search = input("What ingredient would you like to search for? ")
#     while search not in ingredient_list:
#         print("That ingredient is not on the list")
#         search_again = input("Would you like to search again? y/n ")
#         if search_again == "y":
#             search = input("What ingredient would you like to search for? ")
#         else:
#             print("Okay, no worries")
#             break
#     if search in ingredients:
#         return search


# question_four(ingredient_list)


# Question 5

# list_of_colors = ["red", "yellow", "blue"]


# def reverse_list(list):
#     reverse_list = []
#     reverse_list.append(list[-1])
#     reverse_list.append(list[-2])
#     reverse_list.append(list[-3])

#     print(reverse_list)


# reverse_list(list_of_colors)

# for number in range(5)
# for items in range(len(list)):


# Question 6
list_of_names = ["Eli", "Brad", "Jimmy", "Todd", "Tim", "Tommy"]
new_list = []


def question_six(names):
    for items in names:
        if len(items) > 4:
            new_list.append(items)
            print(new_list)


question_six(list_of_names)
