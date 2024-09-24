secret_number = 21
i = 1
while i<=10:
    number = int(input("Enter the secret number: "))

    if number == secret_number:
        print("you guessed it correct")
        break
    else:
        print("wrong guess")
    i+=1
print("Your guessing chances are over")