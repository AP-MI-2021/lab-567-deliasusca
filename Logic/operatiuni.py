from Domain.obiect import get_locatie, get_pret, get_id, get_nume, get_descriere, creeaza_obiect



def change_location(locatie_initiala, locatie_noua,lista):
    '''
    Mutarea tuturor obiectelor intr-o anumita locatie
    :param locatie_noua: Locatia in care vor fi mutate obiectele
    :param lista: Lista de obiecte
    :return: Returneaza o lista cu obiectele mutate intr-o locatie precizata de user
    '''

    lista_noua = []
    for obiect in lista:
        if locatie_initiala in get_locatie(obiect):
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret(obiect),
                locatie_noua
            )
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def max_price(lista):
    '''
    Determinam cel mai mare pret per locatie
    :param lista: lista de obiecte
    :return: Returneaza locatia si pretul cel mai mare din ea.
    '''
    rezultat ={}
    for obiect in lista:
        locatie= get_locatie(obiect)
        if locatie in rezultat:
             if get_pret(obiect)> rezultat[locatie]:
                rezultat[locatie] = get_pret(obiect)
        else:
            rezultat[locatie] = get_pret(obiect)

    return rezultat


def ordering_objects(lista):
    '''
    Ordoneaza obiectele crescator dupa pretul de achizitie.
    :param lista: Lista de obiecte
    :return: Returneaza o lista in ordine crescatoare in functie de pretul obiectelor.
    '''
    return sorted(lista, key = lambda obiect:get_pret(obiect))

def sum_prices (lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare locație.
    :param lista: Lista de obiecte.
    :return: Returneaza sumelor prețurilor pentru fiecare locație.
    '''
    rezultat={}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie in rezultat:
            rezultat[locatie] = rezultat[locatie] + pret
        else:
            rezultat[locatie] = pret
    return rezultat


def concatenation_str(pret,add_string,lista):
    '''
    Concateneaza un string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
    :param add_descriere: stringul adaugat la finalul fiecarei descriere
    :param pret:float
    :param lista:lista de obiecte
    :return: Returneaza lista de obiecte cu stringul modificat
    '''

    rezultat = []
    for obiect in lista:
        if pret < get_pret(obiect):
            rezultat.append(creeaza_obiect(get_id(obiect), get_nume(obiect),
                                       get_descriere(obiect) + add_string, get_pret(obiect), get_locatie(obiect)))
        else:
            rezultat.append(obiect)
    return rezultat