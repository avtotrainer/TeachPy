# ობიექტის ატრიბუტების შეცვლა (Modify Attributes)


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject


tch = Teacher("Bob", 30, "Math")

print(tch.name)
print(tch.age)
print(tch.subject)

tch.name = "John"
tch.age = 25
tch.subject = "English"

print(tch.name)
print(tch.age)
print(tch.subject)

print(tch.__dict__)

print(tch.__dict__["name"])
print(tch.__dict__["age"])
print(tch.__dict__["subject"])

print(tch.name)
print(tch.age)
print(tch.subject)
