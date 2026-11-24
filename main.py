
import csv
import re

companii = []
randuri_corectate = 0

# deschid fisierul original
with open("Companies-House-search-results.csv",
          encoding="utf-8-sig", newline="") as fisier:

    cititor = csv.reader(fisier)
    antet = next(cititor)

    for rand in cititor:

        # gasesc pozitia statutului active
        poz_status = rand.index("active")

        # reconstruiesc numele companiei
        nume = ", ".join(rand[:poz_status - 1])
        numar = rand[poz_status - 1]

        # identific unde incep codurile SIC
        inceput_sic = poz_status + 7

        # gasesc sfarsitul listei de coduri SIC
        sfarsit_sic = next(
            i for i in range(inceput_sic, len(rand))
            if rand[i].strip().endswith("]")
        )

        # reunesc separat codurile SIC si adresa
        coduri = ", ".join(rand[inceput_sic:sfarsit_sic + 1])
        adresa = ", ".join(rand[sfarsit_sic + 1:])

        # reconstruiesc cele 11 coloane
        companie = (
            [nume, numar]
            + rand[poz_status:inceput_sic]
            + [coduri, adresa]
        )

        if len(rand) > 11:
            randuri_corectate += 1

        companii.append(companie)

# salvez fisierul curatat
with open("companii_curatate.csv", "w",
          encoding="utf-8-sig", newline="") as fisier:

    scriitor = csv.writer(fisier)
    scriitor.writerow(antet)
    scriitor.writerows(companii)

# verific daca datele sunt corecte
model_sic = r"\[\s*\d{5}(?:\s*,\s*\d{5})*\s*\]"

erori = sum(
    len(c) != 11
    or c[2] != "active"
    or re.fullmatch(model_sic, c[9]) is None
    for c in companii
)

print("Companii procesate:", len(companii))
print("Randuri ajustate:", randuri_corectate)
print("Erori detectate:", erori)
print("Fisier salvat!")
