"""
順列とはモノの順番付きの並びのことである. たとえば, 3124は数 1, 2, 3, 4 の一つの順列である. すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ. 0と1と2の順列を辞書順に並べると

012 021 102 120 201 210
になる.

0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目はいくつか?
"""

import math


# 最初の数字を決定させ、その値とそうなるための下限値を返す関数
def check_first_digit(number_list, order):
    first_digit_rank = 0
    for i in range(1, len(number_list) + 1):
        if order <= i * math.factorial(len(number_list) - 1):
            lower = (i - 1) * math.factorial(len(number_list) - 1)
            break
        first_digit_rank += 1

    return number_list[first_digit_rank], lower


if __name__ == '__main__':
    order = 1000000
    target_list = []
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 左から順にリスト内の数字を決定していき、決定した数字を元のリストから取り除いて別リストに移す
    while len(number_list) != 0:
        first_digit_number = check_first_digit(number_list, order)[0]
        current_lower = check_first_digit(number_list, order)[1]
        target_list.append(first_digit_number)

        # 決まった数字を取り除いて、その中での順列を考える
        number_list.remove(first_digit_number)
        order = order - current_lower

    # リストの中の文字列を結合させてintに直す
    answer = int(''.join(target_list))
    print(answer)
