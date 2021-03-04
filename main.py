from math import sqrt

#Teste
def teste():
    if p1_distance(1,1,1,1) != 0:
        raise ValueError

    if p2_double([1,2,2,3,4,6]) != 2:
        raise ValueError

    if p2_double([1,2,3,3,4,6]) != 3:
        raise ValueError

    if p3_last("Ana are mere si pere") != "si":
        raise ValueError

    if p3_last("Ana are pere si xan") != "xan":
        raise ValueError

    if len(p4_uniques("ana are ana are pere mere")) != 2:
        raise ValueError

    if len(p4_uniques("ana are ana are mere")) != 1:
        raise ValueError

#Distanta Euclidiana dintre 2 puncte.
def p1():
    x1 = int(input("x1= "))
    y1 = int(input("y1= "))

    x2 = int(input("x2= "))
    y2 = int(input("y2= "))

    print("The distance between (" + str(x1) + ":" + str(y1) + ") and (" + str(x2) + ":" + str(y2) + ") is aproximately "
          + str(p1_distance(x1, y1, x2, y2)) + " .")

def p1_distance(x1 , y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

#Numarul care apare de 2 ori in sir
def p2():
    n = int(input("nr elemente: "))

    lista = []
    for i in range(n):
        lista.append(input("x[" + str(i) + "] = "))

    print(p2_double(lista))

def p2_double(lista):
    rez = []
    for i in range(len(lista)):
        if lista[i] in rez:
            return lista[i]
        else:
            rez.append(lista[i])
    return -1

#Ultimul cuvant ca si ordine lexicografica dintr-o propozitie data
def p3():
    propozitie = input("Introduceti propozitia initiala:\n>>> ")

    print(p3_last(propozitie))

def p3_last(propozitie):
    last = "-1"
    for curent in propozitie.split():
        if (curent > last) or (last == "-1"):
            last = curent
    return last

#Cuvintele care nu se repeta dintr-o propozitie data
def p4():
    propozitie = input("Introduceti propozitia initiala:\n>>> ")

    print(p4_uniques(propozitie))

def p4_uniques(propozitie):
    cuvinte = propozitie.split()
    evidenta = []
    repetari= []

    for i in range(len(cuvinte) - 1):
        if cuvinte[i] in evidenta:
            repetari.append(cuvinte[i])
        else:
            evidenta.append(cuvinte[i])

    rez = []

    for curent in cuvinte:
        if curent not in repetari:
            rez.append(curent)

    return rez

#Descopera elementul majoritar dintr-un sir de elemente dat
def p5():
    dict = {}

    n = int(input("Numarul de elemente din sir: "))

    for i in range(n):
        x = int(input("x[" + str(i) + "] = "))
        if x in dict.keys():
            dict[x] += 1
        else:
            dict.setdefault(x, 1)

    max_key = -1
    max_value = -1

    for key in dict:
        if dict[key] > max_value:
            max_value = dict[key]
            max_key = key

    print(str(max_key) + ":" + str(max_value))


teste()
