# gcd(a,b)= gcd(a-b, b), where a > b
def calcGDC(n:int, m: int) -> int:
    while(m!= 0 and n!=0):
        if (m > n):
            if (m-n > n):
                temp = n
                n = m-n
                m = temp
            else:
                m = m - n
            
        else:
            if (n - m > m):
                n = n - m
            else:
                temp = m
                m = n - m
                n = temp
    if (m == 0):
        return n
    return m

# better way to do it
def calcGCD2(n:int, m:int) -> int:
    while(n!=0 and m!=0):
        if (n > m):
            n = n%m
        else:
            m = m%n
    if (m==0):
        return n
    return m