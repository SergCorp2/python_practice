class Cleint:

    def __init__(self, name, sername, city, balans):
        self.name = name
        self.sername = sername
        self.city = city
        self.balans = balans

    def __str__(self):
        return f'{self.name}  {self.sername}. {self.city}. Баланс:{self.balans}руб.'

    def get_guests(self):
        return f'{self.name}{self.sername}, г.{self.city}'

client = Cleint('Иван ', 'Петров', 'Москва', 50)
client_1 = Cleint('Иван ', 'Петров', 'Электросталь', 55)
client_2 = Cleint('Иван ', 'Иванов', 'Кострома', 100)
client_3 = Cleint('Петр ', 'Петров', 'Ярославль', 150)
client_4 = Cleint('Сидор ', 'Петров', 'Вологда', 200)

guest_list = [client_1, client_2, client_3, client_4]

for guest in guest_list:
    print(guest.get_guests())

# print(client)