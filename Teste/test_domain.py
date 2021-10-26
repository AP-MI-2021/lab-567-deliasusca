from Domain.obiect import *


def test_obiect():

    obiect= creeaza_obiect("123", "Barbie Fairytopia", "DVD seria Barbie", 45.98, "S63")

    assert get_id(obiect) == "123"
    assert get_nume(obiect) == "Barbie Fairytopia"
    assert get_descriere(obiect) == "DVD seria Barbie"
    assert get_pret_achizitie(obiect) == 45.98
    assert get_locatie(obiect) == "S63"

    set_id(obiect, "130")
    set_nume(obiect, "Barbie Mariposa")
    set_descriere(obiect, "DVD seria Barbie 2021")
    set_pret_achizitie(obiect, 51.03)
    set_locatie(obiect, "S70")

    assert get_id(obiect) == "130"
    assert get_nume(obiect) == "Barbie Mariposa"
    assert get_descriere(obiect) == "DVD seria Barbie 2021"
    assert get_pret_achizitie(obiect) == 51.03
    assert get_locatie(obiect) == "S70"

