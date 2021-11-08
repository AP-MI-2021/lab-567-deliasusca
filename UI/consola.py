from Domain.obiect import to_string
from Logic.crud import adauga_obiect, stergere_obiect, modificare_obiect
from Logic.operatiuni import change_location, max_price, ordering_objects, sum_prices, concatenation_str



def printmenu():
    print("1. Adauga obiect")
    print("2. Sterge obiect")
    print("3. Modifica obiect")
    print("4. Mutarea tuturor obiectelor intr-o locatie")
    print("5. Determinarea celui mai mare preț pentru fiecare locație")
    print("6. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("7. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("8. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită")
    print("a. Afiseaza toate obiectele")
    print("u. Undo")
    print("r. Redo")
    print("x. Iesire")


def uiAdaugaObiect(lista, undolist, redolist):
    try:
        id=input ("Dati id-ul: ")
        nume = input ("Dati numele: ")
        descriere = input ("Dati descriere: ")
        pret = float( input ("Dati pret: "))
        locatie = input ("Dati locatie: ")
        rezultat = adauga_obiect(id , nume, descriere, pret, locatie, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereObiect(lista, undolist, redolist):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        rezultat =  stergere_obiect(id, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}.".format(ve))



def uiModificaObiect(lista, undolist, redolist):
    try:
        id = input("Dati id-ul prajiturii de modificat : ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float (input("Dati noul pret: "))
        locatie = input("Dati noua locatie: ")
        rezultat = modificare_obiect(id, nume, descriere, pret, locatie,lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiChangeLocation(lista, undolist, redolist):
    locatie_initiala = input("Dati locatiea initiala: ")
    locatie_noua = input("Dati locatia noua: ")
    rezultat = change_location(locatie_initiala, locatie_noua,lista)
    undolist.append(lista)
    redolist.clear()
    return rezultat

def uiMaxPrice(lista):
    rezultat = max_price(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def uiOrderingObjects(lista, undolist, redolist):
    rezultat = ordering_objects(lista)
    undolist.append(lista)
    redolist.clear()
    showAll(rezultat)


def showAll(lista):
    for obiect in lista:
        print(to_string(obiect))
    if lista == []:
        print ("Dictionarul este gol!")


def uiSumPrices(lista):
    rezultat = sum_prices(lista)
    for locatie in rezultat:
        print("Locatia {} are suma de preturi:{}".format(locatie,rezultat[locatie]))


def uiConcatenationStr(lista, undolist, redolist):
        add_string = str(input("Dati stringul: "))
        pret = float(input("Dati valoarea: "))
        rezultat=concatenation_str(pret,add_string,lista)
        undolist.append(lista)
        redolist.clear()
        showAll(rezultat)


def runMenu():
    undolist = []
    redolist = []
    lista = []
    while True:
        printmenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaObiect(lista, undolist, redolist)

        elif optiune == "2":
            lista = uiStergereObiect(lista, undolist, redolist)

        elif optiune == "3":
            lista = uiModificaObiect(lista, undolist, redolist)

        elif optiune == "4":
            lista = uiChangeLocation(lista, undolist, redolist)

        elif optiune == "5":
            uiMaxPrice(lista)

        elif optiune == "6":
            uiOrderingObjects(lista, undolist, redolist)

        elif optiune == "7":
            uiSumPrices(lista)

        elif optiune == "8":
            uiConcatenationStr(lista, undolist, redolist)

        elif optiune == "u":
            if len(undolist) > 0:
                redolist.append(lista)
                lista = undolist.pop()
            else:
                print("Nu se poate face undo!")
                
        elif optiune == "r":
            if len(redolist) > 0:
                undolist.append(lista)
                lista = redolist.pop()
            else:
                print("Nu se poate face redo!")

        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

















