# Python – Day V (Advanced Data Manipulation)

Day V-ში ვსწავლობთ:
- სტრიქონების გაფართოებულ შესაძლებლობებს  
- List Comprehension ტექნიკას  
- თარიღებთან და დროთა მუშაობას (datetime)

---

# 1. Advanced String Manipulation

სტრიქონები Python-ში ძალიან მოქნილი და მასიურად გამოყენებადი სტრუქტურაა.

---

## 1.1. ძირითადი მეთოდები

```python
text = "hello world"

text.upper()     # "HELLO WORLD"
text.lower()     # "hello world"
text.title()     # "Hello World"
text.replace("world", "Python")
```

---

## 1.2. slicing — სტრიქონის დაჭრა

```python
name = "Python"
print(name[0:3])   # "Pyt"
print(name[2:])    # "thon"
print(name[:4])    # "Pyth"
```

---

## 1.3. split და join

```python
colors = "red,green,blue".split(",")   # ["red","green","blue"]
joined = "-".join(colors)              # "red-green-blue"
```

---

# 2. List Comprehension

List comprehension არის Python-ის სუპერ-მძლავრი ინსტრუმენტი  
სიების სწრაფი შექმნისთვის, ფილტრაციისთვის და გარდაქმნისთვის.

---

## 2.1. მარტივი მაგალითი

```python
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
```

---

## 2.2. ფილტრი:

```python
even = [x for x in numbers if x % 2 == 0]
```

---

## 2.3. სტრიქონების გარდაქმნა

```python
names = ["nika", "ana", "giorgi"]
capitalized = [n.title() for n in names]
```

---

# 3. Working With Datetime

Python-ში თარიღებთან და დროსთან სამუშაოდ გამოიყენება `datetime` მოდული.

```python
from datetime import datetime
now = datetime.now()
print(now)
```

---

## 3.1. თარიღის ფორმატირება

```python
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))
```

---

## 3.2. ტექსტიდან თარიღის მიღება

```python
dt = datetime.strptime("2024-02-15", "%Y-%m-%d")
```

---

## 3.3. დროის სხვაობა

