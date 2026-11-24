
import csv

# citesc fisierul cu rezultatele
with open("rezultate_tva.csv", encoding="utf-8-sig", newline="") as fisier:
    cititor = csv.DictReader(fisier)
    companii = list(cititor)
    coloane = cititor.fieldnames

# actualizez primele doua companii
for companie in companii:
    if companie["CRN"] in ["15226800", "12137082"]:
        companie["Website"] = "Neidentificat"
        companie["Sursa"] = "Google - cautari website si VAT number"
        companie["Status verificare"] = "TVA negasit - neverificat HMRC"

# salvez rezultatele actualizate
with open("rezultate_tva.csv", "w", encoding="utf-8-sig", newline="") as fisier:
    scriitor = csv.DictWriter(fisier, fieldnames=coloane)
    scriitor.writeheader()
    scriitor.writerows(companii)

print("Rezultatele au fost actualizate!")
