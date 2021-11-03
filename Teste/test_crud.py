from Domain.obiect import get_nume, get_descriere, get_pret_achizitie, get_locatie, creeaza_obiect, get_id
from Logic.crud import getById, adaugare_obiect, modifica_obiect, stergere_obiect


def test_adaugare_obiect():
    lista = []
    lista = adaugare_obiect("111", "cartea Minunea", "inspirat din realitate", 100, "2345", lista)
    obiect_adaugat = creeaza_obiect("111", "cartea Minunea", "inspirat din realitate", 100, "2345")
    assert len(lista) == 1
    assert lista[0] == obiect_adaugat
    assert get_nume(lista[0]) == "cartea Minunea"
    assert get_descriere(lista[0]) == "inspirat din realitate"
    assert get_pret_achizitie(lista[0]) == 100
    assert get_locatie(lista[0]) == "2345"

    lista = adaugare_obiect('12d', 'nume2', 'descriere2', 34.05, 'S345', lista)
    obiect_adaugat_2 = creeaza_obiect('12d', 'nume2', 'descriere2', 34.05, 'S345')
    assert len(lista) == 2
    assert lista[0] == obiect_adaugat
    assert lista[1] == obiect_adaugat_2

def test_stergere_obiect():
    o1 = creeaza_obiect('123', 'nume1', 'descriere1', 45.89, 'S905')
    o2 = creeaza_obiect('12d', 'nume2', 'descriere2', 34.05, 'S345')
    lista = [o1, o2]
    assert len(lista) == 2
    lista = stergere_obiect('12d', lista)
    assert len(lista) == 1
    lista = stergere_obiect('1sd2d', lista)
    assert len(lista) == 1


def test_modifica_obiect():
    o1 = creeaza_obiect('123', 'nume1', 'descriere1', 45.89, 'S905')
    o2 = creeaza_obiect('12d', 'nume2', 'descriere2', 34.05, 'S345')

    lista = [o1, o2]
    assert len(lista) == 2
    lista = modifica_obiect('12d', 'nume new', 'descriere new', 46, 'S345', lista)
    assert len(lista) == 2
    o1_new = getById('12d', lista)
    assert get_id(o1_new) == '12d'
    assert get_nume(o1_new) == 'nume new'
    assert get_descriere(o1_new) == 'descriere new'
    assert get_pret_achizitie(o1_new) == 46
    assert get_locatie(o1_new) == 'S345'

    try:
        lista = modifica_obiect('12d', '', 'descriere new', -46, 'S345', lista)
        assert False
    except ValueError:
        assert True


