# კონსტრუქტორი (init) და ატრიბუტები


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class teacher(Person):  # classname:
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


t = teacher("Bob", 30, "Math")

print(t.name)
print(t.age)
prppint(t.subject)
