from Domain.obiect import *
from Logic.crud import adaugare_obiect, getById
from Logic.operatiuni import schimbare_locatie, schimbare_descriere_dupa_pret, sort_obiecte

def test_schimbare_locatie():
    lista = []
    lista = adaugare_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adaugare_obiect("2", "caiet", "desc2", 12, "alba", lista)
    lista = adaugare_obiect("3", "creion","desc3", 12, "cluj", lista)

    lista = schimbare_locatie("alba","cluj",lista)

    assert get_locatie(getById("1", lista)) == "arad"
    assert get_locatie(getById("2", lista)) == "cluj"
    assert get_locatie(getById("3", lista)) == "cluj"

def test_schimbare_descriere_dupa_pret():
    lista = []
    lista = adaugare_obiect("1", "carte", "desc1", 12, "arad", lista)
    lista = adaugare_obiect("2", "caiet", "desc2", 100, "alba", lista)
    lista = adaugare_obiect("3", "creion","desc3", 34, "cluj", lista)

    lista = schimbare_descriere_dupa_pret(50,"_concatenat",lista)

    assert get_descriere(getById("1", lista)) == "desc1"
    assert get_descriere(getById("2", lista)) == "desc2_concatenat"
    assert get_descriere(getById("3", lista)) == "desc3"

def test_ordonare_obiecte():
    o1 = creeaza_obiect("1", "carte", "desc1", 12, "arad")
    o2 = creeaza_obiect("2", "caiet", "desc2", 334, "alba")
    o3 = creeaza_obiect("3", "creion","desc3", 6, "cluj")

    sorted_list = sort_obiecte([o1, o2, o3])
    assert sorted_list[0] == o3
    assert sorted_list[1] == o1
    assert sorted_list[2] == o2