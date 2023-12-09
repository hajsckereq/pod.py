import time
import numpy
import cProfile
import pstats

tab = [0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],
def start(numer):
    global tab
    tab[numer][0] = time.time()
    tab[numer][3] = tab[numer][3] + 1

def koniec(numer):
    global tab
    tab[numer][1] = time.time()
    tab[numer][2] = (tab[numer][1]-tab[numer][0])*10

#print(moja_mapa)
#print(moja_mapa[klucz])
#print(moja_mapa["bhjsdjbkdsfjkb"])
def IloscPowtorzen(ciag):
    #start(0)
    #zwraca powtorzenia cyfr w ciagu
    powtorzenia = [0,0,0,0,0,0,0,0,0,0]
    for j in range(len(ciag)):
        powtorzenia[ciag[j]] +=1
    #koniec(0)
    return powtorzenia

def kombinacjev3(ciag,dlugosc,doskrocenia):
    #start(2)
    calaLiczbaPodzielona = []
    podzieloneTablica = []
    powtorzenia = IloscPowtorzen(ciag)
    wynik = [' '] * dlugosc
    level = 0
    
    indeksy = [0] * dlugosc
    while True:
        while indeksy[level]<len(powtorzenia):
            if powtorzenia[indeksy[level]]>0:
                powtorzenia[indeksy[level]]-=1
                wynik[level]=(indeksy[level])
                
                if level<dlugosc-1:
                    levelTeraz = level
                    level+=1
                    if level%(doskrocenia)==0:
                        indeksy[level]=0
                    else:
                        indeksy[level]=indeksy[level-1]
                    continue
                else:
                    wynik[level]=(indeksy[level])
                    Rwynik = wynik[::-1]
                    for m in range(0,len(wynik),doskrocenia):
                        koniecPodzialu = m+doskrocenia
                        podtablica=Rwynik[m:koniecPodzialu]
                        podtablica=podtablica[::-1]
                        calaLiczbaPodzielona.append(podtablica)
                    calaLiczbaPodzielona = calaLiczbaPodzielona[::-1]
                    podzieloneTablica.append(calaLiczbaPodzielona)
                    calaLiczbaPodzielona = []
                    powtorzenia[indeksy[level]]+=1

            indeksy[level]+=1
        level-=1
        if indeksy[0]==10:
            break
        powtorzenia[indeksy[level]]+=1
        indeksy[level]+=1
        #koniec(2)
    return podzieloneTablica 
def permutacjev3(ciag, minusPlus):
    #zwraca tablice w ktorej kazdy indeks to reszta z ciagu
    #start(3)
    resztyWTablicy = [0]*7
    tablicaWyniki = []
    wynikInt=0
    ilosc = 0
    #print(ciag)

    dlugosc = len(ciag)
    powtorzenia = IloscPowtorzen(ciag)
    wynik = [0] * dlugosc

    level = 0
    zeraPoJeden = [1,10,100,1000,10000,100000,1000000]
    indeksy = [0] * dlugosc
    while True:
        while indeksy[level]<len(powtorzenia):
            if powtorzenia[indeksy[level]]>0:
                powtorzenia[indeksy[level]]-=1
                wynik[level]=(indeksy[level])
                wynikInt += indeksy[level] * zeraPoJeden[dlugosc-level] #(10**(dlugosc-level-1))
                
                if level<dlugosc-1:
                    level+=1
                    indeksy[level]=0
                    continue
                else:
                    wynik[level]=(indeksy[level])
                    resztyWTablicy[((7000000000+(wynikInt*minusPlus))%7)]+=1
                    powtorzenia[indeksy[level]]+=1 
                    wynikInt -= indeksy[level] * zeraPoJeden[dlugosc-level]

            indeksy[level]+=1
        level-=1
        if indeksy[0]==10:
            break
        powtorzenia[indeksy[level]]+=1
        wynikInt -= indeksy[level] * zeraPoJeden[dlugosc-level]
        indeksy[level]+=1
    #koniec(3)
    return resztyWTablicy
    

def wariacjev2(ciag,dlugosc):
    #start(5)
    onFinal = 0
    #powtorzenia = IloscPowtorzen(ciag)
    wynik = [' '] * dlugosc
    level = 0
    potrzebne = 7000000
    potrzebneIndeksy = [' ',' ',' ']
    indeksy = [0] * dlugosc
    #indeksy[0] = 1
    while True:
        while indeksy[level]<len(ciag[level]):
            if level==dlugosc-1:
                pass
            if ciag[level][indeksy[level]]>0:
                #wynik[level]=(indeksy[level])
                wynik[level]=indeksy[level]#*ciag[level][indeksy[level]]
                potrzebne-=indeksy[level]
                #potrzebneIndeksy[level][indeksy[level]]
                
                if level<dlugosc-2:
                    level+=1
                    if level==0:
                        indeksy[level]=1
                    else:
                        indeksy[level]=0
                    continue
                else:
                    level+=1
                    if ciag[level][(potrzebne%7)]>0:
                        wynik[level]=(potrzebne%7)           
                        onFinal+=warjacjaCiagSuma(ciag,wynik)

                    
                level-=1
                potrzebne+=indeksy[level]
                #indeksy[level]+=1
            indeksy[level]+=1
        level-=1
        if indeksy[0]==7:
            break
        potrzebne+=indeksy[level]
        indeksy[level]+=1
    #koniec(5)
    return onFinal

def warjacjaCiagSuma(ciag,warjacja):
    #start(6)
    wynik = 1
    for i in range(len(warjacja)):
        wynik*=ciag[i][warjacja[i]]
    #koniec(6)
    return wynik

def zKombinacjiKontynuacja(kombinacjev3):
    mapaZLiczbami = {}
    tempTablica = []
    wynik = 0
    for i in range(0, len(kombinacjev3), 1): 
        for j in range(0, len(kombinacjev3[i]), 1):
            if not (str(1-((j%2)<<1))+str(kombinacjev3[i][j]) in mapaZLiczbami):
                mapaZLiczbami[str(1-((j%2)<<1))+str(kombinacjev3[i][j])]=permutacjev3(kombinacjev3[i][j], 1-((j%2)<<1))
                tempTablica.append(mapaZLiczbami[str(1-((j%2)<<1))+str(kombinacjev3[i][j])])
            else:
                tempTablica.append(mapaZLiczbami[str(1-((j%2)<<1))+str(kombinacjev3[i][j])])
        wynik+=wariacjev2(tempTablica, len(tempTablica))

        
        tempTablica = []
    #print
    print(wynik)
    #koniec(7)
                
            
def main():
        ciag = [1,2,3,4,5,6,7,8,9,0]
        zKombinacjiKontynuacja(kombinacjev3(ciag,10,6))
with cProfile.Profile() as profile:
    main()
results = pstats.Stats(profile)
results.sort_stats(pstats.SortKey.TIME)
results.print_stats()