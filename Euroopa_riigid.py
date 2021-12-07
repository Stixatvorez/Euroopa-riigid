from module import*

countries_dict={"Österreich": "Wien", "Belgien": "Brüssel", "Vereinigtes Königreich": "London", "Deutschland": "Berliin", "Irland": "Dublin", "Liechtenstein": "Vaduz", "Niederlande": "Amsterdam", 
           "Frankreich": "Paris", "Weißrussland": "Minsk", "Bulgarien": "Sofia", "Polen": "Warschau", "Tschechien": "Prag", "Albanien": "Tirana", "Bosnien und Herzegowina": "Sarajevo",
           "Nordmazedonien": "Skopje", "Serbien": "Belgrad"}
print(countries_dict )
while True:
    print("Hallo! Gehen wir durch die Länder und ihre Hauptstädte!Привет! Поехали по странам и их столицам!")
    print("1 - Finden Sie die Hauptstadt des Landes heraus oder umgekehrt Узнай столицу страны или наоборот,\n2 - Neues Land und Hauptstadt hinzufügen Добавить новую страну и столицу,\n3 - Fehler korrigieren исправь ошибки,\n4 - Teste Dein Wissen Проверьте свои знания")
    menu=input()
    if menu=="1":
        v=input("Wir werden ein Land nach der Hauptstadt suchen Будем искать страну по столице(1) oder Hauptstadt nach Ländern или столица по стране(2)? ")
        countries(countries_dict,v)
    elif menu=="2":
        new_key_value(countries_dict)
