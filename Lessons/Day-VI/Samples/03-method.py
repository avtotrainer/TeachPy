# მეთოდები (Methods) — ქცევა კლასის შიგნით


class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")
