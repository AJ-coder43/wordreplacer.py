# import module
from replacer import word_replacer
# prompt for some text
string_1 = input("Enter a string: ")
# prompt for a word to replace
string_2 = input("Enter a string to replace: ")
# prompt for the replacement word
string_3 = input("Enter the string to replace with: ")
# ask if the replacement is "whole word" or not
answer = input("Replace full words only? (Y/N): ")
if answer == 'Y':
    a = word_replacer(string_2, string_3, string_1)
    print("Result =>", a) 
else:
    b = word_replacer(string_2, string_3, string_1, False)
    print("Result =>", b)