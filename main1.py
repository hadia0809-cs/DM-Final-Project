import time
import random
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Banner in magenta
banner_text = r"""
  /$$$$$$                        /$$           /$$    /$$ /$$                                          /$$ /$$
 /$$__  $$                      | $$          | $$   | $$|__/                                         | $$|__/
/$$  \__/  /$$$$$$   /$$$$$$  /$$$$$$        | $$   | $$ /$$  /$$$$$$$ /$$    /$$ /$$   /$$  /$$$$$$ | $$ /$$ /$$$$$$$$  /$$$$$$   /$$$$$$
|  $$$$$$  /$$__  $$ /$$__  $$|_  $$_/        |  $$ / $$/| $$ /$$_____/|  $$  /$$/| $$  | $$ |____  $$| $$| $$|____ /$$/ /$$__  $$ /$$__  $$
\____  $$| $$  \ $$| $$  \__/  | $$           \  $$ $$/ | $$|  $$$$$$  \  $$/$$/ | $$  | $$  /$$$$$$$| $$| $$   /$$$$/ | $$$$$$$$| $$  \__/
/$$  \ $$| $$  | $$| $$        | $$ /$$        \  $$$/  | $$ \____  $$  \  $$$/  | $$  | $$ /$$__  $$| $$| $$  /$$__/  | $$_____/| $$
 $$$$$$/|  $$$$$$/| $$        |  $$$$/         \  $/   | $$ /$$$$$$$/   \  $/   |  $$$$$$/|  $$$$$$$| $$| $$ /$$$$$$$$|  $$$$$$$| $$
\______/  \______/ |__/         \___/            \_/    |__/|_______/     \_/     \______/  \_______/|__/|__/|________/ \_______/|__/
"""

# Print banner
print(Fore.MAGENTA + Style.BRIGHT + banner_text)

# Some information about the case study
print("----------------------------------------------------------------------------------")

print(Fore.YELLOW + "              SORTING ALGORITHMS CASE STUDY")
print(Fore.YELLOW + "              Students Result Management System")

print("----------------------------------------------------------------------------------")

print(Fore.CYAN + "A school wants to sort the results of students in descending order. This ")
print(Fore.CYAN + "program will help in sorting and tells which algorithm is best for small")
print(Fore.CYAN + "and large datasets.")

# Menu function for source of data set


def dataset_menu():

    print(Fore.WHITE + "\nChoose the type of dataset you want to process")
    print(Fore.BLUE + "1: Want to sort data from files")
    print(Fore.BLUE + "2: Want to sort data generated automatically")
    print(Fore.BLUE + "0: Exit the program")

    while True:

        choice_1 = input("Enter choice (0-2): ")

        if choice_1 in ["0", "1", "2"]:
            return int(choice_1)
        else:
            print(Fore.RED + "Invalid choice! Enter choice between 1 and 2")


# Menu for type of data
def type_data():

    print(Fore.WHITE + " What type of data you want")
    print(Fore.BLUE + "1: Sorted dataset")
    print(Fore.BLUE + "2: Reverse sorted dataset")
    print(Fore.BLUE + "3: Random dataset")
    print(Fore.BLUE + "0: Exit the program")

    while True:
        choice_2 = input("Enter choice frome (0-3): ")

        if choice_2 in ["0", "1", "2", "3"]:
            return int(choice_2)
        else:
            print(Fore.RED + "Invalid choice! Enter choice between 1 and 3")

# Generating dataset accoring to chosen category


def dataset_type(size, data_type):

    students = []
    marks = []

    for i in range(size):
        students.append(f"Student{i+1}")
        marks.append(random.randint(0, 1000000))
    if data_type == 1:
        marks.sort(reverse=True)
    elif data_type == 2:
        marks.sort()

    return students, marks

# Menu function with validation


def menu():

    while True:
        print(Fore.BLUE + "1: Selection Sort")
        print(Fore.BLUE + "2: Bubble Sort")
        print(Fore.BLUE + "3: Insertion Sort")
        print(Fore.BLUE + "4: Merge Sort")
        print(Fore.BLUE + "5: Quick Sort")
        print(Fore.BLUE + "0: Exit the program")
        choice = input(Fore.WHITE + "Enter your choice (0-5): ")

        if choice in ["0", "1", "2", "3", "4", "5"]:
            return int(choice)

        else:
            print(Fore.RED + "Invalid choice! Enter a number between 0-5.")

# Function to read marks along with students names


def read_marks(filename):
    students = []
    marks = []

    with open(filename, "r") as file:

        for line in file:
            name, mark = line.split()
            students.append(name)
            marks.append(int(mark))

    return students, marks

# Function to store marks along with students names


