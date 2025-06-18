# This is business logic layer
from data.students_repository import get_students

def calculate_average():
    students = get_students()

    total_sum = 0
    count = 0

    for student in students:
        total_sum+=student['grade']
        count+=1

    return total_sum/count