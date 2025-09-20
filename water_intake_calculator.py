# Veejoomise kalkulaator
# Aljona Rutkovskaja KLO2024

# Programmi käivitamine
# Kasutajalt küsitakse, mitu klaasi vett on joonud
# Kui klaaside arv on väiksem kui 4, siis ütleb programm: „Joo rohkem vett, keha vajab seda!“
# Kui klaaside arv on 4 kuni 7, siis ütleb programm: „Tubli, jätka samas vaimus!“
# Kui klaaside arv on 8 või rohkem, siis ütleb programm: „Suurepärane, oled oma päevase eesmärgi täitnud!“
# Lõpeta programm


klaasid = float(input("Mitu klaasi vett oled täna joonud?"))
norm = 8 # 2000 ml / 250 ml = 8 klaasi

if klaasid < 4:   # alla 50%
    print("Joo rohkem vett, keha vajab seda!")
elif klaasid < 8:   # alla 100%
    print("Tubli, jätka samas vaimus!")
else:   # üle 100%
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")