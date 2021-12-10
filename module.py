def pealinn():
    for country in Countries:
        country=input("Введите страну:  Geben Sie Ihr Land ein: ")
        if country in Capitals:
            print("Столица страны Die Hauptstadt des Landes "+country+": " +Capitals[country])
            p=input("Возможно в базе данных ошибка, хотите исправить её? Vielleicht liegt ein Fehler in der Datenbank vor, möchten Sie ihn beheben?  ")
            if p=="Да ja":
                o=input("Введите правильно страну: Geben Sie das richtige Land ein: ")
                l=input("Введите правильно столицу: Geben Sie das richtige Kapital ein: ")
                Capitals.pop(country)
                Capitals.update({o: l})
            elif p=="Нет Nein":
                print("Всего доброго! Alles Gute!")
        else:
            print("В базе данных не страны с названием Es sind keine Länder mit dem Namen in der Datenbank vorhanden" +country)
            v=input("Хотите внести Willst du beitragen " +country+ " в базу данных?: zur Datenbank ?: ")
            if v=="Да":
                ca=input("Введите столицу страны Betreten Sie die Hauptstadt des Landes  "+country)
                Capitals.update({country: ca})
            elif v=="Нет Nein":
                print("Всего доброго! Alles Gute!")
        p=input("Хотите ли пройти тест на знания столиц Европы? Да или Нет? Möchten Sie den Wissenstest zu den europäischen Hauptstädten machen? Ja oder Nein? ")
        if p=="Да ja":
            Countries.sort()
            Countries.reverse()
            m=0
            for i in range(10):
                print(choices(Countries))
                st=input("Введите столицу: Geben Sie die Hauptstadt ein: ")
                if st in Capitals:
                        print("Правильно! Richtig!")
                        m+=1
                else:
                    print("Неправильно! Nicht richtig!")
            if m==0:
                print("0%")
            elif m==1:
                print("10%")
            elif m==2:
                print("20%")
            elif m==3:
                print("30%")
            elif m==4:
                print("40%")
            elif m==5:
                print("50%")
            elif m==6:
                print("60%")
            elif m==7:
                print("70%")
            elif m==8:
                print("80%")
            elif m==9:
                print("90%")
            elif m==10:
                print("100%")
        if p=="Нет":
            print("Всего доброго! Alles Gute! ")




        

