class Example:
    s1 = 5
    s2 = 6

    def __init__(self):
        self.d1 = 7
        self.d2 = 3

    def _method1(self):
        a = 10
        print(a)

    def _method2(self):
        return self.s1 + self.s2

    def _method3(self):
        return self.d1 ** self.d2


ex = Example()
ex._method1()
print(ex._method2())
print(ex._method3())
print(ex.s1)