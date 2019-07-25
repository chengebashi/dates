num = [9, 4, 7,32, 2, 22, 430, 2, 4, 9]
sum = []
while len(num) > 0:
    m = num[0]
    for i in range(len(num)):
        if m > num[i]:
           m = num[i]
    sum.append(m)
    num.remove(m)
num = sum
print(num)