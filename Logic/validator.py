def validate_obiect(id, nume, descriere, pret_achizitie, locatie):
    '''
    Validate params for a object
    Throws a ValueError if fields are not correct
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: string
    :param locatie: string
    :return:
    '''
    errors = []
    if id == '':
        errors.append('Id-ul nu poate fi vid')
    if nume == '':
        errors.append('Numele nu poate fi vid')
    if descriere == '':
        errors.append('Descrierea nu poate fi vida')
    #print(len(locatie))
    #if len(locatie) != 4:
    #    errors.append('Locatie trebuie sa aiba exact 4 caractere')
    try:
        pret_achizitie = float(pret_achizitie)
        if pret_achizitie < 0:
            errors.append('Pretul trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append("Pretul trebuie sa fie un numar real")

    if len(errors) != 0:
        raise ValueError(errors)

    return id, nume, descriere, pret_achizitie, locatie