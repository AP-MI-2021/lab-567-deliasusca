from Teste.test_crud import test_adaugare_obiect, test_stergere_obiect, test_modifica_obiect
from Teste.test_domain import test_obiect
from Teste.test_operatiuni import test_schimbare_locatie, test_schimbare_descriere_dupa_pret

def runAllTests():
    test_obiect()
    test_adaugare_obiect()
    test_stergere_obiect()
    test_modifica_obiect()
    test_schimbare_locatie()
    test_schimbare_descriere_dupa_pret()