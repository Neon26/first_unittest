#Solve the following question and create test cases with unittest

# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.
array1 = [0, 1, 0, 3, 12]
# Output:
 #[1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
Output = [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]


#Your grade will be judged on:
#ability to solve the question (speed of your solution will not affect your grade, but efficiency is king)
#Correctly creating your Test file
#Choosing The correct Test Cases to ensure your solution is valid.

#loop through the list of numbers
#if number is zero move to another list.
# once all numbers have been checked and all zeros removed
#move the zeros back to the first list at the end of the list.


def zero_number(lst):
    zero_count=0
    for n in lst:
        if n:
           lst[zero_count] = n
           zero_count = zero_count + 1
    for n in range(zero_count, len(lst)):
        lst[n] = 0
    return lst
 
if __name__ == '__main__':
    
    print(zero_number(array1))    
