"""

@author: Tarmoboy

"""
import numpy as np
import matplotlib.pyplot as plt

# Lasketaan kitkattoman tennispallon liikerata kaksiulotteisessa avaruudessa 
# (x,y) 2 sekunnin ajan lyönnin jälkeen. Välittömästi lyönnin jälkeen
# pallo etenee 45 asteen kulmassa yläviistoon nopeudella 20 m/s. 
# Ainoa voima, joka palloon vaikuttaa on gravitaatio y-suunnassa.
# Käytä Eulerin menetelmää, jossa seuraavan aika-askeleen arvot paikalle ja 
# nopeudelle riippuvat nykyisestä paikasta, nopeudesta ja kiihtyvyydestä sekä 
# tietenkin aika-askeleen pituudesta. Vastaava yhtälö pätee tietenkin myös 
# y-koordinaateille.
# Tallenna pallon koordinaatit kullakin ajanhetkellä, joita on siis 
# N-kappaletta, muuttujiin x ja y. Alla olevassa koodiboksissa aikaparametrit 
# tmax, dt ja N on annettu jo valmiiksi.

# Määritellään vakiot
g = 9.81         # Gravitaatiokiihtyvyys
m = 0.1          # Massa, tarpeeton
v0 = 20          # Alkuvauhti

# Alkuarvot
t0 = 0
x0 = 0
y0 = 0
vx0 = v0 * np.cos(np.pi/4)      
vy0 = v0 * np.sin(np.pi/4)      

tmax = 2         # Aika joka lasketaan
dt = 0.01        # Yhden askeleen pituus
N = int(tmax/dt) # Askelten lukumäärä

# Laske näihin muuttujiin pallon koordinaatit
x = np.zeros(N)
y = np.zeros(N)
i = 1
# x[0] ja y[0] ovat nollia joten aloitetaan suoraan indeksistä 1
while i < N:
    # Eulerin menetelmä
    y[i] = y[i-1] + vy0 * dt 
    vy0 = vy0 - g * dt 
    x[i] = x[i-1] + vx0 * dt
    i += 1
print(x)
print(y)
plt.plot(x, y)
plt.show()