def save_sorted_marks(filename, students, marks):

    with open(filename, "w") as file:

        for student, mark in zip(students, marks):
            file.write(f"{student} {mark}\n")
    print(Fore.YELLOW + f"\nSorted data saved to {filename}")


# Selection Sort
def selection_sort(students, marks):

    n = len(marks)
    step = 1
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        index_max = i

        for j in range(i + 1, n):
            comparisons += 1  # Count comparison here

            if marks[j] > marks[index_max]:  # Descending order
                index_max = j
        marks[i], marks[index_max] = marks[index_max], marks[i]
        students[i], students[index_max] = students[index_max], students[i]
        swaps += 1  # Count swap here
        print(Fore.LIGHTCYAN_EX + f"Step {step}: {list(zip(students, marks))}")
        step += 1

    print(Fore.YELLOW + f"Total Comparisons: {comparisons}")
    print(Fore.YELLOW + f"Total Swaps: {swaps}")

    return students, marks

# Bubble Sort


def bubble_sort(students, marks):

    n = len(marks)
    step = 1
    comparisons = 0
    swaps = 0

    for i in range(n - 1):

        for j in range(n - 1 - i):
            comparisons += 1  # Count comparison here

            if marks[j] < marks[j + 1]:  # Descending
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                students[j], students[j + 1] = students[j + 1], students[j]
                swaps += 1  # Count swap here
                print(Fore.LIGHTCYAN_EX +
                      f"Step {step}: {list(zip(students, marks))}")
                step += 1

    print(Fore.YELLOW + f"Total Comparisons: {comparisons}")
    print(Fore.YELLOW + f"Total Swaps: {swaps}")

    return students, marks

# Insertion Sort


def insertion_sort(students, marks):

    n = len(marks)
    step = 1
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        key_mark = marks[i]
        key_students = students[i]
        j = i - 1

        while j >= 0 and marks[j] < key_mark:  # Descending
            comparisons += 1  # Count comparison here
            marks[j + 1] = marks[j]
            students[j + 1] = students[j]
            j -= 1
            swaps += 1  # Count move as swap here
            print(Fore.LIGHTCYAN_EX +
                  f"Step {step}: {list(zip(students, marks))}")
            step += 1

        marks[j + 1] = key_mark
        students[j + 1] = key_students
        print(Fore.LIGHTCYAN_EX + f"Step {step}: {list(zip(students, marks))}")
        step += 1

    print(Fore.YELLOW + f"Total Comparisons: {comparisons}")
    print(Fore.YELLOW + f"Total Swaps: {swaps}")

    return students, marks

# Merge Sort helper


def merge(left_students, left_marks, right_students, right_marks):
    merged_students = []
    merged_marks = []
    i = j = 0

    while i < len(left_marks) and j < len(right_marks):
        if left_marks[i] >= right_marks[j]:  # Descending
            merged_marks.append(left_marks[i])
            merged_students.append(left_students[i])
            i += 1
        else:
            merged_marks.append(right_marks[j])
            merged_students.append(right_students[j])
            j += 1

    while i < len(left_marks):
        merged_marks.append(left_marks[i])
        merged_students.append(left_students[i])
        i += 1

    while j < len(right_marks):
        merged_marks.append(right_marks[j])
        merged_students.append(right_students[j])
        j += 1

    print(Fore.LIGHTCYAN_EX + "Merging:",
          list(zip(merged_students, merged_marks)))

    return merged_students, merged_marks


def merge_sort(students, marks):

    if len(marks) <= 1:

        return students, marks

    mid = len(marks) // 2
    left_students, left_marks = merge_sort(students[:mid], marks[:mid])
    right_students, right_marks = merge_sort(students[mid:], marks[mid:])

    return merge(left_students, left_marks, right_students, right_marks)

# Quick Sort


def quick_sort(students, marks):

    if len(marks) <= 1:
        return students, marks

    pivot_index = len(marks) // 2
    pivot_mark = marks[pivot_index]
    pivot_students = students[pivot_index]
    left_marks = []
    left_students = []
    right_marks = []
    right_students = []
    equal_marks = []
    equal_students = []

    for s, m in zip(students, marks):
        if m > pivot_mark:
            left_marks.append(m)
            left_students.append(s)
        elif m < pivot_mark:
            right_marks.append(m)
            right_students.append(s)
        else:
            equal_marks.append(m)
            equal_students.append(s)
    print(Fore.LIGHTCYAN_EX +
          f"Pivot {pivot_mark} → {list(zip(left_students, left_marks))} {list(zip(equal_students, equal_marks))} {list(zip(right_students, right_marks))}")

    left_students, left_marks = quick_sort(left_students, left_marks)
    right_students, right_marks = quick_sort(right_students, right_marks)
    students_sorted = left_students + equal_students + right_students
    marks_sorted = left_marks + equal_marks + right_marks

    return students_sorted, marks_sorted

