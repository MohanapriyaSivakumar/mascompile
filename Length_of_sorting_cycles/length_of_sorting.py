def cycle_length(lst,n):
    l=lst[:]
    l.sort()
    j=0
    i=lst.index(n)
    k=l.index(n)
    while(k!=i):
        t=lst[i]
        y=lst[k]
        lst[k]=t
        lst[i]=y
        i=lst.index(y)
        k=l.index(y)
        j+=1
    return j

j=cycle_length([1,6,7,2,4,3,8,9,5],7)
print(j)
