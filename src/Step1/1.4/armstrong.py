def checkArmstrong(n):
    dup = n
    size= len(str(n))
    summ = 0

    while (n > 0):
        t = n%10
        n = n//10
        summ+=pow(t,size)
    if (summ == dup):
        return 'true'

    return 'false'
print(checkArmstrong(371))