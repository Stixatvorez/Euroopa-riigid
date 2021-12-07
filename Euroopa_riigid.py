from module import*

countries_dict={"Österreich": "Wien", "Belgien": "Brüssel", "Vereinigtes Königreich": "London", "Deutschland": "Berliin", "Irland": "Dublin", "Liechtenstein": "Vaduz", "Niederlande": "Amsterdam", 
           "Frankreich": "Paris", "Weißrussland": "Minsk", "Bulgarien": "Sofia", "Polen": "Warschau", "Tschechien": "Prag", "Albanien": "Tirana", "Bosnien und Herzegowina": "Sarajevo",
           "Nordmazedonien": "Skopje", "Serbien": "Belgrad"}
print(countries_dict )
while True:
    print("Hallo! Gehen wir durch die Länder und ihre Hauptstädte!Привет! Поехали по странам и их столицам!")
    print("1 - Finden Sie die Hauptstadt des Landes heraus oder umgekehrt Узнай столицу страны или наоборот,\n2 - Neues Land und Hauptstadt hinzufügen Добавить новую страну и столицу,\n3 - Fehler korrigieren исправь ошибки,\n4 - Teste Dein Wissen Проверьте свои знания,\n5 deutsches Lied немецкая песенка")
    menu=input()
    if menu=="1":
        v=input("Wir werden ein Land nach der Hauptstadt suchen Будем искать страну по столице(1) oder Hauptstadt nach Ländern или столица по стране(2)? ")
        countries(countries_dict,v)
    elif menu=="2":
        new_key_value(countries_dict)
    elif menu=="5":
        v=input("\nWas wollen wir trinken, sieben Tage lang,Was wollen wir trinken, so ein Durst,Was wollen wir trinken, sieben Tage lang,Was wollen wir trinken, so ein Durst,Es wird genug für alle sein,Wir trinken zusammen,Roll das Fass mal rein,Wir trinken zusammen, nicht allein,Es wird genug für alle sein,Wir trinken zusammen,Roll das Fass mal rein,Wir trinken zusammen, nicht allein,Dann wollen wir schaffen, sieben Tage lang,Dann wollen wir schaffen, komm fass an,Dann wollen wir schaffen, sieben Tage lang,Dann wollen wir schaffen, komm fass an,Und dass wird keine Plagerei,Wir schaffen zusammen,Sieben Tage lang,Ja schaffen zusammen, nicht allein,Und dass wird keine Plagerei,Wir schaffen zusammen,Sieben Tage lang,Ja schaffen zusammen, nicht allein,Jetzt müssen wir streiten,Keiner weiß wie lang,Ja, für ein Leben ohne Zwang,Jetzt müssen wir streiten,Keiner weiß wie lang,Ja, für ein Leben ohne Zwang,Dann kriegt der Frust uns nicht mehr klein,Wir halten zusammen,Keiner kämpft allein,Wir gehen zusammen, nicht allein,Dann kriegt der Frust uns nicht mehr klein,Wir halten zusammen,Keiner kämpft allein,Wir gehen zusammen, nicht allein,Was wollen wir trinken, sieben Tage lang,Was wollen wir trinken, so ein Durst,Was wollen wir trinken, sieben Tage lang,Was wollen wir trinken, so ein Durst,Es wird genug für alle sein,Wir trinken zusammen,Roll das Fass mal rein,Wir trinken zusammen, nicht allein,Es wird genug für alle sein,Wir trinken zusammen,Roll das Fass mal rein,Wir trinken zusammen, nicht allein")
