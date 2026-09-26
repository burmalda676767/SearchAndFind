import random


class Human:
    def __init__(self, name="Human", energy=100, mood=100, money=50):
        self.name = name
        self.energy = energy
        self.mood = mood
        self.money = money
        self.home = None   # Поки персонаж без житла
        self.job = None    # Поки персонаж без роботи

    def info(self):
        adress = self.home.adress if self.home else "Без житла"
        job_title = self.job.title if self.job else "Безробітний(-а)"

        return (f"{self.name}: Енергія: {self.energy} | Настрій: {self.mood} | "
                f"Гроші: {self.money} | Дім: {adress} | Робота: {job_title}")

    def use(self, item):
        item.apply_to(self)

    def get_job(self, job):
        self.job = job
        job.add_employee(self)
        print(f"{self.name} влаштувався(-лась) на посаду \"{job.title}\"")

    def work(self):
        if self.job is None:
            print(f"{self.name} ще ніде не працює!")
            return

        self.job.work(self)  # комунікація: Human делегує роботу об'єкту Job


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

        human.energy = min(100, human.energy + self.energy)
        human.mood = min(100, human.mood + self.mood)
        human.money -= self.price

        print(f"{human.name} використав(-ла) {self.name}. Енергія: {human.energy}, настрій: {human.mood}")


class House:
    MAX_RESIDENT = 4  # Атрибут класу - спільний для всіх будинків

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
            human.home = self  # Зворотній звязок
            print(f"{human.name} заселився(-лась) у дім за адресою {self.adress}")

    def add_item(self, *args):
        for item in args:
            self.items.append(item)
            print(f"У дім за адресою {self.adress} додано: {item.name}")

    def print_resident(self):
        if self.resident:
            print(f"Мешканці дому {self.adress}: ")
            for human in self.resident:
                print(f"- {human.info()}")
        else:
            print(f"У домі {self.adress} поки ніхто не живе")


class Job:
    """Новий клас: робоче місце. Спілкується з Human через метод work()."""

    def __init__(self, title, energy_cost=30, mood_cost=(5, 10), salary_range=(30, 59)):
        self.title = title
        self.energy_cost = energy_cost
        self.mood_cost = mood_cost
        self.salary_range = salary_range
        self.employees = []  # зворотній звязок: хто тут працює

    def add_employee(self, human):
        if human not in self.employees:
            self.employees.append(human)

    def work(self, human):
        if human.energy < self.energy_cost:
            print(f"{human.name} занадто втомлений(-а), щоб працювати на посаді \"{self.title}\"!")
            return

        human.energy -= self.energy_cost
        human.mood = max(0, human.mood - random.randint(*self.mood_cost))
        salary = random.randint(*self.salary_range)
        human.money += salary

        print(f"{human.name} попрацював(-ла) на посаді \"{self.title}\" і отримав(-ла) {salary} грн. "
              f"Енергія: {human.energy}, гроші: {human.money}")

    def print_employees(self):
        if self.employees:
            print(f"Працівники посади \"{self.title}\":")
            for human in self.employees:
                print(f"- {human.name}")
        else:
            print(f"На посаді \"{self.title}\" поки ніхто не працює")


# --- Демонстрація ---

house = House("вул. Пітонівська, 7")

bed = Item("Ліжко", energy=50, mood=5)
fridge = Item("Холодильник", energy=20, mood=10, price=15)
tv = Item("Телевізор", energy=-5, mood=30)

house.add_item(bed, fridge, tv)

nick = Human("Nick")
kate = Human("Kate", energy=40, mood=60, money=110)
house.add_resident(nick, kate)

house.print_resident()

programmer_job = Job("Програміст", energy_cost=30, mood_cost=(5, 10), salary_range=(30, 59))
barista_job = Job("Бариста", energy_cost=15, mood_cost=(2, 5), salary_range=(15, 25))

nick.get_job(programmer_job)
kate.get_job(barista_job)

nick.work()
nick.use(bed)

kate.work()
kate.use(fridge)
kate.use(tv)

programmer_job.print_employees()
house.print_resident()
