def count(arr, n):
    d = {}
    for i in arr:
        if (i<=n):
            d[i] = d.get(i, 0) + 1
        
    print(d)

count([1,2,1,5,4,5,7,6, 8], 7)