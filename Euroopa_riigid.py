from module import*
from random import*
###text to speach
#from gtts import gTTS
#import os 
#s=gTTS(text="Estonia",lang='et',slow=True).save("heli.mp3")
#os.system("heli.mp3")
###
Capitals=dict()
Capitals["Estonia"]="Tallinn"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Finland"]="Helsinki"
Capitals["France"]="Paris"
Capitals["Germany"]="Berlin"
Capitals["Sweden"]="Stockholm"
Capitals["Spain"]="Madrid"
Capitals["Serbia"]="Belgrade"
Capitals["Norway"]="Oslo"
Capitals["Moldova"]="Chisinau"
Capitals["Greece"]="Athens"
Capitals["Bulgaria"]="Sofia"
Capitals["Austria"]="Vienna"
Capitals["Switzerland"]="Bern"
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany","Sweden","Spain","Serbia","Norway","Moldova","Greece","Bulgaria","Austria","Switzerland"]
for country in Countries:
    country=input("Введите страну: Geben Sie Ihr Land ein: ")
    if country in Capitals:
        print("Столица страны Die Hauptstadt des Landes "+country+": " +Capitals[country])
    else:
        print("В базе данных нет страны с названием Es gibt kein Land mit dem Namen in der Datenbank " +country)
        v=input("Хотите внести Willst du beitragen " +country+ " в базу данных?Да или Нет? zur Datenbank Ja oder Nein? ")
        if v=="Да":
            ca=input("Введите столицу страны Betreten Sie die Hauptstadt des Landes " +country+": ")
            Capitals.update({country: ca})
            g=input("Возможно в базе данных ошибка, хотите исправить её? Да или Нет? Vielleicht liegt ein Fehler in der Datenbank vor, möchten Sie ihn beheben? Ja oder Nein? ")
            if g=="Нет Nein":
                print("Хорошо")
            if g=="Да":
                o=input("Введите правильно страну: Bitte geben Sie das richtige Land ein: ")
                l=input("Введите правильно столицу: Geben Sie das richtige Kapital ein: ")
                Capitals.pop(country)
                Capitals.update({o: l})

        if v=="Нет":
            print("Хорошо Gut")
    a=input("Хотите ли вы начать проговаривание слов для самостоятельного изучения? Да или Нет? Möchten Sie mit dem Sprechen von Wörtern zum Selbststudium beginnen? Ja oder Nein? ")
    if a=="Да":
        sonastik={}
        countries=[]
        capitals=[]
        file=open("countries-.txt","r")
        for line in file:
            k, v=line.strip().split("-")
            sonastik[k.strip()]=v.strip()
            countries.append(k)
            capitals.append(sonastik[k.strip()])
        file.close()
        print(sonastik)
        print("Countries: ")
        print(countries)
        print("Capitals:")
        print(capitals)
        a=input()
    if a=="Нет":
        print("Хорошо Gut")
    p=input("Хотите ли пройти тест на знания столиц Европы? Да или Нет? Möchten Sie den Wissenstest zu den europäischen Hauptstädten machen? Ja oder Nein? ")
    if p=="Да":
        Countries.sort()
        Countries.reverse()
        a=0
        for i in range(10):
            country=str(choice(Countries))
            print(country)
            zp=input("Введите столицу: Geben Sie die Hauptstadt ein: ")
            if zp==Capitals[country]:
                print("Правильно! Richtig!")
                a+=1
            else:
                print("Неправильно! Nicht richtig!")
        if a==0:
            print("0%")
        elif a==1:
            print("10%")
        elif a==2:
            print("20%")
        elif a==3:
            print("30%")
        elif a==4:
            print("40%")
        elif a==5:
            print("50%")
        elif a==6:
            print("60%")
        elif a==7:
            print("70%")
        elif a==8:
            print("80%")
        elif a==9:
            print("90%")
        elif a==10:
            print("100%")
    if p=="Нет":
        print("Всего доброго! Alles Gute!")
       
