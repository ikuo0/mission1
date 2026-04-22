import sys
import copy


def bubble_sort_float(arr: list[float], order: str):
    size = len(arr)
    arr_clone = copy.deepcopy(arr)
    cmp = None
    if order == "desc": # 降順
        cmp = lambda a, b: a < b
    elif order == "asc": # 昇順
        cmp = lambda a, b: a > b
    else:
        raise Exception(f"illegal order [{order}]")

    for i in range(1, size):
        for j in range(size - i):
            v1 = arr_clone[j]
            v2 = arr_clone[j + 1]
            if cmp(v1, v2):
                arr_clone[j + 1] = v1
                arr_clone[j] = v2
    return arr_clone

def bubble_sort_str(arr: list[str], order: str):
    size = len(arr)
    arr_clone = copy.deepcopy(arr)
    cmp = None
    if order == "desc": # 降順
        cmp = lambda a, b: a < b
    elif order == "asc": # 昇順
        cmp = lambda a, b: a > b
    else:
        raise Exception(f"illegal order [{order}]")

    for i in range(1, size):
        for j in range(size - i):
            v1 = arr_clone[j]
            v2 = arr_clone[j + 1]
            if cmp(v1, v2):
                arr_clone[j + 1] = v1
                arr_clone[j] = v2
    return arr_clone

def test():
    print(bubble_sort_float([2,1,4,7,3], "asc"))
    print(bubble_sort_str(["hoge", "piyo", "fuga"], "asc"))
    print(bubble_sort_str(["hoge", "piyo", "fuga"], "desc"))

if __name__ == "__main__":
    test()
