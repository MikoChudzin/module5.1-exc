import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

# Exercise - Address Book
class BusinessCard:
    """
    Klasa przechowująca dane z wizytówek
    Argumenty:
    imię, nazwisko, nazwa firmy, stanowisko, adres e-mail

    __init__ konstruktor klasy, jakie zmienne przyjmuje, co z nimi robi
    __str__ definiuje jak klasa zachowuje się po dodaniu do fcji print()
    __repr__ co zostanie wyświetlone po wywołaniu samego obiektu tej klasy
            jeśli __str__ nie zostało zdefiniowane, to jest dziedziczone z __repr__
    """
    def __init__(self, full_name, business, position, email):
       self.name = full_name.split(" ")[0]
       self.surname = full_name.split(" ")[-1]
       self.business = business
       self.position = position
       self.email = email

    def __str__(self):
        return f"{self.name} {self.surname} {self.email}"

if __name__ == "__main__":
    """
    Fake Name Generator data:
    Christopher Corona, Rogers Food Stores, Personnel manager, ChristopherKCorona@rhyta.com
    Eugeniusz Chmielewski, Montana's Cookhouse, Military officer, EugeniuszChmielewski@jourrapide.com
    Iven Lesage, Awthentikz, Cutting and slicing machine operator, IvenLesage@armyspy.com
    Otávio Pinto Lima, BASCO, Illustrator, OtavioPintoLima@teleworm.us
    Melanie Freytag, Formula Grey, Cost engineer, MelanieFreytag@jourrapide.com
    """
    data = []
    data.append("Christopher Corona, Rogers Food Stores, Personnel manager, ChristopherKCorona@rhyta.com".split(", "))
    data.append("Eugeniusz Chmielewski, Montana's Cookhouse, Military officer, EugeniuszChmielewski@jourrapide.com".split(", "))
    data.append("Iven Lesage, Awthentikz, Cutting and slicing machine operator, IvenLesage@armyspy.com".split(", "))
    data.append("Otávio Pinto Lima, BASCO, Illustrator, OtavioPintoLima@teleworm.us".split(", "))
    data.append("Melanie Freytag, Formula Grey, Cost engineer, MelanieFreytag@jourrapide.com".split(", "))

    card_list = []
    for i in range (0,len(data)):
        card_list.append(BusinessCard(full_name = data[i][0], business = data[i][1], position = data[i][2], email = data[i][3]))
        print(card_list[i])