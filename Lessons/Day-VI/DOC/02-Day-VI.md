# Python – Day VI (Object-Oriented Programming — OOP)

Day VI-ში ვსწავლობთ ობიექტურ პროგრამირებას:
- კლასები  
- ობიექტები  
- ატრიბუტები  
- მეთოდები  
- კონსტრუქტორი (__init__)

OOP გვაძლევს უფრო ორგანიზებულ, მოდულარულ და მასშტაბურ კოდს.

---

# 1. What is OOP?

OOP (Object-Oriented Programming) წარმოადგენს პროგრამირების სტილს,  
სადაც ყველაფერი ობიექტებად არის წარმოდგენილი.

- **Class** — შაბლონი  
- **Object** — ამ შაბლონის კონკრეტული მაგალითი

---

# 2. Creating a Class

```python
class Student:
    pass
```

ეს არის ცარიელი კლასი.

---

# 3. Constructor (__init__) და Attributes

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `__init__` — კონსტრუქტორი  
- `self` — მიუთითებს კონკრეტულ ობიექტზე  

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

    def greet(

