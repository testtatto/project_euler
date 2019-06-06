"""
10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.

200万以下の全ての素数の和を求めよ.
"""

import math


# 素数かどうかの判定関数
def check_prime_number(number, number_list):
    end_number = math.sqrt(number)
    for i in number_list:
        # 試し割り法により平方根より大きい値については不要なので、抜ける
        if i > end_number:
            break
        # 各素数で割り切れるなら素数でないのでFalseを返す
        elif number % i == 0:
            return False

    return True


# ある数字まで素数判定を行い、素数リストを作成する関数
def create_prime_list(end_number):
    target_number = 2  # 素数判定を行う数字の初期設定
    prime_number_list = [2]  # 初期の素数リスト

    while target_number <= end_number:
        if check_prime_number(target_number, prime_number_list):
            # 素数の場合は素数リストに追加する
            prime_number_list.append(target_number)

        target_number = target_number + 1

    return prime_number_list


if __name__ == '__main__':
    NUMBER = 2000000
    prime_list = create_prime_list(NUMBER)

    # 総和を算出する
    answer = sum(prime_list)
    print(answer)

