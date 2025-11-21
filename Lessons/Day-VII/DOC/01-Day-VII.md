# Python – Day 7 (Practical Python & AI Integration)

Day 7-ში ვსწავლობთ:
- JSON ფაილებთან მუშაობას  
- მარტივ შეცდომების მოძებნას (Debugging)  
- AI/Scientific ბიბლიოთეკების საბაზისო გამოყენებას  
  (NumPy, NLTK — მარტივი მაგალითებით)

---

# 1. JSON (JavaScript Object Notation)

JSON არის მონაცემთა გაცვლის მარტივი ფორმატი.

## 1.1. JSON ჩაწერა ფაილში

```python
import json

student = {
    "name": "Nika",
    "age": 12,
    "grade": 6
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

## 1.2. JSON წაკითხვა ფაილიდან

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
```

---

# 2. Debugging — შეცდომების პოვნა და გასწორება

## 2.1. print-based debugging
სწრაფი მეთოდი:

```python
value = 10
print("DEBUG value =", value)
```

## 2.2. try/except-ის გამოყენება

```python
try:
    number = int("abc")
except ValueError as e:
    print("შეცდომა:", e)
```

## 2.3. ტიპიური შეცდომები:
- TypeError  
- ValueError  
- KeyError  
- IndexError  

---

# 3. NumPy (AI/Science ბიბლიოთეკის საფუძვლები)

NumPy საშუალებას გაძლევს იმუშაო მათემატიკურ მასივებთან.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr * 2)
```

---

# 4. NLTK (Natural Language Processing — საბაზისო მაგალითი)

NLTK გამოიყენება ტექსტური ანალიზისთვის.

```python
import nltk
from nltk.tokenize import word_tokenize

text = "Hello, this is Python."
tokens = word_tokenize(text)
print(tokens)
```

(შენიშვნა: NLTK მოითხოვს დამატებით რესურსებს დათვირთვას.)

---

# შეჯამება

Day 7-ის შემდეგ სტუდენტი იცნობს:

- JSON ფაილების ჩაწერას და წაკითხვას  
- შეცდომების პოვნასა და მართვას  
- საბაზისო AI ინსტრუმენტებს (NumPy, NLTK)  

ამით სრულდება Python-ის 7-დღიანი საბაზისო კურსი.

