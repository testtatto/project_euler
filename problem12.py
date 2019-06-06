"""
三角数の数列は自然数の和で表わされ, 7番目の三角数は 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 である. 三角数の最初の10項は:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
となる.

最初の7項について, その約数を列挙すると, 以下のとおり.

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

これから, 7番目の三角数である28は, 5個より多く約数をもつ最初の三角数であることが分かる.

では, 500個より多く約数をもつ最初の三角数はいくつか.
"""

import math


# ある数の約数をすべて求める関数(リスト)
def enumerate_divisor(triangle_number):
    divisor_list = []
    for i in range(1, int(math.sqrt(triangle_number)) + 1):
        if triangle_number % i == 0:
            divisor_list.append(i)
            if i != triangle_number // i:
                divisor_list.append(triangle_number // i)

    return divisor_list


if __name__ == '__main__':
    triangle_numbers_list = [1]  # 三角数リストの初期設定

    while True:
        current_last_number = triangle_numbers_list[-1]  # 現在の三角数リストの末端
        diff = len(triangle_numbers_list) + 1  # 次の三角数との階差
        next_triangle_number = current_last_number + diff  # 次の三角数
        triangle_numbers_list.append(next_triangle_number)

        divisor_amount = len(enumerate_divisor(next_triangle_number))
        if divisor_amount > 500:
            answer = next_triangle_number
            print(answer)
            break





