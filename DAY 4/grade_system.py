marks = int(input("Enter Marks: "))

if marks >= 200:
  grade = "A+"
elif marks >= 180:
  grade = "A"
elif marks >= 90:
  grade = "B+"
else:
  grade = "C"

print("Grade:", grade)
