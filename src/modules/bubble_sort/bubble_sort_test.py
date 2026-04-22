
from bubble_sort import bubble_sort_float, bubble_sort_str
import numpy as np
from contextlib import contextmanager
import time
from dataclasses import dataclass

@dataclass
class TimerResult:
    elapsed: float
    

@contextmanager
def measure_time():
    result = TimerResult(elapsed=0.0)
    start = time.perf_counter()
    try:
        yield result
    finally:
        result.elapsed = time.perf_counter() - start
        # print(f"measure_time {result.elapsed:.6f} sec")

def is_nearly_equal(a, b, tolerance=1e-3):
    return abs(a - b) <= tolerance

def verify_sorting(sorted_data, answer_data, tolerance=1e-3) -> float:
    if len(sorted_data) != len(answer_data):
        raise Exception("list length unmatched!!!")

    size = len(sorted_data)
    sort_error_distance = 0.0
    for i in range(size):
        n1 = sorted_data[i]
        n2 = answer_data[i]
        if is_nearly_equal(n1, n2, tolerance):
            pass
        else:
            raise Exception("Sorting Error!!!")
        sort_error_distance += (n1 - n2) ** 2
    pass
    return sort_error_distance

def print_report(file_name, size, distance, data, elapsed):
    print("#" * 100)
    print(f"OK: {file_name}")
    print(f"size: {size}")
    print(f"distance: {distance}")
    print(f"sorted top 5: {data[:5]}")
    print(f"sorted tail 5: {data[-5:]}")
    print(f"elapsed: {elapsed}")

def test_target(tsv_file_name: str) -> float:
    X = np.loadtxt(
        fname=tsv_file_name,
        dtype=float,
        delimiter="\t"
    )
    test_data = X[:,0]
    answer_data = X[:,1]
    indexes = X[:,2].astype(np.int32)

    with measure_time() as timer_result:
        sorted_data = bubble_sort_float(test_data.astype(np.float64).tolist(), "asc")
    size = len(test_data)
    distance = verify_sorting(sorted_data, answer_data, 1e-5)
    print_report(tsv_file_name, size, distance, sorted_data, timer_result.elapsed)
    return distance

def test():
    test_target("../testdata/dataset1.tsv")
    test_target("../testdata/dataset2.tsv")
    test_target("../testdata/dataset3.tsv")

if __name__ == "__main__":
    test()

