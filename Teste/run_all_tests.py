from Teste.test_operatiuni import test_max_price
from Teste.test_crud import test_adauga_obiect, test_stergere_obiect, test_modificare_obiect, \
    test_getById
from Teste.test_domain import test_obiect


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_stergere_obiect()
    test_modificare_obiect()
    test_getById()
    test_max_price()


