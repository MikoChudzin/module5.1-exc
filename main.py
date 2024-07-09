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
    
    def __gt__(self,other):
        return self.surname > other.surname
    
    def __lt__(self,other):
        return self.surname < other.surname
    
    def __eq__(self, other):
        return (
        self.name == other.name and
        self.surname == other.surname and
        self.business == other.business and
        self.position == other.position and
        self.email == other.email
        )

    """
    # funkcjonalnie to samo co powyżej
    def __eq__(self, other):
    return all(
        (
            self.name == other.name,
            self.surname == other.surname,
            self.business == other.business,
            self.position == other.position,
            self.email == other.email
        )
    )
    """

    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname}, {self.position} pod adresem {self.email}")

    @property
    def full_name_length(self):
        return len(self.name + self.surname) + 1


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
        # ćwiczenie 1: wylistuj wszystkie posiadane wizytówki, ćwiczenie 2: ulepsz metodę printowania poprzez zdefiniowanie __str__
        #print(card_list[i])

    by_name = sorted(card_list, key=lambda card: card.name)
    by_surname = sorted(card_list, key=lambda card: card.surname)
    by_mail = sorted(card_list, key=lambda card: card.email)
    sorted_cards = {"Po imieniu" : by_name, "Po nazwisku" : by_surname, "Po adresie" : by_mail}

    # ćwiczenie 3: wyświetl wizytówki posortowane po kolei: po imieniu, po nazwisku, po adresie email
    # for key,value in sorted_cards.items():
    #     print(f"{key}: {value[0]}, {value[1]}, {value[2]}")

    # ćwiczenie 4: dodaj do klasy metodę contact(), która wyświetli
    # “Kontaktuję się z …”, a na końcu wyświetli imię, nazwisko, stanowisko i adres e-mail osoby, z którą chcemy się skontaktować.
    # card_list[3].contact()

    # ćwiczenie 5: zdefiniuj dynamiczny atrybut (używając @property), który będzie zwracał sumę długości imienia i nazwiska oddzielonych spacją
    #print(card_list[2].full_name_length)