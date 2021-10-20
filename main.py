def citireLista():
    '''
    Formeaza lista
    :return: lista citita
    '''
    l = []
    givenString = input("Dati lista de nr. int, despartite prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def listaElementePare(l):
    '''
    determina numerele pare dintr-o lista
    :param l: lista nr intregi
    :return: numarul de elemente pare dintr-o lista
    '''
    nr = 0
    for nr in l:
        if nr % 2 == 0:
            nr = nr + 1
    return nr

def testlistaElementePare():
    assert listaElementePare([]) == 0
testlistaElementePare()

def intersectiaListelor(lst1, lst2):
    '''
    reprezinta intersectia a doua liste
    :param lst1: lista
    :param lst2: lista
    :return: intersectia celor doua liste
    '''
    rezultat = []
    if len(lst1) >= len(lst2):
        for i in lst1:
            if (i in lst2) and (i not in rezultat):
                rezultat.append(i)
    else:
        if len(lst1) > len(lst2):
            for i in lst2:
                if (i in lst1) and (i not in rezultat):
                    rezultat.append(i)
    return rezultat

def testintersectiaListelor():
    assert intersectiaListelor([1,13,23,33,43], [13,33,54,64]) == [13,33]
testintersectiaListelor()

def main():
    lst1 = []
    lst2 = []
    while True:
        print("1. Citire lista int-uri")
        print("2. Afisare lista")
        print("3. Afisare lista cu aceleasi nr de elemente pare")
        print("4. Aflati daca cele 2 liste au acelasi numar de elemente")
        print("x. Iesire")

        optiune = input("Dati optiunea:")

        if optiune == "1":
            print("lista nr. 1:")
            l = citireLista()
            print("lista nr. 2:")
            lst = citireLista()
        elif optiune == "2":
            print(lst1)
            print(lst2)
        elif optiune == "3":
            if listaElementePare(lst1) == listaElementePare(lst2):
                print("Au acelasi nr de elemente pare")
            else:
                print("Nu au acelasi nr de elemente pare")
        elif optiune == "4":
            print("Intersectia celor doua liste:", intersectiaListelor(lst1,lst2))
        elif optiune == "x":
            break
        else:
            print("Optine gresita! Reincercati.")
main()
