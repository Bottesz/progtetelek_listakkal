''' 1. írj metódust ami a paraméterében kapott lista elemeit ki irja a képernyőre'''

''' 2. Mennyi a pozitív számok összege? - Összegzés'''

''' 3. Hánmy negatív szám van - Megszámlálás'''

''' 4. Hány nem egészszám van a számok között? - Megszámlálás'''

''' 5. Mennyi a hárommal osztható számo átlaga? - összegzés - megszámlálás'''

'''6. Mekkora a legnagyobb szám - max '''

'''7. Mekkora a legkisebb szám? - max '''

'''8. Mekkora a legkisebb és a legnagyobb szám különbsége? '''

szam_lista=[12,23, -56, 82, 12.23, 69, -100]
def elso_feladat(szam_lista):
    listahossza = len(szam_lista)
    i:int = 0
    for i in range (0,len(szam_lista),1):
        print(f"A lista {i}. eleme: {szam_lista[i]} ")

print()

def masodik_feladat(szam_lista):
    db = 0
    for i in range (1,len(szam_lista),1):
        if szam_lista[i] > 0:
            db += szam_lista[i]
    return db

print()

def harmadik_feladat(szam_lista):
    negativ = 0
    for i in range (0,len(szam_lista),1):
        if szam_lista[i] < 0:
            negativ +=1
    
    return negativ

print()

def negyedik_feladat(szam_lista):
    tortszam = 0
    for i in range (0,len(szam_lista),1):
        if szam_lista[i] % 1 != 0:
            tortszam += 1
    return tortszam 

print()

def otodik_feladat(szam_lista):
    oszthatok = 0
    db = 0
    for i in range (len(szam_lista)):
        if szam_lista[i] % 3 ==0:
            oszthatok += szam_lista[i]
            db += 1

    return oszthatok/db

def hatodik_feladat(szam_lista):
    legnagyobb = szam_lista[0]
    for i in range (len(szam_lista)):
        if legnagyobb < szam_lista[i]:
            legnagyobb = szam_lista [i]

    return legnagyobb

def hetedik_feladat(szam_lista):
    legkisebb = szam_lista[0]
    for i in range (len(szam_lista)):
        if legkisebb < szam_lista[i]:
            legkisebb = szam_lista[i]
    
    return legkisebb


def nyolcadik_feladat(szam_lista):
    különbség = 0
    legkisebb = 0
    legnagyobb = 0

    for i in range (0,len(szam_lista),1):
        if legkisebb < szam_lista[i]:
            legkisebb = szam_lista[i]
        if legnagyobb < szam_lista[i]:
            legnagyobb = szam_lista [i]
    különbség = legnagyobb - legkisebb

    return különbség