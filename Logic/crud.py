from Domain.obiect import *
from Logic.validator import validate_obiect
from copy import deepcopy


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
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    lista.append(obiect)
    return lista

def getById(id,lista):
    """
    Da obiectul cu id-ul dat intr-o lista
    Daca nu-l gasim returnam None
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
    result_list = [obiect for obiect in lista if get_id(obiect)!=id]
    return result_list

def modifica_obiect(id, nume_new, descriere_new, pret_new, locatie_new,lista):
    """
    Modifica un obiect dupa id si aruncarea unei Vallue Error in cazul in care
    fieldurile nu sunt corecte
    :param id:
    :param nume_new:
    :param descriere_new:
    :param pret_new:
    :param locatie_new:
    :param lista:
    :return:
    """
    id, nume_new, descriere_new, pret_new, locatie_new = validate_obiect(id, nume_new, descriere_new, pret_new, locatie_new)
    updated_list = deepcopy(lista)
    for obiect in updated_list:
        if get_id(obiect) == id:
            set_nume(obiect, nume_new)
            set_descriere(obiect, descriere_new)
            set_pret_achizitie(obiect, pret_new)
            set_locatie(obiect, locatie_new)
    return updated_list


