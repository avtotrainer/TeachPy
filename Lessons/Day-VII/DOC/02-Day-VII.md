# Python – Day VII (JSON, Debugging, Basic AI Libraries)

Day VII-ში ვსწავლობთ პრაქტიკულად მნიშვნელოვან თემებს:
- JSON ფაილებთან მუშაობა  
- შეცდომების მოძებნა და მართვა (Debugging)  
- საბაზისო AI/Science ბიბლიოთეკები (NumPy, NLTK)

ეს დღე არის საბოლოო ეტაპი 7-დღიან კურსში.

---

# 1. JSON (JavaScript Object Notation)

JSON არის მონაცემების შენახვისა და გადაცემის ტექსტური ფორმატი.

---

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

---

## 1.2. JSON წაკითხვა ფაილიდან

```python
import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
```

---

# 2. Debugging — შეცდომების პოვნა და მართვა

---

## 2.1. print-based debugging
ყველაზე მარტივი გზა:

```python
value = 10
print("DEBUG value =", value)
```

---

##

