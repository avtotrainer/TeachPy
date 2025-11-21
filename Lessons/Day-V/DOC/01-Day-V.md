# Python – Day 5 (Advanced Data Manipulation)

Day 5-ში ვსწავლობთ:
- სტრიქონების დამატებით შესაძლებლობებს
- List Comprehension ტექნიკას
- თარიღებთან და დროთა მუშაობას

---

# 1. Advanced String Manipulation

## 1.1. სტრიქონის მეთოდები
```python
text = "hello world"

text.upper()     # "HELLO WORLD"
text.lower()     # "hello world"
text.title()     # "Hello World"
text.replace("world", "Python")
```

## 1.2. სტრიქონის დაჭრა (Slicing)
```python
name = "Python"
print(name[0:3])   # "Pyt"
print(name[2:])    # "thon"
print(name[:4])    # "Pyth"
```

## 1.3. გაყოფა და შეერთება
```python
words = "red,green,blue".split(",")   # ["red","green","blue"]
joined = "-".join(words)              # "red-green-blue"
```

---

# 2. List Comprehension

List comprehension არის მოკლე გზა ახალი სიის შესაქმნელად:

```python
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
```

ფილტრით:
```python
even = [x for x in numbers if x % 2 == 0]
```

სტრიქონების გარდაქმნა:
```python
names = ["nika", "ana", "giorgi"]
capitalized = [n.title() for n in names]
```

---

# 3. Working With Dates and Times

Python-ში თარიღებისთვის გამოიყენება `datetime` მოდული.

```python
from datetime import datetime

now = datetime.now()
print(now)
```

## 3.1. თარიღის ფორმატირება
```python
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))
```

## 3.2. სტრიქონიდან თარიღის მიღება
```python
dt = datetime.strptime("2024-02-25", "%Y-%m-%d")
```

## 3.3. დროის სხვაობა
```python
from datetime import timedelta

start = datetime.now()
end = start + timedelta(minutes=30)
```

---

# შეჯამება

- სტრიქონების მეთოდები → `upper`, `lower`, `split`, `join`, slicing  
- List Comprehension → სწრაფი ფილტრაცია და გარდაქმნა  
- Datetime → თარიღის/დროს წაკითხვა, ფორმატირება, დელტები  

Day 5 ამით დასრულებულია.

