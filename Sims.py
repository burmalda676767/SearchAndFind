import random

class Human:
    def __init__(self, name="Human", energy=100, mood=100, money=50):
        self.name = name
        self.energy = energy
        self.mood = mood
        self.money = money
        self.home = None # Поки персонаж без житла

    def info(self):
        if self.home:
            adress = self.home.adress
        else:
            adress = "Без житла"

        return f"{self.name}: Енергія: {self.energy} | Настрій: {self.mood} | Гроші: {self.money} | Дім: {adress}"

    def use(self, item):
        item.apply_to(self)

    def work(self):
        if self.energy < 30:
            print(f"{self.name} занадто втомлений(-а), щоб іти на роботу!")
            return

        self.energy -= 30
        self.mood -= random.randint(5, 10)
        self.money += random.randint(30, 59)

        print(f"{self.name} попрацював(-ла). Енергія: {self.energy}, гроші: {self.money}")

class Item:

    def __init__(self, name, energy=0, mood=0, price=0):
        self.name = name
        self.energy = energy
        self.mood = mood
        self.price = price

    def apply_to(self, human):
        if human.money < self.price:
            print(f"{human.name} не має грошей на {self.name}")
            return

        human.energy = self.energy
        human.mood = self.mood
        human.money -= self.price

        if human.energy > 100:
            human.energy = 100
        if human.mood > 100:
            human.energy = 100
        print(f"{human.name} використав(-ла) {self.name}. Енергія: {human.energy}, настрій: {human.mood}")

class House:
    MAX_RESIDENT = 4 # Атрибут класу - спільний для всіх будинків

    def __init__(self, adress):
        self.adress = adress
        self.resident = []
        self.items = []

    def add_resident(self, *args):
        for human in args:
            if len(self.resident) >= House.MAX_RESIDENT:
                print(f"У домі {self.adress} немає місця для {human.name}")
                return

            if human in self.resident:
                print(f"{human.name} вже живе у домі за адресою {self.adress}")
                continue

            self.resident.append(human)
            human.home = self # Зворотній звязок
            print(f"{human.name} заселився(-лась) у дім за адресою {self.adress}")

    def add_item(self, *args):
        for item in args:
            self.items.append(item)
            print(f"У дім за адресою {self.adress} додано: {item.name}")


    def print_resident(self):
        if self.resident != []:
            print(f"Мешканці дому {self.adress}: ")
            for human in self.resident:
                print(f"- {human.info()}")
        else:
            print(f"У домі {self.adress} поки ніхто не живе")

house = House("вул. Пітонівська, 7")

bed = Item("Ліжко", energy=50, mood=5)
fridge = Item("Холодильник", energy=20, mood=10, price=15)
tv = Item("Телевізор", energy=-5, mood=30)

house.add_item(bed, fridge, tv)

nick = Human("Nick")
kate = Human("Kate", energy=40, mood=60, money=110)
house.add_resident(nick, kate)

house.print_resident()

nick.work()
nick.use(bed)

kate.use(fridge)
kate.use(tv)

house.print_resident()