#twiddle factor
import math
def twiddle(i,n):
    rl=float(format(math.cos((2*(math.pi)*i)/n),'.4f'))
    im=-(float(format(math.sin((2*(math.pi)*i)/n),'.4f')))
    if((rl==0) and (im==0)):
        w=0
    elif(im==0):
        w=rl
    else:
        w=complex(rl,im)
    return w

#Bit reverse

def bitrevorder(seq,n):
    s=[0 for i in range(n)]
    for i in range(n):
        j=int('0b'+format(i,'03b')[::-1],base=2)
        s[i]=seq[j]
    return s

#butterfly2
def butter(seq_c,n,p,q):
    if(p==0):
        s=[0 for i in range(n)]
        for i in range(n):
            if(i%2==0):
                s[i]=seq_c[i]+seq_c[i+1]*twiddle(0,n)
            else:
                s[i]=seq_c[i-1]+seq_c[i]*twiddle(0,n)*(-1)
    elif(p==1):
        s=[0 for i in range(n)]
        for i in range(n):
            if(i==0 or i==4):
                s[i]=seq_c[i]+seq_c[i+2]*twiddle(0,n)
            elif(i==1 or i==5):
                s[i]=seq_c[i]+seq_c[i+2]*twiddle(2,n)
            elif(i==2 or i==6):
                s[i]=seq_c[i-2]+seq_c[i]*twiddle(0,n)*(-1)
            else:
                s[i]=seq_c[i-2]+seq_c[i]*twiddle(2,n)*(-1)           
    else:
        s=[0 for i in range(n)]
        for i in range(n):
            if(i>=0 and i<4):  
                s[i]=complex(format(seq_c[i]+seq_c[i+4]*twiddle(i,n),'.3f'))
               # s[i]=seq_c[i]+seq_c[i+4]*twiddle(i,n)
                if(s[i]==0j):
                    s[i]=0
            else:
                s[i]=complex(format(seq_c[i-4]+seq_c[i]*twiddle((i-4),n)*(-1),'.3f'))
                #s[i]=seq_c[i-4]+seq_c[i]*twiddle((i-4),n)*(-1)
                if(s[i]==0j):
                    s[i]=0
    return s
    
        
                
                           
seq=[1,2,3,4,4,3,2,1]
n=len(seq)

seq_c=bitrevorder(seq,n)
print(bitrevorder(seq,n))

p=int(math.log(n,2))  #calculate stages log2(n) i.e. base=2
q=list(range(1,8))
q=list(filter(lambda y:8%y==0,q))

for i in range(p):
    seq_c=butter(seq_c,n,i,q)
    print(seq_c)

