# Python – Day 4 (Functions, Modules, File Handling)

Day 4-ში ვსწავლობთ:
- ფუნქციებს (Functions)
- მოდულებს (Modules)
- ფაილებთან მუშაობას (File Handling)

---

# 1. Functions (ფუნქციები)

ფუნქცია არის კოდის ბლოკი, რომელიც ასრულებს კონკრეტულ მოქმედებას.

```python
def greet():
    print("გამარჯობა!")
```

ფუნქციის გამოძახება:

```python
greet()
```


## ფუნქცია პარამეტრებით
```python
def greet(name):
    print("გამარჯობა,", name)
```

გამოძახება:
```python
greet("Nika")
```


## ფუნქცია დაბრუნებული მნიშვნელობით (return)
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

მოდული არის Python ფაილი, სადაც ფუნქციები და კოდი ინახება.

მოდულის გამოყენება:

```python
import math
print(math.sqrt(16))
```

კონკრეტული ფუნქციის იმპორტი:
```python
from math import sqrt
print(sqrt(25))
```

---

# 3. საკუთარი მოდულის შექმნა

ვთქვათ, გვაქვს ფაილი:

`helpers.py`  
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

## ფაილის გახსნა და წაკითხვა
```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

## ფაილის ჩაწერა
```python
file = open("output.txt", "w")
file.write("Hello file!")
file.close()
```

---

# 5. with — უსაფრთხო ფაილის გახსნა

```python
with open("data.txt", "r") as file:
    text = file.read()
```

`with` ავტომატურად ხურავს ფაილს.

---

# შეჯამება

- **Function** = კოდის ბლოკი, რომელსაც შეუძლია პარამეტრების მიღება და შედეგის დაბრუნება  
- **Module** = Python ფაილი, რომელსაც სხვა ფაილში ვიყენებთ  
- **File Handling** = ფაილების კითხვა/ჩაწერა `open()` ან `with open()` კონსტრუქციით  

Day 4 ამით დასრულებულია.

