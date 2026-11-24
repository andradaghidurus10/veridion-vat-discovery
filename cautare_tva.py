import csv
import webbrowser
from urllib.parse import quote_plus

#firme selectate
with open("rezultate_tva.csv", encoding="utf-8-sig", newline="") as fisier:
    cititor = csv.DictReader(fisier)
    companii = list(cititor)

    # caut urmatoarele 3 companii
for companie in companii[2:5]:
    nume = companie["Nume companie"]
    crn = companie["CRN"]

    print("Caut:", nume, "-", crn)

    cautare = '"' + nume + '" website'
    link = "https://www.google.com/search?q=" + quote_plus(cautare)

    webbrowser.open(link)

