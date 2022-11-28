class ComAdvertisement: #Commercial Advertisement
    def __init__(self, picture, section):
        self.picture = picture
        self.section = section

class DeclAdvertisement: #Declassified Advertisement
    def __init__(self, price, pub_date, days, type):
        self.price = price
        self.publication_date = pub_date
        self.days = days
        self.type = type

class DeclAdvertisementVeh(DeclAdvertisement): #Declassified Advertisement Vehicle
    def __init__(self, price, pub_date, days, type, brand, model, year, color, km):
        super().__init__(self, price, pub_date, days, type)
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.km = km

class DeclAdvertisementViv(DeclAdvertisement): #Declassified Advertisement Vivienda
    def __init__(self, price, pub_date, days, type, m2, rooms, bathrooms):
        super().__init__(self, price, pub_date, days, type)
        self.m2 = m2
        self.rooms = rooms
        self.bathrooms = bathrooms

