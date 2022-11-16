class Cleint:
    def __init__(self, name, sername, city, balans):
        self.name = name
        self.sername = sername
        self.city = city
        self.balans = balans

    def __str__(self):
        return f'{self.name} {self.sername}. {self.city}. Баланс:{self.balans}руб.'
client = Cleint('Иван', 'Петров', 'Москва', 50)
print(client)