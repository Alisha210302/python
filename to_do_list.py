'''
Assignment 9 : Write a program that implements a basic to-do list where users can add, remove, and view tasks.
Input:
Allow the user to add tasks to the to-do list.
Allow the user to remove tasks by specifying the task name.
Allow the user to view the current list of tasks.
Logic:
Use a list to store the tasks.
Implement a loop that continuously prompts the user to choose an action (add, remove, view, or exit).
Output:
Display the updated to-do list after each operation.
'''
n=1
lst = []
while n:
    choice = int(input("Enter the task you want to perform:\n 1.Add \n 2.Remove \n 3.View \n"))

    if choice == 1:
        add = input("Enter the task you want to add: ")
        lst.append(add)
        print(lst)
    elif choice == 2:
        remove = input("Enter the task you want to remove: ")
        lst.remove(remove)
        print(lst)
    elif choice == 3:
        print(lst)
    else:
        pass
    n = int(input("press 1 if you want to continue or 0 if you want to exit"))


