"""
完全数とは, その数の真の約数の和がそれ自身と一致する数のことである. たとえば, 28の真の約数の和は, 1 + 2 + 4 + 7 + 14 = 28 であるので, 28は完全数である.

真の約数の和がその数よりも少ないものを不足数といい, 真の約数の和がその数よりも大きいものを過剰数と呼ぶ.

12は, 1 + 2 + 3 + 4 + 6 = 16 となるので, 最小の過剰数である. よって2つの過剰数の和で書ける最少の数は24である. 数学的な解析により, 28123より大きい任意の整数は2つの過剰数の和で書けることが知られている. 2つの過剰数の和で表せない最大の数がこの上限よりも小さいことは分かっているのだが, この上限を減らすことが出来ていない.

2つの過剰数の和で書き表せない正の整数の総和を求めよ.
"""
import math

LIMIT = 28123


# ある数の真の約数をすべて求める関数(リスト)
def enumerate_divisor(number):
    divisor_list = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisor_list.append(i)
            if i != number // i:
                divisor_list.append(number // i)

    divisor_list.sort()
    # 約数リストの中から自分（number)のみを取り除く
    return [i for i in divisor_list if i != number]


# 過剰数かどうかを判定する関数
def is_abundant_number(number):
    divisor_list = enumerate_divisor(number)
    if number < sum(divisor_list):
        return True
    return False


# 引数の数までを範囲とした過剰数のリストを作成する関数
def create_abundant_number_list(limit):
    abundant_number_list = []
    for i in range(1, limit):
        if is_abundant_number(i):
            abundant_number_list.append(i)

    return abundant_number_list


# リスト内の2つの数字を足し合わせた和集合を作成する関数(制限値まで)
def two_number_sum(number_list):
    sum_list = []
    for i in range(0, len(number_list)):
        for j in range(0, len(number_list)):
            sum = number_list[i] + number_list[j]
            if sum >= LIMIT:
                break
            sum_list.append(sum)

    return set(sum_list)


if __name__ == '__main__':
    abundant_number_list = create_abundant_number_list(LIMIT)
    two_abundant_numbers_sum_list = two_number_sum(abundant_number_list)

    all_sum = sum([i for i in range(1, LIMIT)])
    answer = all_sum - sum(two_abundant_numbers_sum_list)
    print(answer)

