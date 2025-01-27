marks = {
    "som": 50,
    "kiran": 60,
    "nabin": 90,
    "shankar": 80
}
studentwith80marks = []
for name, mark in marks.items():
   if mark >= 80:
        studentwith80marks.append(name)
        print(studentwith80marks)