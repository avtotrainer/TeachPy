# ✔️ Day 5 → Concept 4

## **Datetime — თარიღებთან და დროთი მუშაობა**

from datetime import datetime


my_datetime = datetime.now()
print(my_datetime)

after_30_min = my_datetime + datetime.timedelta(minutes=30)
print(after_30_min)
