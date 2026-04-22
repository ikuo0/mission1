import os
import sys
import numpy as np
from dataclasses import dataclass

THIS_FILE_PATH = os.path.abspath(__file__)
# スクリプトがあるディレクトリの絶対パス
THIS_FILE_DIR = os.path.dirname(THIS_FILE_PATH)

@dataclass
class DataSet:
    numbers: np.ndarray
    sorted_numbers: np.ndarray

def generate_rnd_numbers(count, coeff=1):
    rng = np.random.default_rng()
    numbers = rng.random(count)
    numbers = numbers * coeff
    return numbers


def generate_test_data(count, coeff=1):
    numbers = generate_rnd_numbers(count, coeff)
    soprted = np.sort(numbers)
    return DataSet(
        numbers=numbers,
        sorted_numbers=soprted
    )

def create_dataset(file_name: str, count, coeff):
    dataset1 = generate_test_data(count, coeff)
    indexes = np.argsort(dataset1.numbers)
    X = np.stack([dataset1.numbers, dataset1.sorted_numbers, indexes], axis=1)
    np.savetxt(file_name, X, delimiter='\t', fmt=['%.10f', '%.10f', '%d'])

def main():
    create_dataset(os.path.join(THIS_FILE_DIR, "dataset1.tsv"), 10, 1)
    create_dataset(os.path.join(THIS_FILE_DIR, "dataset2.tsv"), 100, 10)
    create_dataset(os.path.join(THIS_FILE_DIR, "dataset3.tsv"), 10000, 1)
    return
    print(dataset)

if __name__ == "__main__":
    main()

