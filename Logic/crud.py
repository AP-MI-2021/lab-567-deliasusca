from Domain.obiect import creeaza_obiect, get_id
from Logic.validator import validate_obiect


def adaugare_obiect(id,nume,descriere,pret_achizitie,locatie,lista):
    """
    Adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: lista ce contine obiectele vechi+noul obiect
    """
    id, nume, descriere, pret_achizitie, locatie = validate_obiect(id, nume, descriere, pret_achizitie, locatie)
    obiect= creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    return lista+[obiect]



def getById(id,lista):
    """
    Da obiectul cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat
    """
    for obiect in lista:
         if get_id(obiect) == id:
             return obiect
    return None

def stergere_obiect(id,lista):
    '''
    Sterge un obiect dintr-o lista
    :param id: string
    :param lista: lista de obiecte
    :return: lista fara obiectul sters
    '''
    return[obiect for obiect in lista if get_id(obiect)!=id]

def modifica_obiect(id,nume,descriere,pret_achizitie,locatie,lista):
    """
    Modifica un obiect dupa id
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: lista cu obiectul cu id-ul dat,modificat
    """
    id, nume, descriere, pret_achizitie, locatie = validate_obiect(id, nume, descriere, pret_achizitie, locatie)
    lista_noua=[]
    for obiect in lista:
        if get_id(obiect)==id:
            obiectnou= creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
            lista_noua.append(obiectnou)
        else:
            lista_noua.append(obiect)
    return lista_noua


