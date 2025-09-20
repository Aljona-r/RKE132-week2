# Tervitus Programm
# Aljona Rutkovskaja KLO2024

# Programmi käivitamine
# Kasutajalt küsitakse perekonnanime
# Kasutajalt küsitakse sugu (m või n)
# Küsitakse, kas sugu on 'm' (mees)
# Kui jah, määratakse tervituseks "härra"
# Kui sugu pole 'm', kontrollitakse, kas sugu on 'n' (naine)
# Kui jah, määratakse tervituseks "proua"
# Kui sugu pole ei 'm' ega 'n', kuvatakse erinev tervitus ja programm lõpetatakse
# Kui sugu on õigesti määratud, kuvatakse vastav tervitus
# Lõpeta programm


perekonnanimi = input("Sisesta oma perekonnanimi: ")
sugu = input("Sisesta oma sugu (m/n): ")

if sugu == "m":
    tervitus = "härra"
elif sugu == "n":
    tervitus = "proua"
else:
    print(f"Tere tulemast, {perekonnanimi}! (sugu ei olegi tähtis).")
    exit()

print(f"Tere, {tervitus} {perekonnanimi}!")