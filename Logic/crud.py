from Domain.obiect import get_id, creeaza_obiect
from Logic.validator import validate_obiect


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
