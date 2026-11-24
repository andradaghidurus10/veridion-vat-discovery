import csv
import random

companii=[]

#accesez  inf folosind numele coloanelor
with open("companii_curatate.csv", encoding="utf-8-sig", newline="") as fisier:
    cititor = csv.DictReader(fisier)

    for companie in cititor:
        companii.append(companie)

    print("companiile selectate: ", len(companii))
    print(" ")

    #aleg un esantion de 20 companii random

    random.seed(42)

    esantion=random.sample(companii, 20)

    print(" Nr companii selecatate in estantion: ", len(esantion))

    #ce coloane am in fis:
    print("Coloane din fiiser: ",list(esantion[0].keys()))
    print("\nPrima companie selectata:")

    print(" ")
    for coloana, valoare in esantion[0].items():
        print(coloana,"-",valoare)

    #nr de inregistrare companii:
    nr_inreg_companii=[]
    for companie in esantion:
        nr_inreg_companii.append(companie["company_number"])
    #verif daca exista duplicate

    nr_unice=set(nr_inreg_companii)
    print("Companii selectate:", len(nr_inreg_companii))
    print("Companii unice:", len(nr_unice))
    print("Identificatori lipsa:", nr_inreg_companii.count(""))

    print(" ")

    #salvez companiile in csv :
    with open("esantion_20_companii.csv", "w", encoding="utf-8-sig", newline="") as fisier:
        scriitor = csv.DictWriter(fisier, fieldnames=esantion[0].keys())

        scriitor.writeheader()
        scriitor.writerows(esantion)
    print("Esantion salvat in csv")

    print(" ")
    for companie in esantion:
        print(companie["company_name"],"-",companie["company_number"])


    print(" ")

