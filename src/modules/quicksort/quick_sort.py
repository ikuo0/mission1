import sys
import math
import copy


def split_lr(arr: list[float]):
    # pivot
    pivot = arr[0]
    arr = arr[1:]
    l = []
    r = []
    for n in arr:
        if n < pivot:
            l.append(n)
        else:
            r.append(n)
    return pivot, l, r

def quick_sort_float(arr: list[float], order: str):
    if len(arr) <= 1:
        return arr
    pivot, l, r = split_lr(arr)
    lsorted = quick_sort_float(l, order)
    rsorted = quick_sort_float(r, order)
    if order == "asc":
        return lsorted + [pivot] + rsorted
    elif order == "desc":
        return rsorted + [pivot] + lsorted

def test():
    print(quick_sort_float([2,1,4,7,3], "asc"))
    print(quick_sort_float([2,1,4,7,3], "desc"))

if __name__ == "__main__":
    test()
