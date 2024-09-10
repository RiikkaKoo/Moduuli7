def toiminnot():
    valinta = input("Valitse toiminto:\n 'Uusi lentoasema',\n 'Hae lentoasema'\n 'Lopeta'\n: ")
    print()
    return valinta

lentoasemat = {"EFHK":"Helsinki-Vantaan lentoasema",
               "CYYZ":"Toronto Pearson International Airport",
               "EETN":"Lennart Meri Tallinn Airport",
               "EGLL":"London Heathrow Airport",
               "RJAA":"Narita International Airport"}
ei_lopetus = True

toiminto = toiminnot()
while ei_lopetus:
    if toiminto.lower() == "uusi lentoasema":
        lentoasema_ICAO = input("Anna uuden lentoaseman ICAO-koodi: ")
        lentoasema_nimi = input("Anna tämän lentoaseman nimi: ")
        #lentoasemat[RKSI] = [Incheon International Airport]
        lentoasemat[lentoasema_ICAO.upper()] = lentoasema_nimi
        toiminto = toiminnot()

    elif toiminto.lower() == "hae lentoasema":
        koodi = input("Anna haettavan lentoaseman ICAO-koodi: ")
        if koodi.upper() in lentoasemat:
            print(f"Tämän lentoaseman nimi on '{lentoasemat[koodi.upper()]}'.")
            print()
        else:
            print("Tätä lentoasemaan ei löydy.")
            print()
        toiminto = toiminnot()

    elif toiminto.lower() == "lopeta":
        print("Lopetetaan...")
        ei_lopetus = False

    else:
        print()
        toiminto = toiminnot()