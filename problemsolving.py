
# # # Question 1

# def string(team):
#     last_index = len(team) - 1
#     last_letter = team[last_index]
#     first_index = team[0]
#     add_them = first_index + last_letter
#     print(add_them)


# string("Packers")

# # # Question 2


# def numbers(number_one, number_two):
#     for all_numbers in range(number_one, number_two):
#         if all_numbers % 3 == 0 and all_numbers % 5 == 0:
#             print("peanut butter jelly")
#         elif all_numbers % 3 == 0:
#             print("peanut butter")
#         elif all_numbers % 5 == 0:
#             print("jelly")


# numbers(0, 101)

# # # Question 3
# # loop over the letters in word = for loop
# # append the letters of the word and the index to the final word +=?
# # print the final_result


# def question_three_function(word):
#     final_result = " "
#     for letters in range(len(word)):
#         print(word[letters])
#         print(letters)


# question_three_function("world peace")


# # # Question 4
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


# # # Question 5

# list_of_colors = ["red", "yellow", "blue"]


# def reverse_list(list):
#     reverse_list = []
#     for items in range(len(list) - 1, -1, -1):
#         reverse_list.append(list[items])

#     print(reverse_list)


# reverse_list(list_of_colors)


# # # Question 6
# # list_of_names = ["Eli", "Brad", "Jimmy", "Todd", "Tim", "Tommy"]
# # new_list = []


# def question_six(names):
#     for items in names:
#         if len(items) > 4:
#             new_list.append(items)
#             print(new_list)


# question_six(list_of_names)


# # Question 1, page 2
# # make a function that will print out the word "hello"
# # get the length of the string
# # use the length of the string to get a reverse string using -1 step in the range
# # add together the reverse string
# def reverse_string(string):
#     full_word = " "
#     for item in range(len(string) - 1, -1, -1):
#         full_word += string[item]
#     print(full_word)


# reverse_string("string")


# # Question 2, page 2
# # set up an input parameter
# # figure out how to capitalize letters
# # capitalize the first letter of the input
# # figure out how to capitalize after every " "
# # found the str.title function

# def capitalize_letter(input):
#     capitalize_word = str.title(input)
#     print(capitalize_word)


# capitalize_letter(input("please enter a word "))


# # Question 3, page 2
# # set a function with use input as the parameter
# # reverse the input entered
# # set an if/else function to see if the input word == the input word in reverse


# def reverse_word_function(input):
#     reversed_word = ""
#     for letter in range(len(input) - 1, -1, -1):
#         reversed_word += input[letter]
#     return reversed_word


# def palindrome(input):
#     reversed_word = reverse_word_function(input)
#     if reversed_word == input:
#         print("Neat, its a palindrome!")
#     else:
#         print("try another word")


# palindrome(input("please enter a word: "))


# # Bonus Challange
# # make a function to compress a word
#if index 0 = index 1 add 1 to count but if != index 1, still need to +1 to count

# def compress(word):
#     compressed_word = ""
#     count = 1
#     for index in range(len(word)-1):
#         if word[index] == word[index + 1]:
#             count = count + 1 
#         else:
#             compressed_word += (word[index] + str(count))
            
#             count = 1   
       
#     print(compressed_word)

    
# compress("aabbbcccc")


# Question 1, page 3




def split_up_number(number):
    number_list = []
    for individual_number in range(len(str(number))):
        single_number =(str(number)[individual_number])
        single_number = int(single_number)
        number_list.append(single_number)
    return number_list
    
def multiply_and_add(list):
    number_list = []
    for numbers in list:
        number_multiplied = numbers **2 
        number_list.append(number_multiplied)
    return number_list

def add_numbers(number_list):
    total = sum(number_list)
    return total
        



def master_function(number):
    keep_checking = True
    while keep_checking == True:
        single_number = split_up_number(number)
        multiplied_numbers = (multiply_and_add(single_number))
        total = ""
        total = add_numbers(multiplied_numbers)
        number = total
        if number == 1:
            print("This is a happy number")
            keep_checking = False
        elif number == 4:
            print("this is not a happy number")
            keep_checking = False
    

master_function(1)
