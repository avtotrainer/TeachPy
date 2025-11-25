# Python – Day III (Data Structures)

Day III-ში ვსწავლობთ Python-ის ოთხ ძირითად მონაცემთა სტრუქტურას:
- List
- Tuple
- Dictionary
- Set

ყველა მათგანი განსხვავებული უპირატესობებით და გამოყენებით გამოირჩევა.

---

# 1. List (სია)

სია არის ელემენტების კოლექცია, რომელიც **შეიძლება შეიცვალოს**.

```python
colors = ["red", "green", "blue"]
print(colors[1])   # green
```

## ძირითადი ოპერაციები:
```python
colors.append("yellow")   # დამატება
colors.remove("green")    # წაშლა
length = len(colors)      # სიგრძე
```

---

# 2. Tuple (ტაპლი)

Tuple არის სიის მსგავსი, მაგრამ **შეუცვლელი**.

```python
sizes = (38, 39, 40)
print(sizes[0])
```

ტაპლი გამოიყენება მაშინ, როცა მონაცემი უცვლელი უნდა დარჩეს.

---

# 3. Dictionary (ლექსიკონი)

ლექსიკონი ინახავს მონაცემებს **key : value** წყვილებით.

```python
student = {
    "name": "Nika",
    "age": 12,
    "grade": 6
}

print(student["name"])
```

## მნიშვნელობის შეცვლა ან დამატება
```python
student["age"] = 13
student["school"] = "Public School #1"
```

## წესები:
- key-ები უნიკალურია  
- key უნდა იყოს უცვლადი ტიპი (str, int, tuple…)  
- value შეიძლება იყოს ნებისმიერი (str, list, dict…)  

---

# 4. Set (მრავალობა)

Set ინახავს **მხოლოდ უნიკალურ** ელემენტებს (დუბლიკატები ავტომატურად იშლება).

```python
nums = {1, 2, 2, 3, 3}
print(nums)   # {1, 2, 3}
```

## ძირითადი ოპერაციები:
```python
nums.add(10)
nums.remove(2)
```

Set გამოიყენება:
- დუბლიკატების მოცილებისთვის  
- სწრაფი შემოწმებისთვის (`if x in set:`)  
- უნიკალური წევრების მოძიებისთვის  

---

# Day III — შეჯამება

- **List** → შეცვლადი კოლექცია  
- **Tuple** → უცვლელი კოლექცია  
- **Dictionary** → key/value მონაცემები  
- **Set** → უნიკალური ელემენტები  

Day III ამით დასრულებულია.

