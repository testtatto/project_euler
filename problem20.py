"""
n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.

例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.

では, 100! の各位の数字の和を求めよ.

注: Problem 16 も各位の数字の和に関する問題です。解いていない方は解いてみてください。
"""

import math

if __name__ == '__main__':
    target_number = math.factorial(100)
    str_target_number = str(target_number)
    target_number_str_list = [str_target_number[i] for i in range(0, len(str_target_number))]

    answer = sum([int(i) for i in target_number_str_list])
    print(answer)

