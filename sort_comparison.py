from random import randint
from time import time

def initialize_list(LENGTH_OF_LIST_TO_SORT):
    '''
    A function which creates a random list of twenty (20) random numbers
    to sort. 
    '''
    num_list = list()

    for i in range(0, LENGTH_OF_LIST_TO_SORT):
        num_list.append(randint(0, 100))

    return num_list


# begin selection sort logic
def selection_sort(num_list):
    '''
    This function contains the selection sort algorithm. It takes the list made in
    initialize_list() as an input, and returns the same list, sorted from least
    to greatest.
    '''
    length_of_list = len(num_list)

    for i in range(0, length_of_list):
        swap_value = 100

        for j in range (i, length_of_list):
            if num_list[j] < swap_value:
                swap_value = num_list[j]
                swap_index = j

        num_list[swap_index] = num_list[i]
        num_list[i] = swap_value
        
        # uncomment the line below to see selection sort steps
        # print(num_list)

    return num_list
# end selection sort logic


# begin insertion sort logic
def insertion_sort(num_list):
    '''
    
    '''
    length_of_list = len(num_list)
    
    for i in range(1, length_of_list): # starts at one to allow looking to left
        is_sorted = False
        element_being_checked = num_list[i]
        while is_sorted == False:
            if i == 0:
                is_sorted = True
            elif num_list[i - 1] > element_being_checked:
                num_list[i] = num_list[i - 1]
                num_list[i - 1] = element_being_checked
            else:
                is_sorted = True
            i = i - 1
            # uncomment the line below to see insertion sort steps
            # print(num_list)
    
    return num_list
# end insertion sort logic


# begin bubble sort logic
def bubble_sort(num_list):
    length_of_list = len(num_list)
    
    for i in range(0, length_of_list):
        for j in range(1, length_of_list - i):
            if num_list[j - 1] > num_list[j]:
                temp = num_list[j]
                num_list[j] = num_list[j - 1]
                num_list[j - 1] = temp
                # uncomment the line below to see bubble sort steps
                # print(num_list)
    
    return num_list
# end bubble sort logic






















def main():
    '''
    The main function serves as a test bed for the sorting algorithms within the program.
    It saves the time before and after each sort executes, then prints the time taken to
    sort several lists once the process has concluded. Each algorithm sorts one hundred 
    thousand (100000) lists, each of which have twenty (20) elements in them.
    '''
    test_list = [5, 7, 8, 2, 4, 3, 6, 9, 19, 22, 15, 7]
    
    NUMBER_OF_LISTS_TO_SORT = 100000
    LENGTH_OF_LIST_TO_SORT = 20
    
    # list_to_sort = initialize_list()
    # bubble_sort(list_to_sort)
    
    # test for selection sort
    start_time = time()
    for i in range(0, NUMBER_OF_LISTS_TO_SORT):
        list_to_sort = initialize_list(LENGTH_OF_LIST_TO_SORT)
        selection_sort(list_to_sort)
    end_time = time()
    
    time_to_complete = end_time - start_time
    time_to_complete = format(time_to_complete, ".5f")
    print("Time to complete selection sort: " + str(time_to_complete) + " seconds.")
    
    # test for insertion sort
    start_time = time()
    for i in range(0, NUMBER_OF_LISTS_TO_SORT):
        list_to_sort = initialize_list(LENGTH_OF_LIST_TO_SORT)
        insertion_sort(list_to_sort)
    end_time = time()
    
    time_to_complete = end_time - start_time
    time_to_complete = format(time_to_complete, ".5f")
    print("Time to complete insertion sort: " + str(time_to_complete) + " seconds.")
    
    # test for bubble sort
    start_time = time()
    for i in range(0, NUMBER_OF_LISTS_TO_SORT):
        list_to_sort = initialize_list(LENGTH_OF_LIST_TO_SORT)
        bubble_sort(list_to_sort)
    end_time = time()
    
    time_to_complete = end_time - start_time
    time_to_complete = format(time_to_complete, ".5f")
    print("   Time to complete bubble sort: " + str(time_to_complete) + " seconds.")
    
main()








