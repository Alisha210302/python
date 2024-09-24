
def get_integer_ip():
        try:
            n = int(input("Enter the input as integer: "))
            print(n)
        except ValueError:
            print("Invalid entry")

def get_element_from_list():
        try:
            lst = [1,2,3,4,5,6]
            i = int(input("Enter the index of number which you want: "))
            return print(lst[i])
        except IndexError:
            print("Invalid index")
        except TypeError:
             print("please enter valid text")
        finally:
            print("Successful execution")

def divide_numbers(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Invalid denominator")


get_integer_ip()
print(get_element_from_list())
divide_numbers(4,2)