# Apply sort with timing


def apply_sort(students, marks, choice):
    show_time_complexity(choice)

    start_time = time.time()
    if choice == 1:
        students, marks = selection_sort(students, marks)
    elif choice == 2:
        students, marks = bubble_sort(students, marks)
    elif choice == 3:
        students, marks = insertion_sort(students, marks)
    elif choice == 4:
        students, marks = merge_sort(students, marks)
    elif choice == 5:
        students, marks = quick_sort(students, marks)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(Fore.MAGENTA + f"\nTime taken: {elapsed_time:.6f} seconds")
    print(Fore.GREEN + f"Sorted Result: {list(zip(students, marks))}")

    # Save to file
    save_sorted_marks("sorted_marks4.txt", students, marks)
    return students, marks

# time complexities of sorting algorithms


def show_time_complexity(choice):

    print(Fore.YELLOW + "\n--- Time Complexity Analysis (Theoretical) ---")

    if choice == 1:  # Selection Sort
        print("Algorithm     : Selection Sort")
        print("Best Case     : O(n^2)")
        print("Average Case  : O(n^2)")
        print("Worst Case    : O(n^2)")

    elif choice == 2:  # Bubble Sort
        print("Algorithm     : Bubble Sort")
        print("Best Case     : O(n)")
        print("Average Case  : O(n^2)")
        print("Worst Case    : O(n^2)")

    elif choice == 3:  # Insertion Sort
        print("Algorithm     : Insertion Sort")
        print("Best Case     : O(n)")
        print("Average Case  : O(n^2)")
        print("Worst Case    : O(n^2)")

    elif choice == 4:  # Merge Sort
        print("Algorithm     : Merge Sort")
        print("Best Case     : O(n log n)")
        print("Average Case  : O(n log n)")
        print("Worst Case    : O(n log n)")

    elif choice == 5:  # Quick Sort
        print("Algorithm     : Quick Sort")
        print("Best Case     : O(n log n)")
        print("Average Case  : O(n log n)")
        print("Worst Case    : O(n^2)")

    print("-" * 90)

# table for complexities so that user can easily choose based on length of input


def show_complexity_table():
    print(Fore.YELLOW + "\n--- Sorting Algorithms Time Complexity Table & Dataset Suitability ---")

    print(Fore.GREEN +
          f"{'Algorithm':<15} {'Best Case':<12} {'Average Case':<14} {'Worst Case':<12} {'Best For Data Size':<20}")
    print("-" * 90)

    print(Fore.GREEN +
          f"{'Selection Sort':<15} {'O(n^2)':<12} {'O(n^2)':<14} {'O(n^2)':<12} {'Small datasets':<20}")

    print(Fore.GREEN +
          f"{'Bubble Sort':<15} {'O(n)':<12} {'O(n^2)':<14} {'O(n^2)':<12} {'Small datasets':<20}")

    print(Fore.GREEN +
          f"{'Insertion Sort':<15} {'O(n)':<12} {'O(n^2)':<14} {'O(n^2)':<12} {'Small or nearly sorted':<20}")

    print(Fore.GREEN +
          f"{'Merge Sort':<15} {'O(n log n)':<12} {'O(n log n)':<14} {'O(n log n)':<12} {'Large datasets':<20}")

    print(Fore.GREEN +
          f"{'Quick Sort':<15} {'O(n log n)':<12} {'O(n log n)':<14} {'O(n^2)':<12} {'Large datasets*':<20}")

    print("-" * 90)


# Main function
def main():
    show_complexity_table()

    while True:
        source = dataset_menu()
        if source == 0:
            print(Fore.MAGENTA + "Exiting program. Goodbye!")
            break

        if source == 1:

            if not os.path.isfile("data/marks.txt"):
                print(
                    Fore.RED + "Error: Input file 'marks.txt' not found. Please create the file and try again.")
                continue

            students, marks = read_marks("data/marks.txt")

        else:
            print(Fore.YELLOW + "\nDataset Configuration")
            size = int(input("Enter number of students: "))
            data_type = type_data()
            if data_type == 0:
                print(Fore.MAGENTA + "Exiting program. Goodbye!")
                break
            students, marks = dataset_type(size, data_type)

        print(Fore.GREEN + "\nInitial Dataset:")
        print(list(zip(students, marks)))

        choice = menu()
        if choice == 0:
            print(Fore.MAGENTA + "Exiting program. Goodbye!")
            break

        students, marks = apply_sort(students, marks, choice)


if __name__ == "__main__":
    main()
