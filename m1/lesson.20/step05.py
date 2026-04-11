import json


with open("student_data_1.json", "r", encoding="utf-8") as f:
    student_data = json.load(f)

print('Наши данные')

print(student_data)
print(student_data.get("name"))
print(type(student_data))