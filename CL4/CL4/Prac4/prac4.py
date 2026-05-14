# Student Grade Calculation using MapReduce

from collections import defaultdict

# Mapper
def mapper(line):
    student_id, marks = line.split(",")
    return student_id, int(marks)


# Grade Function
def get_grade(total):

    if total >= 90:
        return "A"
    elif total >= 80:
        return "B"
    elif total >= 70:
        return "C"
    elif total >= 60:
        return "D"
    else:
        return "F"


# Input Data
data = [
    "101,40",
    "102,50",
    "101,55",
    "103,30",
    "102,45",
    "103,50"
]

mapped = []

# Map Phase
for line in data:
    mapped.append(mapper(line))

# Shuffle Phase
grouped = defaultdict(list)

for student_id, marks in mapped:
    grouped[student_id].append(marks)

# Reduce Phase
print("Final Grades:\n")

for student_id in sorted(grouped):

    total = sum(grouped[student_id])
    grade = get_grade(total)

    print(f"Student {student_id} = Grade {grade}")