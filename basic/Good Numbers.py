number = int(input())
num_good = 0
for num in range(1, number + 1):
    good_flag = True
    temp = num
    while temp != 0:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            good_flag = False
        temp //= 10
    if good_flag == True:
        num_good += 1
print(num_good)