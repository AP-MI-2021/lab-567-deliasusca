from Domain.obiect import to_string
from Logic.crud import adaugare_obiect, stergere_obiect, modifica_obiect


def printMenu():
    print("1.Adaugare obiect:")
    print("2.Stergere obiect:")
    print("3.Modificare obiect:")
    print("a.Afisare rezervari: ")
    print("x.Iesire")

def ui_adaugare_obiect(lista):
    id = input ("Dati id-ul: ")
    nume = input ("Dati nume: ")
    descriere = input ("Dati descriere: ")
    pret_achizitie = input ("Dati pret achizitie: ")
    locatie = input ("Dati locatie: ")
    return adaugare_obiect(id, nume, descriere, pret_achizitie, locatie, lista)

def ui_stergere_obiect(lista):
    id = input ("Dati id-ul obiectului de sters: ")
    return stergere_obiect(id, lista)

def ui_modifica_obiect(lista):
    id = input ("Dati id-ul obiectului de modificat: ")
    nume = input ("Dati noul nume: ")
    descriere = input ("Dati noua descriere: ")
    pret_achizitie = input ("Dati noul pret de achizitie: ")
    locatie = input ("Dati noua locatie: ")
    return modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista)

def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))

def runMenu(lista):
    while True :
        printMenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista)
        elif optiune == "2":
            lista =ui_stergere_obiect(lista)
        elif optiune =="3":
            lista =ui_modifica_obiect(lista)
        elif optiune =="a":
            show_all(lista)
        elif optiune =="x":
            break
        else:
            print("Optiunea este gresita!Reincercati: ")