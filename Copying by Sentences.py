import sys

sequence_words = []
for line in sys.stdin:
    sequence_words.append(line)

sequence_words = ''.join(sequence_words)
sequence_words = sequence_words.split('\n')
sequence_words = ' '.join(sequence_words)

sentences = sequence_words.split('.')
sentences_correct = []
for line in sentences:
    line = line.strip(' ')
    sentences_correct.append(line)
sentences_correct.remove('')

sentences_lined = '.\n'.join(sentences_correct)
sentences_lined += '.'
print(sentences_lined)
