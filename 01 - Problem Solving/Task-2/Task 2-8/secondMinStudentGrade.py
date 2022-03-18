students = []

countStudents = int(input("How many student?: "))

for i in range(countStudents):
    name = input("Enter A Name: ")
    score = float(input("Enter a grade: "))
    students.append([score, name])

students.sort()
b = [i for i in students if i[0] != students[0][0]]
c = [j for j in b if j[0] == b[0][0]]

c.sort(key=lambda x: x[1])
for i in range(len(c)):
    print(c[i][1])