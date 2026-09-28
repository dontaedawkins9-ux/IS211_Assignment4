import random
import time

def sequential_search(a_list, item):
    start_time = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()
    time_taken = end_time - start_time

    return found, time_taken

def ordered_sequential_search(a_list, item):
    start_time = time.time()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()
    time_taken = end_time - start_time
        
    return found, time_taken

def binary_search_iterative(a_list, item):
    start_time = time.time()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()
    time_taken = end_time - start_time

    return found, time_taken

def binary_search_recursive(a_list, item):
    start_time = time.time()

    def binary_search(a_list, item):
        if len(a_list) == 0:
            return False

        midpoint = len(a_list) // 2

        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search(a_list[:midpoint], item)
            else:
                return binary_search(a_list[midpoint + 1:], item)

    found = binary_search(a_list, item)

    end_time = time.time()
    time_taken = end_time - start_time

    return found, time_taken


def main():
    list_sizes = [500, 1000, 5000]
    search_item = 99999999

    for size in list_sizes:
        sequential_total = 0
        ordered_total = 0
        iterative_total = 0
        recursive_total = 0

        for i in range(100):
            random_list = [random.randint(1, 1000000) for _ in range(size)]

            result, time_taken = sequential_search(random_list, search_item)
            sequential_total += time_taken

            random_list.sort()

            result, time_taken = ordered_sequential_search(random_list, search_item)
            ordered_total += time_taken

            result, time_taken = binary_search_iterative(random_list, search_item)
            iterative_total += time_taken

            result, time_taken = binary_search_recursive(random_list, search_item)
            recursive_total += time_taken

        print("List size:", size)
        print(f"Sequential Search took {sequential_total / 100:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ordered_total / 100:10.7f} seconds to run, on average")
        print(f"Iterative Binary Search took {iterative_total / 100:10.7f} seconds to run, on average")
        print(f"Recursive Binary Search took {recursive_total / 100:10.7f} seconds to run, on average")
        print()


if __name__ == "__main__":
    main()
