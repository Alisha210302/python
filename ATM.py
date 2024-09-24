'''
Input: Prompt the user to enter their account balance and the amount they wish to withdraw.
Logic:
Check if the withdrawal amount is greater than the account balance. If so, display an error message.
If the withdrawal amount is valid, subtract it from the balance.
Ensure the withdrawal amount is a multiple of 10 (as ATMs typically dispense money in multiples of 10).
Output:
Display the remaining balance if the withdrawal is successful.
If not, display an appropriate error message (e.g., "Insufficient balance" or "Amount must be a multiple of 10").
Check if user wishes to withdraw more money, else exit
'''
n = 1
while n:
    account_balance = int(input("Enter the account balance: "))
    amount_for_withdrawal = int(input("Enter the amount to withdraw: "))
    if amount_for_withdrawal %10 == 0:
        if amount_for_withdrawal>account_balance:
            print("Please enter valid withdrawal amount there is insufficient balance")
        elif amount_for_withdrawal<account_balance:
            balance = account_balance - amount_for_withdrawal
            print("Withdrawal successful!")
        else:
            pass
    else:
        print("Please enter the amount in multiples of 10")
    n = int(input("Do you want to continue press 1 for continue and 0 for exit"))
print("Succesfully Exited")