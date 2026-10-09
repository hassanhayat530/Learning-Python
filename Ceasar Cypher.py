shift = int(input())
word = input()
word = word.upper()
shift_word = ""
position = 0
import string
alphabet = string.ascii_uppercase
letters_list = list(alphabet)
for letter in word:
    if letter not in letters_list:
        shift_word += letter
        continue
    new_letter_position = letters_list.index(letter) + 1 + shift
    if new_letter_position > 26:
        new_letter_position %= 26
    if new_letter_position < 0:
        new_letter_position %= 26
        new_letter_position = abs(new_letter_position)
    shift_word += letters_list[new_letter_position - 1]
print(shift_word)