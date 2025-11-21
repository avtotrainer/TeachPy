# Python – Day 6 (OOP — Object-Oriented Programming)

Day 6-ში ვსწავლობთ:
- ობიექტურ პროგრამირებას  
- კლასებს  
- ობიექტებს  
- ატრიბუტებს და მეთოდებს  

---

# 1. What is OOP?

OOP (Object-Oriented Programming) არის პროგრამირების სტილი,  
სადაც ყველაფერი წარმოდგენილია ობიექტებად, რომლებიც ერთმანეთთან ურთიერთობენ.

**კლასი** = შაბლონი  
**ობიექტი** = ამ შაბლონის კონკრეტული ”ნიმუში”

მაგალითად:

- „მოსწავლე“ არის კლასი  
- კონკრეტული მოსწავლე (ნიკა, ანა) არის ობიექტი

---

# 2. Creating a Class

```python
class Student:
    pass
```

ეს არის ცარიელი კლასი.  

---

# 3. Class Attributes (ატრიბუტები)

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `__init__` — კონსტრუქტორი  
- `self` — ობიექტის თავს გულისხმობს  

ობიექტის შექმნა:

```python
s1 = Student("Nika", 12)
print(s1.name)
print(s1.age)
```

---

# 4. Methods (მეთოდები)

მეთოდები არის ფუნქციები კლასის შიგნით.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("გამარჯობა, მე ვარ", self.name)
```

გამოძახება:

```python
s = Student("Ana")
s.greet()
```

---

# 5. Changing Attributes

```python
s = Student("Nika", 12)
s.age = 13
print(s.age)
```

---

# 6. Class Example — Rectangle

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

გამოყენება:

```python
r = Rectangle(5, 10)
print(r.area())
print(r.perimeter())
```

---

# შეჯამება

- **Class** = ობიექტის შაბლონი  
- **Object** = კლასის გამოძახება  
- **Attributes** = ობიექტის მონაცემები  
- **Methods** = ობიექტის ფუნქციები  
- **__init__** = კონსტრუქტორი  

Day 6 ამით დასრულებულია.
