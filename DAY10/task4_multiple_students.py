students = [
    {"Name": "Aamena", "Marks": 85},
    {"Name": "Ruhin", "Marks": 92},
    {"Name": "Zeba", "Marks": 78}
]


for student in students:
    name = student["Name"]
    marks = student["Marks"]
    print(f"Student: {name}, Marks: {marks}")
