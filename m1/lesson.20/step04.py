import json


student_data = {
    "name": "Алиса",
    "age": 25,
    "height": 1.68,
    "is_student": True,
    "middle_name": None,
    "skills": ["Python", "SQL", "Git"],
    "address": {
        "city": "Москва",
        "street": "Baker Street",
        "house_number": 221,
    }
}

print(student_data)
print(type(student_data))


with open("student_data_1.json", "w", encoding="utf-8") as f:
    json.dump(student_data, f, ensure_ascii=False, indent=4)

print('Данные сохранены')


# json_str = json.dumps(student_data)
# print(json_str)
# print(type(json_str))
#
# print("*" * 50)
#
# python_data = json.loads(json_str)
# print(python_data)
# print(python_data.get("name"))
# print(type(python_data))