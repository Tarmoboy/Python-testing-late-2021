"""

@author: Tarmoboy

"""
# Lue data tiedostosta 'suihku.txt' ja laske rms-emittanssin arvo
import numpy as np

x, xp = np.loadtxt('suihku.txt', delimiter=' ', unpack=True)
print(x)
print(xp)
n = 0
x2 = 0
while n < x.size:
    x2 = x2 + np.take(x, n)**2
    n = n+1
x2 = 1/x.size * x2
print(x2)
xp2 = 0
n = 0
while n < xp.size:
    xp2 = xp2 + np.take(xp, n)**2
    n = n+1
xp2 = 1/xp.size * xp2
print(xp2)
xxp = 0
n = 0
while n < x.size:
    xxp = xxp + (np.take(x, n)*np.take(xp, n))
    n = n+1
xxp = 1 / x.size * xxp
print(xxp)
E = np.sqrt(x2*xp2-xxp**2)
print(E)

