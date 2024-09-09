vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")
kuukaudet = ((3,4,5),(6,7,8),(9,10,11),(1,2,12))

kuukausi = int(input("Anna kuukauden numero (1-12), niin saat tietää sen vuodenajan: "))
if kuukausi in kuukaudet[0]:
    vuodenaika = vuodenajat[0]
    print(f"{vuodenaika}!")
elif kuukausi in kuukaudet[1]:
    vuodenaika = vuodenajat[1]
    print(f"{vuodenaika}!")
elif kuukausi in kuukaudet[2]:
    vuodenaika = vuodenajat[2]
    print(f"{vuodenaika}!")
elif kuukausi in kuukaudet[3]:
    vuodenaika = vuodenajat[3]
    print(f"{vuodenaika}!")
else:
    print("Tätä kuukautta ei ole vuodessa.")