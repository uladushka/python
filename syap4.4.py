class Vlada():
    zz = ""
    def __init__(self, day, month, year):
        print("появилась на свет Влада!")
        self.day = day
        self.month = month
        self.year = year
    def age(self):
        if self.month < 11:
            age = 2023 - self.year
        else:
            if self.month == 11 and self.day < 10:
                age = 2023 - self.year
            else:
                age = 2023 - self.year - 1
        print(age, "лет")

    @staticmethod
    def info():
        print("Влада дева по знаку зодиака")

    @classmethod
    def method_3(cls, new_zz):
        cls.zz = new_zz
        return cls.zz

v = Vlada(18, 9, 2004)
v.age()
v.info()
print(v.method_3("Влада больше не дева:("))