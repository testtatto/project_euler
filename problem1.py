"""
10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ
"""

import numpy as np

if __name__ == '__main__':
    three_multiples = np.arange(3, 1000, 3)
    five_multiples = np.arange(5, 1000, 5)
    fifteen_multiples = np.arange(15, 1000, 15)
    answer = (np.sum(three_multiples) + np.sum(five_multiples) - np.sum(fifteen_multiples))

    print(answer)



