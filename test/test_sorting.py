# test/test_sorting.py

# Import your sorting functions from your main script file
# Replace 'your_sorting_script' with the name of your script file without '.py'
from main1 import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort


def test_sorting_algorithm(sort_func):
    print(f"\nTesting {sort_func.__name__}...")

    # Sample test data
    students = ["A", "B", "C", "D"]
    marks = [50, 20, 80, 40]

    # Copy lists to avoid modifying original test data
    students_copy = students[:]
    marks_copy = marks[:]

    # Run sorting algorithm
    sorted_students, sorted_marks = sort_func(students_copy, marks_copy)

    # Expected output (descending order by marks)
    expected_marks = [80, 50, 40, 20]

    # Check if output matches expected
    if sorted_marks == expected_marks:
        print(f"{sort_func.__name__} passed!")
    else:
        print(f"{sort_func.__name__} failed.")
        print(f"Expected marks: {expected_marks}")
        print(f"Got marks     : {sorted_marks}")


def main():
    test_sorting_algorithm(selection_sort)
    test_sorting_algorithm(bubble_sort)
    test_sorting_algorithm(insertion_sort)
    test_sorting_algorithm(merge_sort)
    test_sorting_algorithm(quick_sort)


if __name__ == "__main__":
    main()