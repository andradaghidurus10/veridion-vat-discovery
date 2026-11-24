import re
from urllib.request import Request, urlopen
from html import unescape
import csv

import re
from urllib.request import Request, urlopen
from html import unescape

url = input("Introdu linkul website-ului: ")
cerere = Request(url, headers={"User-Agent": "Mozilla/5.0"})

with urlopen(cerere, timeout=15) as raspuns:
    pagina = raspuns.read().decode("utf-8", errors="ignore")

text = re.sub(r"<[^>]+>", " ", pagina)
text = unescape(text)

numere = re.findall(r"GB\s*\d{3}\s*\d{4}\s*\d{2}", text)

if numere:
    for numar in set(numere):
        print("Numar TVA gasit:", numar)
        print("Sursa:", url)
else:
    print("Nu am gasit niciun numar TVA.")

nume_companie = input("Introdu numele companiei: ")
crn = input("Introdu numarul de inregistrare: ")



nume_gasit = nume_companie.lower() in text.lower()
crn_gasit = crn in text

if nume_gasit and crn_gasit:
    print("Numele companiei si CRN-ul au fost gasite!")
else:
    print("Nu am suficiente dovezi.")



# verific separat numele si numarul de inregistrare
print("Nume gasit:", nume_companie.lower() in text.lower())
print("CRN gasit:", crn in text)


# salvez rezultatul cautarii
if numere:
    tva = numere[0]
else:
    tva = "Negasit"

with open("teste_extragere.csv", "a", encoding="utf-8-sig", newline="") as fisier:
    scriitor = csv.writer(fisier)

    if fisier.tell() == 0:
        scriitor.writerow(["Companie", "CRN", "Website", "TVA candidat",
                           "Nume gasit", "CRN gasit"])

    scriitor.writerow([nume_companie, crn, url, tva,
                       nume_gasit, crn_gasit])

print("Rezultatul a fost salvat!")
