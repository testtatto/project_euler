"""
2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり, そのような数字の中では最小の値である.

では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
"""
import math


# 最小公倍数を求める関数
def lcm(a, b):
    return a * b // math.gcd(a, b)


if __name__ == '__main__':
    current_lcm = 1
    # 最小公倍数を再帰的に更新していく
    for i in range(1, 21):
        current_lcm = lcm(current_lcm, i)

    answer = current_lcm
    print(answer)
