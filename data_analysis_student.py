def main():
    students = []

    while True:
        name = input("Enter students name or if you want to exit enter 'exit': ")
        if name == "exit":
            break
        age = int(input("Enter the age of student: "))
        score1 = int(input("Enter the score1: "))
        score2 = int(input("Enter the score2: "))
        score3 = int(input("Enter the score3: "))

        student_data = (name,age,score1,score2,score3)
        students.append(student_data)

    updated_students = []
    for student in students:
        name,age,score1,score2,score3 = student
        average = (score1+score2+score3)/3
        up_student = (name,age,score1,score2,score3,average)
        updated_students.append(up_student)

    highest_student = max(updated_students,key = lambda x:x[-1])
    print(f"Highest score is {highest_student[-1]:.2f} with name {highest_student[0]}")

    min_student =  float(input("enter the minimun average score: "))
    for student in updated_students:
        if student[-1]>=min_student:
            print(f"{student[0]} with average score of {student[-1]:.2f}")

if __name__ == "__main__":
    main()