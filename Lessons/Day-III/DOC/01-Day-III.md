# Python – Day 3 (Data Structures)

Day 3-ში ვსწავლობთ Python-ის ოთხ ძირითად სტრუქტურას:
- List
- Tuple
- Dictionary
- Set

---

## 1. List (სია)
სია არის ელემენტების კოლექცია, რომელიც შეიძლება შეიცვალოს.

```python
colors = ["red", "green", "blue"]
print(colors[1])   # green
```

### მნიშვნელოვანი ოპერაციები:
```python
colors.append("yellow")
colors.remove("green")
length = len(colors)
```

---

## 2. Tuple (ტაპლი)
Tuple არის სიის მსგავსი, მაგრამ **შეუცვლელი**.

```python
sizes = (40, 41, 42)
print(sizes[0])
```

ტაპლი უსაფრთხოა მაშინ, როცა მონაცემი არ უნდა შეიცვალოს.

---

## 3. Dictionary (ლექსიკონი)
ლექსიკონში მონაცემები ინახება **key : value** წყვილებით.

```python
student = {
    "name": "Nika",
    "age": 12,
    "grade": 6
}
print(student["name"])
```

### ოპერაციები:
```python
student["age"] = 13
student["school"] = "Public School #1"
```

---

## 4. Set (მრავალობა)
Set ინახავს **მხოლოდ უნიკალურ** ელემენტებს (არ მეორდება).

```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)   # {1, 2, 3}
```

### ოპერაციები:
```python
unique_numbers.add(4)
unique_numbers.remove(2)
```

---

# შეჯამება
- **List** – შეცვლადი ნუსხა  
- **Tuple** – შეუცვლელი ნუსხა  
- **Dictionary** – ключ–მნიშვნელობა  
- **Set** – უნიკალური ელემენტები  

ეს ოთხი სტრუქტურა არის Python-ის ყველა სერიოზული პროგრამის საფუძველი.

