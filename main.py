def calculate_average(*grades):
    total_grades = len(grades)
    result = 0  # Initialize result to 0

    for grade in grades:  # Go through all grades with a for loop
        result += grade  # Add each grade to result

    return result / total_grades  # Return the average


# Test cases
print(calculate_average(85, 90, 78, 92))
print(calculate_average(100, 95))