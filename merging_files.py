def merge_files(file_list):
    """Merge the contents of multiple files into a single list and remove duplicates."""
    merged_lines = []

    # Read each file and collect the lines
    for filename in file_list:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                merged_lines.extend(line.strip() for line in lines)  # Strip whitespace and add to the list
        except FileNotFoundError:
            print(f"Error: {filename} not found. Skipping this file.")

    # Remove duplicates by converting the list to a set
    unique_lines = list(set(merged_lines))

    return unique_lines


def save_unique_lines_to_file(unique_lines, output_filename='merged_unique.txt'):
    """Save the unique lines to a new text file."""
    with open(output_filename, 'w') as file:
        for line in unique_lines:
            file.write(line + '\n')


if __name__ == "__main__":
    # List of input files
    input_files = ['file1.txt', 'file2.txt']  # Replace with your file names

    # Merge the files and get unique lines
    unique_lines = merge_files(input_files)

    # Save the unique lines to a new file
    save_unique_lines_to_file(unique_lines)

    # Display the merged list
    print("Merged Unique Lines:")
    for line in unique_lines:
        print(line)

    print(f"Unique lines have been saved to 'merged_unique.txt'.")
