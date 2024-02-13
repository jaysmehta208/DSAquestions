def count(num):
    counter = 0
    while (num > 0):
        num = num//10
        counter+=1
    print(counter)
count(78456)
print(len(str(6856)))