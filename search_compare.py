## Part 1: Search Algorithm

import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    ## by adding the 1, n+1 it acts as a starter point, so it doesnt start a 0
    a_list = list(range(1, n+1))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, time.time() - start

def ordered_sequential_search(a_list, item):
    start = time.time()
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

    return found, time.time() - start

def binary_search_iterative(a_list, item):
    start = time.time()
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

    return found, time.time() - start


def binary_search_recursive(a_list, item):
    start = time.time()
    
    def _search(lst, target):
        if len(lst) == 0:
            return False
        else:
            midpoint = len(lst) // 2
            if lst[midpoint] == target:
                return True
            else:
                if target < lst[midpoint]:
                    return _search(lst[:midpoint], target)
                else:
                    return _search(lst[midpoint + 1:], target)
                    
    found = _search(a_list, item)
    return found, time.time() - start

if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]
    target = 99999999

    for size in list_sizes:
        seq_time = 0.0
        ord_seq_time = 0.0
        bin_iter_time = 0.0
        bin_rec_time = 0.0

        for _ in range(100):
            mylist = get_me_random_list(size)

            _, time_spent = sequential_search(mylist, target)
            seq_time += time_spent

            mylist.sort()

            _, time_spent = ordered_sequential_search(mylist, target)
            ord_seq_time += time_spent

            _, time_spent = binary_search_iterative(mylist, target)
            bin_iter_time += time_spent

            _, time_spent = binary_search_recursive(mylist, target)
            bin_rec_time += time_spent

        print(f"\n--- Averages for list of {size} elements ---")
        print(f"Sequential Search took {seq_time / 100:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ord_seq_time / 100:10.7f} seconds to run, on average")
        print(f"Iterative Binary Search took {bin_iter_time / 100:10.7f} seconds to run, on average")
        print(f"Recursive Binary Search took {bin_rec_time / 100:10.7f} seconds to run, on average") 


## if start = time.time() was inside the repeating loop, 
## the stopwatch would reset every time the function called itself.
## keeping the timer on the outside prevents the math from resetting.

