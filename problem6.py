"""
最初の10個の自然数について, その二乗の和は,

1^2 + 2^2 + ... + 10^2 = 385
最初の10個の自然数について, その和の二乗は,

(1 + 2 + ... + 10)^2 = 3025
これらの数の差は 3025 - 385 = 2640 となる.

同様にして, 最初の100個の自然数について二乗の和と和の二乗の差を求めよ.
"""

import numpy as np


if __name__ == '__main__':
    array = np.arange(1, 101)

    result_A = np.sum(array ** 2)
    result_B = (np.sum(array)) ** 2

    answer = result_B - result_A
    print(answer)

