import sys

def IloscPowtorzen(ciag):
    powtorzenia = [0,0,0,0,0,0,0,0,0,0]
    for j in range(len(ciag)):
        powtorzenia[ciag[j]] +=1
    return powtorzenia

def tabNaInt(tab):
    #tablice np [2,3,4,5,3] zmieniam na wynik kotry da 23453
    wynik = 0
    i = 1
    for j in range(len(tab)-1,-1,-1):
        wynik += tab[j] * i
        i*=10
    return wynik

MojWynik = 0

def main(ciag, cyferka):
    global MojWynik
    tablicaWyniki = []
    ilosc = 0
    dlugosc = len(ciag)
    powtorzenia = IloscPowtorzen(ciag)
    wynik = [0] * dlugosc
    level = 0
    
    indeksy = [0] * dlugosc
    while True:
        while indeksy[level]<len(powtorzenia):
            if powtorzenia[indeksy[level]]>0:
                powtorzenia[indeksy[level]]-=1
                wynik[level]=(indeksy[level])
                
                if level<dlugosc-1:
                    level+=1
                    indeksy[level]=0
                    continue
                else:
                    wynik[level]=(indeksy[level])
                    temp = tabNaInt(wynik)
                    if temp%cyferka==0:
                        MojWynik+=1
                    powtorzenia[indeksy[level]]+=1
            indeksy[level]+=1
        level-=1
        if indeksy[0]==10:
            break
        powtorzenia[indeksy[level]]+=1
        indeksy[level]+=1


Wartosci = [0, 0]
Wartosci[0] = sys.argv[1]
Wartosci[1] = int(sys.argv[2])
ciag = list(Wartosci[0])
for i in range(len(ciag)):
    ciag[i] = int(ciag[i])
K = int(Wartosci[1])
main(ciag, K)
print(MojWynik)
