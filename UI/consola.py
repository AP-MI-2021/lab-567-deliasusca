from Domain.obiect import to_string
from Logic.crud import adaugare_obiect, stergere_obiect, modifica_obiect
from Logic.operatiuni import schimbare_locatie, schimbare_descriere_dupa_pret, sort_obiecte


def printMenu():
    print("""
    MENIU
    1. Adaugare obiect
    2. Modificare obiect
    3. Stergere obiect
    4. Mutarea tuturor obiectelor dintr-o locație în alta.
    5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    6. Determinarea celui mai mare preț pentru fiecare locație.
    7. Ordonarea obiectelor crescător după prețul de achiziție.
    8. Afișarea sumelor prețurilor pentru fiecare locație.
    a. Afisarea tuturor obiectelor
    x. Iesire
    """)

def ui_adaugare_obiect(lista):
    """
    Adaugam in lista de obiecte un obiect citit de la tastatura
    :param lista: lista de obiecte
    :return:
    """
    id = input('Dati id-ul obiectului')
    nume = input('Dati numele')
    descriere = input('Dati descrierea')
    pret_achizitie = input('Dati pretul')
    locatie = input('Dati locatia')
    try:
        lista = adaugare_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
        print('Obiectul a fost adaugat cu succes')
        return lista
    except ValueError as ve:
        print("!!! Au aparut erori")
        print(ve)
    except:
        print('Unknown error')
    finally:
        pass
        # codul de aici se executa si daca a fost functia executata cu succes si si daca au aparut erori

def ui_stergere_obiect(lista):
    id = input ("Dati id-ul obiectului de sters: ")
    return stergere_obiect(id, lista)

def ui_modifica_obiect(lista):
    id = input ("Dati id-ul obiectului de modificat: ")
    nume = input ("Dati noul nume: ")
    descriere = input ("Dati noua descriere: ")
    pret_achizitie = input ("Dati noul pret de achizitie: ")
    locatie = input ("Dati noua locatie: ")
    try:
        lista = modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
        print('Obiectul a fost modificat cu succes')
        return lista
    except ValueError as ve:
        print("!!! Au aparut erori")
        print(ve)
    except:
        print('Unknown error')

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
            pret_comparat = float(input("cu ce valoare doresti sa compari preturile? "))
            lista = schimbare_descriere_dupa_pret(pret_comparat, str_concat, lista)
        elif optiune =="7":
            lista = sort_obiecte(lista)
        elif optiune =="a":
            show_all(lista)
        elif optiune =="x":
            break
        else:
            print("Optiunea este gresita!Reincercati: ")

















