import sys

import string
word_frequency = {}
word = ''
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
the_alphabet = lowercase_letters + uppercase_letters

for line in sys.stdin:
    for char in line:
        if char in the_alphabet:
            word += char
        if char not in the_alphabet:
            if word == '':
                continue
            elif word in word_frequency:
                word_frequency[word] += 1
                word = ''
            else:
                word_frequency[word] = 1
                word = ''

count_word = []
def most_common_words(word_frequency):
    count = word_frequency.values()
    max_frq = max(count)
    word = ''
    for sequence in word_frequency:
        if word_frequency[sequence] == max_frq:
            word = sequence
    return (max_frq, word)

rng = 0
if len(word_frequency) >= 20:
    rng = 20
else:
    rng = len(word_frequency)
for i in range(rng):
    pair = most_common_words(word_frequency)
    count_word.append(pair)
    del(word_frequency[pair[1]])

for i in count_word:
    print(i[1], end=' ')
    print(i[0])
