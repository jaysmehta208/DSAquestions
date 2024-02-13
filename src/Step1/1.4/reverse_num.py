def reverseNum(num):
    new_num = 0
    while (num > 0):
        rem = num%10
        num = num//10
        new_num=new_num*10 + rem
    print(new_num)

reverseNum(12345)
a = 1234534
print(str(a)[len(str(a))-1: :-1])