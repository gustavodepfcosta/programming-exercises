"""Problem Description

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.
"""

A = [1, 2, 5, -7, 2, 3]


def max_sum_positive_sub_array(array):
    updated_sum = 0
    last_counter_holder = 0
    element_last_index = 0

    for updated_element_index, element_value in enumerate(array):
        print(f'updated_element_index: {updated_element_index} |||| element index {element_value}')
        if element_value >= 0:
            if updated_element_index - element_last_index == 1:
                updated_sum += element_value
                last_counter_holder = updated_sum
            
            else:
                print(f'updated sum {updated_sum} |||| last counter holder : {last_counter_holder}')

                print(last_counter_holder)
        
        element_last_index = updated_element_index

    # print(last_counter_holder)   


max_sum_positive_sub_array(A)
