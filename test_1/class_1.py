class Human:
    def __init__(self, name="Зина", year=2000, height=200, weight=87):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def hi(self):
        print(f"Привет! Меня зовут {self.name}. Мне {2023 - self.year}, у меня рост {self.height} сантиметров, вешу я {self.weight} киллограм")

    def school(self):
        if 2023 - self.year <= 18:
            print("Я хожу в школу, плак-плак.")
        else:
            print("Я хожу на работу, плак-плак.")


a = Human("Саша", 1000, 100, 3678)
b = Human("Гена", 2005, 245, 45)
c = Human()
a.hi()
b.hi()
c.hi()
a.school()
b.school()
c.school()