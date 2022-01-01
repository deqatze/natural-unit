pi=3.141592535

c=299792458
h=6.62607015*10**-34
G=6.6743*10**-11
kB=1.38065*10**-23
e0=8.8541878*10**-12
K=638

def x(a):
    global h,e0
    print(a)
    if a==6.62607015*10**-34:
        h/=2*pi
    elif a== 1.054571857454455e-34:
        h*=2*pi
    elif a==8.8541878*10**-12:
        e0*=4*pi



m=(h*G/c**3)**0.5
kg=(h*c/G)**0.5
s=(h*G/c**5)**0.5
K=(h*c**5/(G*kB**2))**0.5
C=(h*c*e0)**0.5
A=C/s
lm=K*c**5/G
lx=lm/m**2
N=kg*m/s**2
Pa=N/m**2
J=h/s
W=J/s
V=J/C
F=C/V
ohm=h/C**2
Wb=h/C

print('natural   >>    SI        *')
print(' SI       >>    natural   /')