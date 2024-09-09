nimet = set()

nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        print()
        nimi = input("Anna nimi: ")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
        print()
        nimi = input("Anna nimi: ")
print()
print("Syötetyt nimet: ")
for n in nimet:
    print(n)