"""

@author: Tarmoboy

"""
# Tarkastellaan datatiedostoa filtteri.txt. Nyt signaalissa on niin paljon 
# kohinaa että yksinkertainen taajuudenmääritys ei ymmärrettävästi onnistu. 
# Suoritetaan signaalille alipäästösuodatus kohinan vähentämiseksi. 
# Alipäästösuodatettu signaali saadaan yhtälöstä y_i=ax_i+(1-a)y_{i-1},
# missä x on alkuperäinen signaali ja kerroin a=dT/(RC+dT). Tässä dT on 
# näytteistysperiodi eli näytteiden välinen aika. Nyt tämä aika on vakio eli 
# saat laskettua sen kahden ensimmäisen näytteen aikojen erotuksena 
# dT=t_1-t_0. Aikavakio RC=1/(2pi*f_c) riippuu suodattimen katkaisutaajuudesta
# f_c. Aseta katkaisutaajuudeksi 10 kHz. Esitä graafisesti alkuperäinen 
# signaali ja suodatettu signaali samassa kuvassa. Huomaa että signaalin y 
# laskemisessa olevan rekursion vuoksi ei yllä esitettyä kaavaa voida käyttää 
# y_0​ arvon laskemiseen. Voit olettaa että y0=0. Tiedoston luku on jo tehty 
# valmiiksi. Sinun tehtäväksesi jää muuttaa for-silmukkaa siten että signaali 
# y saadaan laskettua esitetyn mukaisesti.

import numpy as np
import matplotlib.pyplot as plt

t,x = np.loadtxt('filtteri.txt',unpack=True)

f = 10000
RC = 1 / (2*np.pi*f)
dT = t[1]-t[0]
a = dT / (RC + dT)

N = len(x)
y = np.zeros(N)
y[0] = 0
i = 1
while i < x.size:
    y[i] = a*x[i] + (1-a)*y[i-1]
    i = i+1
plt.plot(x)
plt.plot(y)
plt.show()
