import functools
from functools import reduce


def func(ints, names, numbers):
    # Use map to print the square of each numbers
    # Use filter to print only the names that are less than or equal to seven letters
    # Use reduce to print the product of these numbers

    # Complete all the three codes.
    map_result = list(map(lambda x: x**2,ints))
    filter_result = list(filter(lambda str1:len(str1)<= 7,names))
    reduce_result = reduce(lambda x,y:x*y,numbers)

    return map_result, filter_result, reduce_result


print(func([4, 6, 3, 9, 2, 8, 12],["scaler", "interviewbit", "rishabh", "student", "course"],[4, 6, 9, 23, 5]))