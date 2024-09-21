def print_star_pyramid(height):
    for i in range(height):
        # Print spaces
        print(' ' * (height - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

# Set the height of the pyramid
pyramid_height = 5
print_star_pyramid(pyramid_height)
