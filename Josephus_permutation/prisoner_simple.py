def who_goes_free(tot, k):
    lst = []
    for i in range(tot):
        lst.append(i)
    c = -1 + k
    while len(lst) > 1:
        item = lst[(c) % len(lst)]
        inc = (c) % len(lst)
        lst.pop(inc)
        c += k - 1
        c = c % len(lst)
    return lst[0]

p=who_goes_free(7,2)
print("the person who goes free is %d"%p)
