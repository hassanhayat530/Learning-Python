import sys


class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def add(self, frac_2):
        max_num = max(self.d, frac_2.d)  # calculating denominator
        while True:
            if max_num % self.d == 0 and max_num % frac_2.d == 0:
                lcm = max_num
                break
            max_num += 1
        c_1, c_2 = lcm / self.d, lcm / frac_2.d  # calculating numerator
        numer = (c_1 * self.n) + (c_2 * frac_2.n)
        gcd = self.gcd(numer, lcm)  # simplifying
        numer /= gcd
        lcm /= gcd
        return Fraction(numer, lcm)

    def sub(self, frac_2):
        max_num = max(self.d, frac_2.d)  # calculating denominator
        while True:
            if max_num % self.d == 0 and max_num % frac_2.d == 0:
                lcm = max_num
                break
            max_num += 1
        c_1, c_2 = lcm / self.d, lcm / frac_2.d  # calculating numerator
        numer = (c_1 * self.n) - (c_2 * frac_2.n)
        gcd = self.gcd(numer, lcm)  # simplifying
        numer /= gcd
        lcm /= gcd
        return Fraction(numer, lcm)

    def gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x

    def mul(self, frac_2):
        numer = self.n * frac_2.n  # calculating unsimplified fraction
        denom = self.d * frac_2.d
        gcd = self.gcd(numer, denom)  # simplifying
        numer /= gcd
        denom /= gcd
        return Fraction(numer, denom)

    def div(self, frac_2):
        frac_2.n, frac_2.d = frac_2.d, frac_2.n  # taking inverse of divisor
        numer = self.n * frac_2.n  # calculating unsimplified fraction
        denom = self.d * frac_2.d
        gcd = self.gcd(numer, denom)  # simplifying
        numer /= gcd
        denom /= gcd
        return Fraction(numer, denom)

    def __repr__(self):
        if self.d == 0:
            return 'invalid'
        if self.n % self.d == 0:
            return str(int(self.n / self.d))
        return str(int(self.n)) + '/' + str(int(self.d))


lines = ''  # reading off lines and storing them in a list
for line in sys.stdin:
    lines += line
lines = lines.split('\n')


def solve(line, operator):
    line = line.split(operator)  # creating list of numbers
    num_1 = line[0].strip()  # removing spaces
    num_2 = line[1].strip()
    num_1 = num_1.split('/')  # removing and storing numerator and denominator in a list
    num_2 = num_2.split('/')
    if len(num_1) == 1:
        frac_1 = Fraction(int(num_1[0]), 1)
    else:
        if num_1[1] == 0:
            return 'invalid'
        frac_1 = Fraction(int(num_1[0]), int(num_1[1]))
    if len(num_2) == 1:
        frac_2 = Fraction(int(num_2[0]), 1)
    else:
        if num_2[1] == 0:
            return 'invalid'
        frac_2 = Fraction(int(num_2[0]), int(num_2[1]))
    if operator == '+':
        return frac_1.add(frac_2)
    if operator == '-':
        return frac_1.sub(frac_2)
    if operator == '*':
        return frac_1.mul(frac_2)
    if operator == '\\':
        return frac_1.div(frac_2)


for line in lines:
    if '+' in line:
        print(solve(line, '+'))
    if '-' in line:
        print(solve(line, '-'))
    if '*' in line:
        print(solve(line, '*'))
    if '\\' in line:
        print(solve(line, '\\'))

