talvi = (1,2,12)
kevat = (3,4,5)
kesa = (6,7,8)
syksy = (9,10,11)

kuukausi = int(input("Anna kuukauden numero (1-12), niin saat tietää sen vuodenajan: "))

if kuukausi in talvi:
    print("Talvi!")
elif kuukausi in kevat:
    print("Kevät!")
elif kuukausi in kesa:
    print("Kesä!")
elif kuukausi in syksy:
    print("Syksy!")
else:
    print("Vuodessa ei ole tätä kuukautta.")