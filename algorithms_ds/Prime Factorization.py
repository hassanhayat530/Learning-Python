num = int(input())
prime = 2
prime_factors = []

# Adding prime factors to a list
while prime * prime <= num:
    if num % prime == 0:
        prime_factors.append(prime)
        num //= prime
    else:
        prime += 1
if num > 1:
    prime_factors.append(num)

# Counting each prime number and storing data into a dictionary
pwr = 0
prime_dict = {}
for p in prime_factors:
    if p in prime_factors:
        pwr = prime_factors.count(p)
        prime_dict[p] = pwr
prime_num = prime_dict.keys()

# Printing prime factorization
factorization = ''
for p in prime_num:
    pwr = prime_dict[p]
    pwr_str = str(pwr)
    p_str = str(p)
    if len(factorization) > 0:
        factorization += ' * ' + p_str
    else:
        factorization += p_str
    if pwr > 1:
        factorization += '^' + pwr_str
print(factorization)
