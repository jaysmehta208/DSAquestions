def divisors(num):
    i = 1
    while (i <= num//2):
        if (num%i == 0):
            print(i)
        i+=1
    print(num)
def square_divisors(num):
    i = 1
    while (i*i < num):
        if (num%i == 0):
            print(i)
            print(num//i)
        i+=1
    if (i*i == num):
        print(i)
square_divisors(36)