import random
import time

def insertion_sort(a_list):
    start_time = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end_time = time.time()
    time_taken = end_time - start_time

    return time_taken

def shell_sort(a_list):
    start_time = time.time()

    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.time()
    time_taken = end_time - start_time

    return time_taken


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    start_time = time.time()

    a_list.sort()

    end_time = time.time()
    time_taken = end_time - start_time

    return time_taken

def main():
    list_sizes = [500, 1000, 5000]

    for size in list_sizes:
        insertion_total = 0
        shell_total = 0
        python_total = 0

        for i in range(100):
            random_list = [random.randint(1, 1000000) for _ in range(size)]

            insertion_list = random_list.copy()
            shell_list = random_list.copy()
            python_list = random_list.copy()

            insertion_total += insertion_sort(insertion_list)
            shell_total += shell_sort(shell_list)
            python_total += python_sort(python_list)

        print("List size:", size)
        print(f"Insertion Sort took {insertion_total / 100:10.7f} seconds to run, on average")
        print(f"Shell Sort took {shell_total / 100:10.7f} seconds to run, on average")
        print(f"Python Sort took {python_total / 100:10.7f} seconds to run, on average")
        print()


if __name__ == "__main__":
    main()
