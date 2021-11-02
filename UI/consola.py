from Domain.obiect import to_string
from Logic.crud import adaugare_obiect, stergere_obiect, modifica_obiect
from Logic.operatiuni import schimbare_locatie, schimbare_descriere_dupa_pret


def printMenu():
    print("1.Adaugare obiect:")
    print("2.Stergere obiect:")
    print("3.Modificare obiect:")
    print("4.Mutarea obiectelor dintr-o locatie in alta")
    print("5.Concatenarea unui string citit la toate descrierile "
          "obiectelor cu prețul mai mare decât o valoare citită.")
    print("a.Afisare rezervari: ")
    print("x.Iesire")

def ui_adaugare_obiect(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input('Dati pretul: '))
        locatie = input("Dati locatia: ")
        return adaugare_obiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
    """id = input('Dati id-ul obiectului')
    nume = input('Dati numele')
    descriere = input('Dati descrierea')
    pret_achizitie = input('Dati pretul')
    locatie = input('Dati locatia')
    try:
        lista = adaugare_obiect(prajituri, id, nume, descriere, pret_achizitie, locatie)
        print('Obiectul a fost adaugat cu succes')
        return lista
    except ValueError as ve:
        print("!!! Au aparut erori")
        print(ve)
    except:
        print('Unknown error')
    finally:
        pass
        # codul de aici se executa si daca a fost functia executata cu succes si si daca au aparut erori"""

def ui_stergere_obiect(lista):
    id = input ("Dati id-ul obiectului de sters: ")
    return stergere_obiect(id, lista)

def ui_modifica_obiect(lista):
    id = input ("Dati id-ul obiectului de modificat: ")
    nume = input ("Dati noul nume: ")
    descriere = input ("Dati noua descriere: ")
    pret_achizitie = float(input ("Dati noul pret de achizitie: "))
    locatie = input ("Dati noua locatie: ")
    """try:
        lista = modifica_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
        print('Obiectul a fost modificat cu succes')
        return lista
    except ValueError as ve:
        print("!!! Au aparut erori")
        print(ve)
    except:
        print('Unknown error')"""
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
        elif optiune == "4":
            locatie_initiala = input("din ce locatie doresti sa le muti? ")
            locatie_noua = input("in ce locatie doresti sa se afle obiectele? ")
            lista = schimbare_locatie(locatie_initiala, locatie_noua, lista)
        elif optiune == "5":
            str_concat = input("ce string doresti sa adaugi? ")
            pret_comparat = int(input("cu ce valoare doresti sa compari preturile? "))
            lista = schimbare_descriere_dupa_pret(pret_comparat, str_concat, lista)
        elif optiune =="a":
            show_all(lista)
        elif optiune =="x":
            break
        else:
            print("Optiunea este gresita!Reincercati: ")












