from Domain.obiect import get_id, creeaza_obiect
from Logic.validator import validate_obiect

def adauga_obiect2(obiecte, id, nume, descriere, pret, locatie):
    """
    Aceasta functie adauga o persoana in lista de persoane.
    :param obiecte: lista de dictionare
    :param id: numar intreg
    :param nume: sir
    :param descriere: string
    :param x1: numar intreg
    :param x2: numar intreg
    :param x3: numar intreg
    :return: 1, daca persoana poate fi adaugata (daca datele sunt valide); 0, in caz contrar
    """
    if int(id)>=0 and int(id)<=999999999:
        ok = 1
        p = creeaza_obiect(id, nume, descriere, pret, locatie)
        obiecte.append(p)
    else:
        ok = 0
    return ok

def sterge_obiect2(obiecte, id):
    """
    Aceasta functie sterge o persoana din lista, daca id-ul acesteia este acelasi cu id-ul dat.
    :param obiecte: lista de dictionare
    :param id: numar intreg
    :return: 0, daca persoana nu a fost gasita in lista; 1, daca da (si a fost stearsa)
    """
    n = len(obiecte)
    i = 0
    ok = 0
    while i<n:
        if get_id(obiecte[i]) == id:
            obiecte.remove(obiecte[i])
            ok = 1
            i = n
        else:
            i+=1
    return ok

def adauga_obiect (id, nume, descriere, pret, locatie,lista):
    '''
Adauga obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand atat elemente vechi, cat si noul obiect
    '''
    errors = []
    if getBYId(id,lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if len(locatie) != 4:
        raise ValueError("Locatia nu contine exact 4 caractere!")
    id, nume, descriere, pret, locatie = validate_obiect(id, nume, descriere, pret, locatie)
    obiect=creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]

def stergere_obiect (id,lista):
    '''
    Sterge un obiect cu id-ul dat din lista
    :param id: id-ul obiectului care se va sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara elementul cu id-ul dat
    '''
    if getBYId(id,lista) is None:
        raise ValueError("Nu exista obiect cu acest ID!")
    return [obiect for obiect in lista if get_id(obiect) != id]


def modificare_obiect (id, nume, descriere, pret, locatie, lista):
    '''
    Modifica obiectul cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: o lista de obiecte
    :return:
    '''

    if getBYId(id,lista) is None:
        raise ValueError("Nu exista obiect cu acest ID!")
    if len(locatie) != 4:
        raise ValueError("Locatia nu contine exact 4 caractere!")
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            id, nume, descriere, pret, locatie = validate_obiect(id, nume, descriere, pret, locatie)
            obiectNou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append (obiectNou)
        else:
            lista_noua.append(obiect)

    return lista_noua



def getBYId (id,lista):
    '''
    Gaseste un obiect cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return:  obiectul cu id-ul dat din lista sau None, daca aceasta nu exista
    '''


    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None

def primeste_comanda_si_argumentele(linie_de_comanda):
    """
    Aceasta functie primeste o linie de comanda din care extrage comanda si argumentele.
    Functia functioneaza pentru separatorul ',' (virgula).
    Comanda este ceea ce a gasit inainte de pozitia primului separator.
    Argumentele se afla dupa primul separator.
    Ca sa poata lucra pe acestea, desparte sirurile (pot fi mai multe cuvinte la fiecare argument) gasite,
    de fiecare data cand intalneste virgula.
    :param linie_de_comanda: sir
    :return: comanda gasita si argumentele care vin cu aceasta
    """
    pozitie = linie_de_comanda.find(',')
    if pozitie == -1:
        return linie_de_comanda, []
    comanda = linie_de_comanda[:pozitie]
    argumente = linie_de_comanda[pozitie + 1:]
    argumente = argumente.split(',')
    for cuvant in argumente:
        cuvant = cuvant.replace(',', '')
    return comanda, argumente
