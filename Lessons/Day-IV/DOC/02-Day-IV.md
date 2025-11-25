# Python – Day IV (Functions, Modules, File Handling)

Day IV-ში ვსწავლობთ სამი ტიპის ბირთვულ ინსტრუმენტს:
- ფუნქციები (Functions)
- მოდულები (Modules)
- ფაილებთან მუშაობა (File Handling)

---

# 1. Functions (ფუნქციები)

ფუნქცია არის კოდის ბლოკი, რომელიც ასრულებს კონკრეტულ ამოცანას.

## 1.1. მარტივი ფუნქცია

```python
def greet():
    print("გამარჯობა!")
```

გამოძახება:

```python
greet()
```

---

## 1.2. ფუნქცია პარამეტრებით

```python
def greet(name):
    print("გამარჯობა,", name)
```

გამოძახება:

```python
greet("Nika")
```

---

## 1.3. ფუნქცია დაბრუნებული მნიშვნელობით

```python
def add(a, b):
    return a + b
```

გამოყენება:

```python
result = add(5, 3)
print(result)
```

---

# 2. Modules (მოდულები)

მოდული არის Python ფაილი, რომლის ფუნქციებიც შეგვიძლია სხვაგან გამოვიყენოთ.

## 2.1. სტანდარტული მოდულის იმპორტი

```python
import math
print(math.sqrt(16))
```

## 2.2. კონკრეტული ფუნქციის იმპორტი

```python
from math import sqrt
print(sqrt(25))
```

---

# 3. საკუთარი მოდულის შექმნა

ფაილი: **helpers.py**

```python
def square(x):
    return x * x
```

გამოყენება სხვა ფაილში:

```python
import helpers
print(helpers.square(4))
```

ან:

```python
from helpers import square
print(square(4))
```

---

# 4. File Handling (ფაილებთან მუშაობა)

ფაილის წაკითხვა და ჩაწერა Python-ში ხდება `open()` ფუნქციით.

## 4.1. ფაილის გახსნა და წაკითხვა

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

## 4.2. ფაილის ჩაწერა

```python
file = open("output.txt", "w")
file.write("Hello file!")
file.close()
```

---

# 5. with — უსაფრთხო ფაილის გახსნა

`with` ავტომატურად ხურავს ფაილს.

```python
with open("data.txt", "r") as file:
    text = file.read()
```

---

# Day IV — შეჯამება

- **Function** = კოდის ბლოკი, რომელსაც აქვს პარამეტრები და დაბრუნებული მნიშვნელობა  
- **Module** = Python ფაილი, რომლის იმპორტიც შეგვიძლია  
- **File Handling** = ფაილების წაკითხვა/ჩაწერა `open()` ან `with open()` ფორმატით  

Day IV ამით დასრულებულია.

