import csv

def write_students_to_csv(filename:str,student_list:list):
    with open(filename,mode='w',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=student_list[0].keys())
        writer.writeheader()
        writer.writerows(student_list)
def read_csv_and_print(filename:str):
    with open(filename,mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    students = [
        {'ID': 1, 'Name': 'Alice', 'Age': 20, 'Grade': 'A'},
        {'ID': 2, 'Name': 'Bob', 'Age': 21, 'Grade': 'B'},
        {'ID': 3, 'Name': 'Charlie', 'Age': 22, 'Grade': 'C'},
        {'ID': 4, 'Name': 'David', 'Age': 23, 'Grade': 'A'},
        {'ID': 5, 'Name': 'Eva', 'Age': 20, 'Grade': 'B'}
    ]

write_students_to_csv('students.csv',students)
read_csv_and_print('students.csv')