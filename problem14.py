"""
正の整数に以下の式で繰り返し生成する数列を定義する.

n → n/2 (n が偶数)
n → 3n + 1 (n が奇数)

13からはじめるとこの数列は以下のようになる.
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
13から1まで10個の項になる. この数列はどのような数字からはじめても最終的には 1 になると考えられているが, まだそのことは証明されていない(コラッツ問題)

さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.
注意: 数列の途中で100万以上になってもよい
"""


# 与えられた関数の処理を行う関数
def calculate(n):
    sequence_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        # 更新したnをリストに追加する
        sequence_list.append(n)

    return sequence_list


if __name__ == '__main__':
    answer_number = 1
    max_length = 1

    for i in range(2, 1000000):
        current_length = len(calculate(i))
        # 現在の長さがこれまでの最大の長さより長い場合は長さとそのときの数値を更新する
        if current_length > max_length:
            max_length = current_length
            answer_number = i

    print(answer_number)
