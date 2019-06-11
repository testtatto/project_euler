"""
d(n) を n の真の約数の和と定義する. (真の約数とは n 以外の約数のことである. )
もし, d(a) = b かつ d(b) = a (a ≠ b のとき) を満たすとき, a と b は友愛数(親和数)であるという.

例えば, 220 の約数は 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 なので d(220) = 284 である.
また, 284 の約数は 1, 2, 4, 71, 142 なので d(284) = 220 である.

それでは10000未満の友愛数の和を求めよ.
"""

import math

# ある数の真の約数をすべて求める関数(リスト)
def enumerate_divisor(number):
    divisor_list = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisor_list.append(i)
            if i != number // i:
                divisor_list.append(number // i)

    # 約数リストの中から自分（number)のみを取り除く
    return [ i for i in divisor_list if i != number]


# 友愛数かかどうかを判定し、友愛数ならば友愛数のリストに追加する関数
def check_add_amicable_numbers(number, divisor_list, amicable_numbers_list):
    target_number = sum(divisor_list)
    target_number_divisor_list = enumerate_divisor(target_number)
    if (sum(target_number_divisor_list) == number) & (target_number != number):
        amicable_numbers_list.append(number)

    return amicable_numbers_list


if __name__ == '__main__':
    amicable_number_list = []  # 友愛数を入れていくリスト
    for x in range(1, 10000):
        x_divisor_list = enumerate_divisor(x)
        check_add_amicable_numbers(x, x_divisor_list, amicable_number_list)

    answer = sum(amicable_number_list)
    print(answer)



