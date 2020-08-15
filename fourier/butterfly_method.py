#twiddle factor
import math
def twiddle(n):
    k=int(n/2)
    w=[0 for i in range(k)]
    for i in range(k):
        rl=float(format(math.cos((2*(math.pi)*i)/n),'.4f'))
        im=-(float(format(math.sin((2*(math.pi)*i)/n),'.4f')))
        if((rl==0) and (im==0)):
            w[i]=0
        elif(im==0):
            w[i]=rl
        else:
            w[i]=complex(rl,im)
    return w

#Bit reverse

def bitrevorder(seq,n):
    s=[0 for i in range(n)]
    for i in range(n):
        j=int('0b'+format(i,'03b')[::-1],base=2)
        s[i]=seq[j]
    return s

#butterfly
def butter(seq_c,w,n):
    s=[0 for i in range(n)]
    for i in range(n):
        if(i%2==0):
            s[i]=seq_c[i]+seq_c[i+1]*w
        else:
            s[i]=seq_c[i-1]+seq_c[i]*w*(-1)
    return s
seq=[1,2,3,4,4,3,2,1]
n=len(seq)

seq_c=bitrevorder(seq,n)
print(bitrevorder(seq,n))
w=twiddle(n)
print("{}".format(twiddle(n)))        
print(butter(seq_c,w[0],n))
