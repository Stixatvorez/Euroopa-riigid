def pealinn():
    for country in Countries:
        country=input("Введите страну:  Geben Sie Ihr Land ein: ")
        if country in Capitals:
            print("Столица страны Die Hauptstadt des Landes "+country+": " +Capitals[country])
            p=input("Возможно в базе данных ошибка, хотите исправить её? Vielleicht liegt ein Fehler in der Datenbank vor, möchten Sie ihn beheben?  ")
            if p=="Да":
                o=input("Введите правильно страну: Geben Sie das richtige Land ein: ")
                l=input("Введите правильно столицу: Geben Sie das richtige Kapital ein: ")
                Capitals.pop(country)
                Capitals.update({o: l})
            elif p=="Нет":
                print("Всего доброго! Alles Gute!")
        else:
            print("В базе данных не страны с названием Es sind keine Länder mit dem Namen in der Datenbank vorhanden" +country)
            v=input("Хотите внести Willst du beitragen " +country+ " в базу данных?: zur Datenbank ?: ")
            if v=="Да":
                ca=input("Введите столицу страны Betreten Sie die Hauptstadt des Landes  "+country)
                Capitals.update({country: ca})
            elif v=="Нет Nein":
                print("Всего доброго! Alles Gute!")
        p=input("Хотите ли пройти тест на знания столиц Европы? Да или Нет? Möchten Sie den Wissenstest zu den europäischen Hauptstädten machen? Ja oder Nein?")
        if p=="Да":
            Countries.sort()
            Countries.reverse()
            a=0
            for i in range(10):
                print(choices(Countries))
                st=input("Введите столицу: Geben Sie die Hauptstadt ein: ")
                if st in Capitals:
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
            print("Всего доброго! Alles Gute! ")




        

