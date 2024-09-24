# Global counter variable
call_count = 0


def count_function_calls(reset=False):
    """Count the number of times the function has been called."""
    global call_count  # Declare global to modify it

    if reset:
        call_count = 0  # Reset the counter if reset is True
        print("Counter has been reset.")
    else:
        call_count += 1  # Increment the counter
        print(f"Function has been called {call_count} times.")


# Example usage
if __name__ == "__main__":
    # Call the function a few times
    count_function_calls()  # Call 1
    count_function_calls()  # Call 2
    count_function_calls()  # Call 3

    # Reset the counter
    count_function_calls(reset=True)  # Reset

    # Call the function again after resetting
    count_function_calls()  # Call 1 after reset
