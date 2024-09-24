data = {}

def add_student():
    name,grade = input("Enter the name and grade of student seperated by commas: ").split(',')
    data['name'] = int(grade)
    print(data)

def average_grade():
    if not data:
        return 0
    total = sum(data.values())
    average = total/len(data)
    return average

def highest_grade():
    if not data:
        return 0
    high = max(data.values())
    return high

add_student()
add_student()
add_student()
print(average_grade())
print(highest_grade())

