
#Bit reverse

def bitrevorder(seq,n):
    s=[0 for i in range(n)]
    for i in range(n):
        j=int('0b'+format(i,'03b')[::-1],base=2)
        s[i]=seq[j]
    return s




seq=[1,2,3,4,4,3,2,1]
n=len(seq)

print(bitrevorder(seq,n))
        
