with open("f1.txt", "w") as f1:
    while True :
        line = input("введите строку: ")
        if line == "":
          break
        f1.write(line+"\n")

with open("f1.txt", "r") as f1, open("f2.txt", "w") as f2:
    for line in f1:
        if line.startswith("A") or line.startswith("a"):
            f2.write(line)

with open("f2.txt", "r") as f2:
    word = 0
    for line in f2:
        words = line.split()
        word += len(words)

print("количество слов во втором файле: ", word)