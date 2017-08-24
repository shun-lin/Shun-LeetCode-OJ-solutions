# use python's list comprehension and first element as pivot
def quickSort(lst):
    if lst == None or len(lst) <= 1:
        return lst;
    pivot = lst[0];
    lower_than_pivot = [num for num in lst if num < pivot];
    higher_or_equal_than_pivot = [num for num in lst if num >= pivot];
    lower_than_pivot = quickSort(lower_than_pivot);
    higher_or_equal_than_pivot = quickSort(higher_or_equal_than_pivot);
    return lower_than_pivot + higher_or_equal_than_pivot;
