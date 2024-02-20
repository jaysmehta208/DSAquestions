def rec(l, index):
    if (index >= len(l)):
        return
    temp = l[len(l) -1 - index]
    rec(l, index+1)
    l[index] = temp
    return
l = [1,2,3,4]


# remembering values before the recursive function call is useful for doing actions after recursion call


def rec2(l, index):
    if (index >= len(l)/2):
        return
    temp = l[len(l) -1 - index]
    l[len(l) - 1- index] = l[index]
    l[index ] = temp

    rec2(l, index+1)
    return
rec2(l, 0)
print(l)