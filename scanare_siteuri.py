
import re
from urllib.request import Request, urlopen
from html import unescape
import csv

# paginile pe care vreau sa le verific
siteuri = [
    ("EV NAILHAUS LIMITED", "16739330",
     "https://laloocosmeticsuk.com/termsconditions/blog-post-title-one-cn6mc"),

    ("SKINCYCLES LIMITED", "12815262",
     "https://www.skincycles.com/policies/terms-of-service"),

    ("ALEXANDRA SOVERAL LIMITED", "07078190",
     "https://alexandrasoveral.com/tandcs.html")

]


# creez fisierul cu rezultatele scanarii
with open("rezultate_scanare.csv", "w", encoding="utf-8-sig", newline="") as fisier:
    scriitor = csv.writer(fisier)
    scriitor.writerow(["Companie", "CRN", "Website", "TVA candidat",
                       "Nume gasit", "CRN gasit", "Status"])


# verific fiecare pagina
for nume, crn, url in siteuri:
    print("\nVerific:", nume)

    try:
        cerere = Request(url, headers={"User-Agent": "Mozilla/5.0"})

        with urlopen(cerere, timeout=15) as raspuns:
            pagina = raspuns.read().decode("utf-8", errors="ignore")

        text = re.sub(r"<[^>]+>", " ", pagina)
        text = unescape(text)

        numere = re.findall(
            r"VAT\s*number\s*:\s*((?:GB\s*)?\d{3}\s*\d{4}\s*\d{2})",
            text,
            re.IGNORECASE
        )

        # verific identitatea companiei
        nume_gasit = nume.lower() in text.lower()
        crn_gasit = crn in text

        print("Numere TVA candidate:", numere)
        print("Nume gasit:", nume_gasit)
        print("CRN gasit:", crn_gasit)


        # salvez rezultatul companiei analizate
        with open("rezultate_scanare.csv", "a", encoding="utf-8-sig", newline="") as fisier:
            scriitor = csv.writer(fisier)
            scriitor.writerow([
                nume, crn, url,
                "; ".join(numere),
                nume_gasit, crn_gasit,
                "TVA candidat - necesita verificare HMRC" if numere else "TVA negasit pe pagina"
            ])


    except Exception as eroare:
        print("Nu am putut verifica pagina:", eroare)


