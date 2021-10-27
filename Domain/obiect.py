def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    """
    Creaza un dictionar ce reprezinta un obiect
    :param lista:
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    """
    return [id, nume, descriere, pret_achizitie, locatie]
    #return {
    #    "id": id,
    #    "nume": nume,
    #    "descriere": descriere,
    #    "pret_achizitie": pret_achizitie,
    #    "locatie": locatie
    #}

def get_id(obiect):
    """
    Da id-ul unui obiect
    :param obiect: dict
    :return: id obiect - string
    """
    return obiect[0]
    #return obiect["id"]

def set_id(obiect, id):
    """
    Setare id la obiect
    :param obiect: dict
    :param id: string
    :return:
    """
    obiect[0] = id
    #obiect["id"] = id

def get_nume(obiect):
    """
    Da numele obiectului
    :param nume: string
    :return: nume obiect - string
    """
    return obiect[1]
    #return obiect["nume"]

def set_nume(obiect, nume):
    """
    Setare nume la obiect
    :param obiect: dict
    :param nume: string
    :return:
    """
    obiect[1] = nume
    #obiect["nume"] = nume

def get_descriere(obiect):
    """
    Da descrierea unui obiect
    :param obiect: dict
    :return: descrierea obiectului - string
    """
    return obiect[2]
    #return obiect["descriere"]

def set_descriere(obiect, descriere):
    """
    Setare descriere la obiect
    :param obiect: dict
    :param descriere: string
    :return:
    """
    obiect[2] = descriere
    #obiect["descriere"] = descriere

def get_pret_achizitie(obiect):
    """
    Da pretul de achizitie al obiectului
    :param obiect: dict
    :return: pret obiect - float
    """
    return obiect[3]
    #return obiect["pret_achizitie"]

def set_pret_achizitie(obiect, pret_achizitie):
    """
    Setare pret de achizitie la obiect
    :param obiect: dict
    :param pret_achizitie: float
    :return:
    """
    obiect[3] = pret_achizitie
    #obiect["pret_achizitie"] = pret_achizitie

def get_locatie(obiect):
    """
    Da locatia unui obiect
    :param obiect: dict
    :return: locatie obiect - string
    """
    return obiect[4]
    #return obiect["locatie"]

def set_locatie(obiect, locatie):
    """
    Setare locatie la obiect
    :param obiect: dict
    :param locatie: string
    :return: 
    """
    obiect[4] = locatie
    #obiect["locatie"] = locatie

def to_string(obiect):
    return "id: {} ,nume: {}, descriere: {},pret achizitie: {},locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret_achizitie(obiect),
        get_locatie(obiect)
    )