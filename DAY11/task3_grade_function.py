def get_grade(marks):
    if marks >= 97:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(f"Marks 98 -> Grade: {get_grade(98)}")
print(f"Marks 86 -> Grade: {get_grade(86)}")
print(f"Marks 68 -> Grade: {get_grade(68)}")
