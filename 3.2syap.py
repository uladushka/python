import os
import re
print(os.path.exists("C:/syap3.2.txt"))

with open("C:/syap3.2.txt", "w") as f:

     f.write("роза 5\n")
     f.write("тюльпан 12\n")
     f.write("гипсофилы 9\n")
     f.write("ромашка 3\n")
     f.write("пионы 10\n")
     f.write("гортензия 4\n")
     f.write("герберы 8\n")
     f.write("лилии 17\n")
     f.write("хризантемы 6\n")
     f.write("гибискус 6\n")

with open("C:/syap3.2.txt", "r") as f:
    data = f.read()
    print(data)
# товары дешевле 5
with open("C:/syap3.2.txt", "r") as f:
   print("товары дешевле 5: ")
   for line in f:
     name, price = line.strip().split(" ")
     if int(price) < 5:
        print(name, price)
   print()
# товары от 5 до 10
with open("C:/syap3.2.txt", "r") as f:
   print("товары от 5 до 10 : ")
   for line in f:
       name, price = line.strip().split(" ")
       if int(price) >= 5 and int(price) <= 10:
           print(name, price)
   print()
#товары дороже 10
with open("C:/syap3.2.txt", "r") as f:
    print("товары дороже 10: ")
    for line in f:
            name, price = line.strip().split(" ")
            if int(price) > 10:
                  print(name, price)
    print()

#вывод товара с минимальной стоимостью
with open("C:/syap3.2.txt", "r") as f:
    print("товар с минимальной стоимостью: ")

    min = 100
    for line in f:
        name, price = line.strip().split(" ")
        if int(price) < min:
            min = int(price)
            min_name = name

    print(min_name, min)

