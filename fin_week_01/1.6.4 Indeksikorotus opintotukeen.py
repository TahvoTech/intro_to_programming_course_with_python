# COMP.CS.100 1.6.4 Indeksikorotus opintotukeen.
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""Enter the amount of the study benefits: 335.32
If the index raise is 1.17 percent, the study benefit,
after a raise, would be 339.243244 euros"""

# Pyydetään käyttäjältä opintotuen suuruus ja muunnetaan se liukuluvuksi
opintotuki_str = input("Enter the amount of the study benefits: ")
opintotuki = float(opintotuki_str)

# Tallennetaan ensimmäisen indeksikorotuksen prosentti
indeksikorotus1 = 1.17

# Lasketaan ensimmäisen indeksikorotuksen jälkeinen opintotuki ja tallennetaan se
korotettu_opintotuki1 = opintotuki * (1 + (indeksikorotus1 / 100))

# Tulostetaan ensimmäisen indeksikorotuksen tulokset
print("If the index raise is", indeksikorotus1, "percent, the study benefit,")
print("after a raise, would be", korotettu_opintotuki1, "euros")

# Tallennetaan toisen indeksikorotuksen prosentti
indeksikorotus2 = 1.17

# Lasketaan toisen indeksikorotuksen jälkeinen opintotuki ja tallennetaan se
korotettu_opintotuki2 = korotettu_opintotuki1 * (1 + (indeksikorotus2 / 100))

# Tulostetaan toisen indeksikorotuksen tulokset
print("and if there was another index raise, the study")
print("benefits would be as much as", korotettu_opintotuki2, "euros")
