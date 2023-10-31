class Stationery:
    title = ""
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Pen class Stationery")

class Pencil(Stationery):
    def draw(self):
        print("Pencil class Stationery")

class Handle(Stationery):
    def draw(self):
        print("Handle class Stationery")

obj = Stationery()
obj1 = Pen()
obj2 = Pencil()
obj3 = Handle()
obj.draw()
obj1.draw()
obj2.draw()
obj3.draw()