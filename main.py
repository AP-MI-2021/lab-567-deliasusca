from Logic.crud import adauga_obiect
from Teste.run_all_tests import run_all_tests
from UI.consola import runMenu



def main():

   run_all_tests()
   lista = []
   lista = adauga_obiect( 1 , "Calculator", "Acer",1000, "loc3", lista)
   lista = adauga_obiect( 2 ,  "Monitor", "144Hz", 3000,"loc4", lista)
   lista = adauga_obiect( 3, "Masa","lemn",4000,"loc3",lista)
   runMenu(lista)


main()


