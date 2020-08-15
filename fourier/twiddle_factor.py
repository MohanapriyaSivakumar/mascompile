#twiddle factor
import math
"""
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


print("{}".format(twiddle(8)))
"""
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

print("{}".format(twiddle(0,8)))
print("{}".format(twiddle(1,8)))
print("{}".format(twiddle(2,8)))
print("{}".format(twiddle(3,8)))
