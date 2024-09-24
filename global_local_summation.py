# Global variable to store the sum
global_sum = 0

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers using a local variable."""
    local_sum = sum(numbers)
    return local_sum

def update_global_sum(numbers):
    """Update the global sum with the local sum calculated from the given numbers."""
    global global_sum  # Declare global to modify it
    local_sum = calculate_sum(numbers)
    global_sum += local_sum

def reset_global_sum():
    """Reset the global sum to zero."""
    global global_sum  # Declare global to modify it
    global_sum = 0

# Example usage
if __name__ == "__main__":
    numbers = [10, 20, 30, 40]

    # Print the global sum before updating
    print("Global sum before calling the function:", global_sum)

    # Update the global sum
    update_global_sum(numbers)

    # Print the global sum after updating
    print("Global sum after calling the function:", global_sum)

    # Reset the global sum
    reset_global_sum()

    # Print the global sum after resetting
    print("Global sum after resetting:", global_sum)