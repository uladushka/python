class Country:
    def __init__(self, capital, area, population):
        self.capital = capital
        self.area = area
        self.population = population

country = [
    Country("Canada", 9984670, 38250000),
    Country("China", 9598962, 1412000000),
    Country("Mexico", 1972550, 126700000),
    Country("Belarus", 207600, 9340000),
    Country("Germany", 357385, 83200000),
    Country("France", 547030, 67750000),
    Country("Russia", 17125191, 143300000)
]

def country_area(country, b):
    result = []
    for c in country:
        if c.area <= b:
            result.append(c)
    return result
try:
    b = int(input("Введите площадь территории, которая не должна превосходить: "))
    if b < 0:
        print("площадь не может быть отрицательной")
except ValueError:
    print("ошибка ввода!")

cc = country_area(country, b)
for c in cc:
    print(c.capital)

def country_population(country, d):
    result = []
    for p in country:
        if p.population >= d:
            result.append(p)
    return result
try:
    d = int(input("Введите численность населения, которая не должна превосходить: "))
    if d < 0:
        print("численность не может быть отрицательной!")
except ValueError:
    print("ошибка ввода!")

pp = country_population(country, d)
for p in pp:
    print(p.capital)