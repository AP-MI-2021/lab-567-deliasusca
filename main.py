from Logic.crud import adauga_obiect
from Teste.run_all_tests import run_all_tests
from UI.consola import runMenu
from UI.command_line_console import runMenu2



def main():

   run_all_tests()
   optiune = input("Alegeti interfata: ")
   if optiune =="1":
      runMenu()
   elif optiune == "2":
      runMenu2()
   else:
      print("Optiune invalida")

main()


