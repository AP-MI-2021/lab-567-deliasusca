from Domain.obiect import get_locatie, get_pret_achizitie,get_descriere
from Logic.crud import adaugare_obiect, getById
from Logic.operatiuni import schimbare_locatie, schimbare_descriere_dupa_pret


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