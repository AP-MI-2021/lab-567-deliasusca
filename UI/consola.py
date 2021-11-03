from Domain.obiect import to_string
from Logic.crud import adaugare_obiect, stergere_obiect, modifica_obiect
from Logic.operatiuni import schimbare_locatie, schimbare_descriere_dupa_pret, sort_obiecte


def printMenu():
    print("""
    MENIU
    1. CRUD
    2. Operatiuni
    3. Undo
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
    """
    Afisare lista de obiecte din memorie
    :param lista: lista de obiecte
    :return:
    """
    for obiect in lista:
        print(to_string(obiect))

def print_menu_crud():
    print("""
    MENIU Crud
    1. Adaugare obiect
    2. Modificare obiect
    3. Stergere obiect
    4. Afisarea tuturor obiectelor
    5. Inapoi
    """)

def print_menu_operatiuni():
    print("""
    MENIU Operatiuni
    1. Mutarea tuturor obiectelor dintr-o locație în alta.
    2. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    3. Determinarea celui mai mare preț pentru fiecare locație.
    4. Ordonarea obiectelor crescător după prețul de achiziție.
    5. Afișarea sumelor prețurilor pentru fiecare locație.
    6. Inapoi
    """)

def run_crud_ui(lista):
    while True:
        print_menu_crud()
        cmd = input("Dati comanda: ")
        if cmd == "1":
            lista = ui_adaugare_obiect(lista)
        elif cmd == "2":
            lista = ui_modifica_obiect(lista)
        elif cmd == "3":
            lista = ui_stergere_obiect(lista)
        elif cmd == "4":
            show_all(lista)
        elif cmd == "5":
            break
        else:
            print("Comanda invalida")

def run_operatiuni_ui(lista):
    while True:
        print_menu_operatiuni()
        cmd = input("Dati comanda: ")
        if cmd == "1":
            locatie_initiala = input("din ce locatie doresti sa le muti? ")
            locatie_noua = input("in ce locatie doresti sa se afle obiectele? ")
            lista = schimbare_locatie(locatie_initiala, locatie_noua, lista)
        elif cmd == "2":
            str_concat = input("ce string doresti sa adaugi? ")
            pret_comparat = int(input("cu ce valoare doresti sa compari preturile? "))
            lista = schimbare_descriere_dupa_pret(pret_comparat, str_concat, lista)
        elif cmd == "4":
            lista = sort_obiecte(lista)
        elif cmd == "5":
            pass
        elif cmd == "6":
            break
        else:
            print("Comanda invalida")


def run_undo_ui(lista):
    pass

def run_console(lista):
    """

    :param lista: lista de obiecte
    :return:
    """
    #lista = []
    while True :
        printMenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            run_crud_ui(lista)
        elif optiune == "2":
            run_operatiuni_ui(lista)
        elif optiune =="3":
            run_undo_ui(lista)
        elif optiune =="x":
            print("La revedere!")
            break
        else:
            print("Optiunea invalida! Reincercati: ")


"""def run_console(lista):
    
    while True :
        printMenu()

        elif optiune == "4":
            locatie_initiala = input("din ce locatie doresti sa le muti? ")
            locatie_noua = input("in ce locatie doresti sa se afle obiectele? ")
            lista = schimbare_locatie(locatie_initiala, locatie_noua, lista)
        elif optiune == "5":
            str_concat = input("ce string doresti sa adaugi? ")
            pret_comparat = int(input("cu ce valoare doresti sa compari preturile? "))
            lista = schimbare_descriere_dupa_pret(pret_comparat, str_concat, lista)
        elif optiune =="6":
            lista = sort_obiecte(lista)
        elif optiune =="c":
            lista = run_client(lista)
        elif optiune =="a":
            show_all(lista)"""
"""if cmd == "1":
            lista = ui_schimbare_locatie(lista)
        elif cmd == "2":
            lista = ui_schimbare_descriere_dupa_pret(lista)"""

"""def ui_schimbare_locatie(lista):

    Schimbarea lacatiei pentru obiectele cu locatia citita de la tastatura
    :param lista: lista de obiecte
    :return:

    locatie_initiala = input("Dati locatia din care mutati:" )
    locatie_noua = input("Dati locatia unde mutati:" )
    schimbare_locatie(locatie_initiala, locatie_noua, lista)

def ui_schimbare_descriere_dupa_pret(lista):

    Concatenarea unui string citit de la tastatura la toate descrierile
    obiectelor cu prețul mai mare decât o valoare citită de la tastura.
    :param lista: lista de obiecte
    :return:

    pret_comparat = input("Dati pretul de comparatie:" )
    str_concat = input("Dati stringul" )
    schimbare_descriere_dupa_pret(pret_comparat, str_concat, lista)"""








