import numpy as np
import time
import sys

def IloscPowtorzen(ciag):
    powtorzenia = [0,0,0,0,0,0,0,0,0,0]
    for j in range(len(ciag)):
        powtorzenia[ciag[j]] +=1
    return powtorzenia

def liczbapermutacji(tabPowtorznia):
    sumaCyfr = 0
    dlugosc = 0
    for i in range(len(tabPowtorznia)):
        sumaCyfr+=tabPowtorznia[i] * i
        dlugosc+=tabPowtorznia[i]
    
    mianownik = 1
    for i in range(len(tabPowtorznia)):
        mianownik = mianownik * np.math.factorial(tabPowtorznia[i])
    permutacji = int(np.math.factorial(dlugosc)/mianownik)
    return permutacji

def wielokrotnosciOsiem(cyfra, parzysta):
    if parzysta==True:
        if cyfra==1:
            return int(6)
        elif cyfra==2:
            return int(4)
        elif cyfra==3:
            return int(2)
        elif cyfra==4:
            return int(0)
        elif cyfra==5:
            return int(6)
        elif cyfra==6:
            return int(4)
        elif cyfra==7:
            return int(2)
        elif cyfra==8:
            return int(0)
        elif cyfra==9:
            return int(6)
    else:
        if cyfra==1:
            return int(2)
        elif cyfra==2:
            return int(0)
        elif cyfra==3:
            return int(6)
        elif cyfra==4:
            return int(4)
        elif cyfra==5:
            return int(2)
        elif cyfra==6:
            return int(0)
        elif cyfra==7:
            return int(6)
        elif cyfra==8:
            return int(4)
        elif cyfra==9:
            return int(2)

MojWynik = 0

#8
def permutacjev3for8(ciag):
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
                    if temp%8==0:
                        MojWynik+=1
                    powtorzenia[indeksy[level]]+=1
            indeksy[level]+=1
        level-=1
        if indeksy[0]==10:
            break
        powtorzenia[indeksy[level]]+=1
        indeksy[level]+=1

#7
def permutacjev3for7(ciag):
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
                    if temp%7==0:
                        MojWynik+=1
                    powtorzenia[indeksy[level]]+=1
            indeksy[level]+=1
        level-=1
        if indeksy[0]==10:
            break
        powtorzenia[indeksy[level]]+=1
        indeksy[level]+=1
def tabNaInt(tab):
    #tablice np [2,3,4,5,3] zmieniam na wynik kotry da 23453
    wynik = 0
    i = 1
    for j in range(len(tab)-1,-1,-1):
        wynik += tab[j] * i
        i*=10
    return wynik

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

#pobieranie
Wartosci = input()
Wartosci=Wartosci.split()
#Wartosci = [0, 0]
#Wartosci[0] = sys.argv[1]
#Wartosci[1] = int(sys.argv[2])
ciag = list(Wartosci[0])
for i in range(len(ciag)):
    ciag[i] = int(ciag[i])
K = int(Wartosci[1])

if K == 2:
    suma=0
    cyfry = ciag
    powtorzenia = IloscPowtorzen(cyfry)
    for i in range(10):
        if powtorzenia[i]>=1 and i%2==0:  
            powtorzenia[i]=powtorzenia[i]-1
            suma+=liczbapermutacji(powtorzenia)
            powtorzenia[i]=powtorzenia[i]+1
    print(suma)
elif K == 5:
    suma=0
    cyfry = ciag
    powtorzenia = IloscPowtorzen(cyfry)
    for i in range(10):
        if powtorzenia[i]>=1 and i==5 or powtorzenia[i]>=1 and i==0:  
            powtorzenia[i]=powtorzenia[i]-1
            suma+=liczbapermutacji(powtorzenia)
            powtorzenia[i]=powtorzenia[i]+1
    print(suma)
elif K == 10:
    suma=0
    cyfry = ciag
    powtorzenia = IloscPowtorzen(cyfry)
    for i in range(10):
        if powtorzenia[i]>=1 and i==0:  
            powtorzenia[i]=powtorzenia[i]-1
            suma+=liczbapermutacji(powtorzenia)
            powtorzenia[i]=powtorzenia[i]+1
    print(suma)
