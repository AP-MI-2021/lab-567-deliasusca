from Teste.test_crud import test_adaugare_obiect, test_stergere_obiect, test_modifica_obiect
from Teste.test_domain import test_obiect

def runAllTests():
    test_obiect()
    test_adaugare_obiect()
    test_stergere_obiect()
    test_modifica_obiect()