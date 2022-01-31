"""

@author: Tarmoboy

"""
import math, random  # Otetaan math- ja random -kirjastot käyttöön
# Luodaan uusi funktio, kysyy listaa ja lukua
def tulosta_luvut_joita_n_kpl(x, n): 
    esiintyvyyslista = {}  # Luodaan tyhjä esiintyvyyslista
    for i in x:  # Käydään listan indeksit läpi
        # Tallennetaan muuttujaan esiintyvyyslistan avaimen i arvo tai 0
        aiemmat = esiintyvyyslista.get(i, 0)
        # Lisätään esiintyvyyslistan avaimen arvoon yksi lisää
        esiintyvyyslista[i] = aiemmat + 1  
    for j in esiintyvyyslista:  # Käydään esiintyvyyslistan avaimet läpi
        # Jos esiintyvyyslistan avaimen arvo on suurempi tai yhtä suuri 
        # kuin annettu luku
        if esiintyvyyslista[j] >= n:  
            print(j)  # Tulostetaan ehdon täyttävä avain
random.seed(1234)  # Määritetään siemenluku
print("Testi 1")  # Tulostetaan testiteksti
# Luodaan uusi satunnainen lista
x = [math.floor(math.exp(3*random.expovariate(1))) for i in range(100)]
# Käytetään funktiota listalla x, kutakin tulostettavaa lukua ainakin 5
tulosta_luvut_joita_n_kpl(x, 5)  
print("Testi 2")  # Tulostetaan toinen testiteksti
# Luodaan toinen uusi satunnainen lista
x2 = [math.floor(math.exp(3*random.expovariate(1))) for i in range(10000)]
# Käytetään funktiota listaan x2, kutakin tulostettavaa lukua ainakin 300
tulosta_luvut_joita_n_kpl(x2, 300)