elif K == 3:
    cyfry = ciag
    sumaCyfr = 0
    for i in range(len(cyfry)):
        sumaCyfr+=cyfry[i]
    if sumaCyfr%3==0:
        print(liczbapermutacji(IloscPowtorzen(cyfry)))
    else:
        print(0)
elif K==9:
    cyfry = ciag
    sumaCyfr = 0
    for i in range(len(cyfry)):
        sumaCyfr+=cyfry[i]
    if sumaCyfr%9==0:
        print(liczbapermutacji(IloscPowtorzen(cyfry)))
    else:
        print(0)
elif K==6:
    cyfry = ciag
    sumaCyfr = 0
    suma=0
    powtorzenia = IloscPowtorzen(cyfry)
    for i in range(len(cyfry)):
        sumaCyfr+=cyfry[i]
    if sumaCyfr%3==0:
        for i in range(10):
            if powtorzenia[i]>=1 and i%2==0:
                powtorzenia[i]=powtorzenia[i]-1
                suma+=liczbapermutacji(powtorzenia)
                powtorzenia[i]=powtorzenia[i]+1
    print(suma)
elif K==4:
    if len(ciag)==1 and ciag[0]==4 or len(ciag)==1 and ciag[0]==8:
        print(1)
        exit()
    elif len(ciag)==1 and ciag[0]!=4:
        print(0)
        exit()
    cyfry = ciag
    sumaCyfr = 0
    suma=0
    powtorzenia = IloscPowtorzen(cyfry)
    CzyWykorzystane = [False] * 100
    for i in range(10):
        if powtorzenia[i]>=1 and i%2!=0:
            powtorzenia[i]-=1
            if powtorzenia[2]>=1:
                powtorzenia[2]-=1
                suma+=liczbapermutacji(powtorzenia)
                powtorzenia[2]+=1
                temp = int(str(i)+str(2))
                CzyWykorzystane[temp] = True
            if powtorzenia[6]>=1:
                powtorzenia[6]-=1
                suma+=liczbapermutacji(powtorzenia)
                powtorzenia[6]+=1
                temp = int(str(i)+str(6))
                CzyWykorzystane[temp] = True
            powtorzenia[i]+=1
        elif powtorzenia[i]>=1 and i%2==0:
            powtorzenia[i]-=1
            if powtorzenia[4]>=1:
                powtorzenia[4]-=1
                suma+=liczbapermutacji(powtorzenia)
                powtorzenia[4]+=1
                temp = int(str(i)+str(4))
                CzyWykorzystane[temp] = True
            if powtorzenia[8]>=1:
                powtorzenia[8]-=1
                suma+=liczbapermutacji(powtorzenia)
                powtorzenia[8]+=1
                temp = int(str(i)+str(8))
                CzyWykorzystane[temp] = True
            if powtorzenia[0]>=1:
                powtorzenia[0]-=1
                suma+=liczbapermutacji(powtorzenia)
                powtorzenia[0]+=1
                temp = int(str(i)+str(0))
                CzyWykorzystane[temp] = True
            powtorzenia[i]+=1
    print(suma)
elif K==8:
    MojWynik=0
    dlugosc = 3
    powtorzenia = IloscPowtorzen(ciag)
    wynik = [0] * dlugosc
    level = 0
    suma=0
    
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
                    if temp%8==0:
                        MojWynik+=liczbapermutacji(powtorzenia)
                                       
                            
                    powtorzenia[indeksy[level]]+=1
            indeksy[level]+=1
        level-=1
        if indeksy[0]==10:
            break
        powtorzenia[indeksy[level]]+=1
        indeksy[level]+=1
    print(MojWynik)
elif K==7:
   #startTime = time.time()
   if len(ciag)<4:
       permutacjev3for7(ciag)
       print(MojWynik)
   elif len(ciag)>3 and len(ciag)<7:
       zKombinacjiKontynuacja(kombinacjev3(ciag,len(ciag),3))
   elif len(ciag)>6:
       zKombinacjiKontynuacja(kombinacjev3(ciag,len(ciag),6))
   #endtime = time.time()
   #print(endtime-startTime)
   #h = input()