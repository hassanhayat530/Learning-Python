import sys

lines = []
for line in sys.stdin:
    line = line.replace('\n', '')
    lines.append(line)

N = list(map(int, lines[0].split(' ')))
sequence = list(map(int, lines[1].split(' ')))
numbers = list(map(int, lines[2].split(' ')))
occurrences_list = []

def first_occurrence(sequence, target):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or sequence[mid - 1] < target) and sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def last_occurrence(sequence, target):
    left = 0
    right = len(sequence) - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == len(sequence) - 1 or sequence[mid + 1] > target) and sequence[mid] == target:
            return mid
        elif sequence[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

for target in numbers:
    first = first_occurrence(sequence, target)
    last = last_occurrence(sequence, target)
    if first != -1 and last != -1:
        occurrences_list.append(last - first + 1)
    else:
        occurrences_list.append(0)

for count in occurrences_list:
    print(count)