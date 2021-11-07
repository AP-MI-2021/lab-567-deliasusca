from Logic.crud import adauga_obiect2, sterge_obiect2, primeste_comanda_si_argumentele
from Domain.obiect import get_id, get_nume, get_descriere, get_pret, get_locatie

def help ():
    print("""
Puteti da mai multe comenzi simultan, pe care le puteti separa prin ',',inclusiv la final, fiecare functia avand structura
Adaugare: add,id,nume,descriere,pret,locatie
Stergere: delete,id-ul obiectului
Afisare Lista: showall
Iesire: iesire
""")


def ui_adauga_obiect(obiecte, *argumente):
    ok = adauga_obiect2(obiecte, *argumente)
    if ok == 0:
        print('Persoana nu a fost adaugata.')
    else:
        print('Persoana adaugata.')

def ui_sterge_obiect(obiecte, *argumente):
    ok = sterge_obiect2(obiecte, *argumente)
    if ok == 0:
        print('Persoana nu a fost stearsa, deoarece nu se gaseste in lista.')
    else:
        print('Persoana stearsa.')

def ui_afiseaza_obiecte(obiecte, *argumente):
    if len(obiecte)>0:
        print('Persoanele sunt:')
        for i in range(0, len(obiecte)):
            print('Id:', get_id(obiecte[i]))
            print('Nume:', get_nume(obiecte[i]))
            print('Descriere:', get_descriere(obiecte[i]))
            print('Pret:', get_pret(obiecte[i]))
            print('Locatie:', get_locatie(obiecte[i]))
    else:
        print('Nu exista persoane adaugate.')


def runMenu2():
    obiecte = []
    comenzi = {'add': ui_adauga_obiect, 'delete': ui_sterge_obiect, 'showall': ui_afiseaza_obiecte}
    while True:
        help()
        linie_de_comanda = input('Introduceti comanda:')
        if linie_de_comanda == 'iesire':
            break
        try:
            comanda, argumente = primeste_comanda_si_argumentele(linie_de_comanda)
            comenzi[comanda](obiecte, *argumente)
        except KeyError:
            print('Date introduse gresit!')
        except TypeError:
           print('Argumente introduse incorect!')
        except ValueError:
            print('Id-ul si x trebuie sa fie numere intregi!')