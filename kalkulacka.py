x = input("Zadejte proměnou x: ")
y = input("Zadejte proměnou y: ")

x = int(x)
y = int(y)

print("pro sčítaní zadejte +")
print("pro odčítání zadejte -")
print("pro násobení zadejte *")
print("pro dělení zadejte /")
print("pro mocnění zadejte **")
print("pro ocmodcnění zadejte /*")

znamenko = input("zvolte si operátora:")
if znamenko == "+":
    vysledek = x + y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko == "-":
    vysledek = x - y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko =="*":
    vysledek = x * y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko =="/":
    if y != 0:
        vysledek = x / y
        vysledek = str(vysledek)
        print("vysledek je: " + vysledek)
    else:
        print("nemuzes delit nulou")
elif znamenko =="**":
    vysledek = x ** y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko =="/*":
    vysledek
