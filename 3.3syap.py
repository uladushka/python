with open("C:/предметы.txt", "w") as file:
    file.write("Информатика: 100(л) 50(пр) 20(лаб)\n")
    file.write("Физика: 30(л) 10(лаб)\n")
    file.write("Физкультура: 30(пр)\n")

with open("C:/предметы.txt", "r") as file:

    subjects = {}


    for line in file:

        subject, classes = line.strip().split(": ")

        classes = classes.split(" ")

        all = 0

        for c in classes:

            count, tc = c.split("(")

            tc = tc[:-1]

            all += int(count)

        subjects[subject] = all


print(subjects)