import sys

case_sense = True
if sys.argv[1] == "-i":
    case_sense = False
    one, two, three = sys.argv[2], sys.argv[3], sys.argv[4]
else:
    one, two, three = sys.argv[1], sys.argv[2], sys.argv[3]


def merge_files(one, two, three, case_sense):
    f1 = open(one, 'r')  # Assigning read,write variables
    f2 = open(two, 'r')
    output = open(three, 'w')
    f1_line = f1.readline()  # Comparison lines
    f2_line = f2.readline()

    while len(f1_line) != 0 or len(f2_line) != 0:  # loops till both lines empty
        if len(f1_line) != 0 and len(f2_line) != 0:  # no line empty
            if case_sense:  # case sensitive
                if f1_line > f2_line:
                    output.write(f2_line)
                    f2_line = f2.readline()
                else:
                    output.write(f1_line)
                    f1_line = f1.readline()
            else:  # case insensitive
                if f1_line.lower() > f2_line.lower():
                    output.write(f2_line)
                    f2_line = f2.readline()
                else:
                    output.write(f1_line)
                    f1_line = f1.readline()
        elif len(f1_line) != 0 and len(f2_line) == 0:  # line 2 empty
            output.write(f1_line)
            f1_line = f1.readline()
        else:  # line 1 empty
            output.write(f2_line)
            f2_line = f2.readline()


merge_files(one, two, three, case_sense)
