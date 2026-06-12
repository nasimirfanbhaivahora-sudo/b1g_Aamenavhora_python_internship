students = [
    {"Name": "Aamena", "Marks": 85},
    {"Name": "Ruhin", "Marks": 92},
    {"Name": "Zeba", "Marks": 78}
]

search_name = input("Enter student name to search: ")
found = False

for student in students:
    
    if student["Name"].lower() == search_name.lower():
        print("Student Found")
        print(f"Marks: {student['Marks']}")
        found = True
        break 

if not found:
    print("Student Not Found")