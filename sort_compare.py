## Part 2: Sorting Algorithm

import argparse
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(1, n+1))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
## starts the stopwatch 
    start = time.time()
    
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
        
## returns containing the modified list and the elapsed time
    return a_list, time.time() - start


def shellSort(alist):
    start = time.time()
    sublistcount = len(alist) // 2
    
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

## reducing terminal spam by limiting  print statements
        sublistcount = sublistcount // 2
        
    return alist, time.time() - start

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    start = time.time()
## sorted() creates and returns a new sorted list 
    a_list = sorted(a_list)
## retunrs with list and time passed
    return a_list, time.time() - start


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    for size in list_sizes:
        insert_time = 0.0
        shell_time = 0.0
        python_time = 0.0

        for _ in range(100):
## generates one master random list for this iteration
            mylist = get_me_random_list(size)

## passes a copy of the list ([:]) so one alogrithm doenst keep resorting for others
            _, time_spent = insertion_sort(mylist[:])
            insert_time += time_spent

            _, time_spent = shellSort(mylist[:])
            shell_time += time_spent

            _, time_spent = python_sort(mylist[:])
            python_time += time_spent

        print(f"\n--- Averages for list of {size} elements ---")
        print(f"Insertion sort took {insert_time / 100:10.7f} seconds to run, on average")
        print(f"Shell sort took {shell_time / 100:10.7f} seconds to run, on average")
        print(f"Python sort took {python_time / 100:10.7f} seconds to run, on average")
