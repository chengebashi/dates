num = [9, 4, 7,32, 2, 22, 430]
swap = 0
for k in range(len(num)):
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            swap = num[i]
            num[i] = num[i+1]
            num[i+1] = swap
print(num)