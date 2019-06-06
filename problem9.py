"""
ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.

a^2 + b^2 = c^2
例えば, 32 + 42 = 9 + 16 = 25 = 52 である.

a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
"""
import math

if __name__ == '__main__':
    a = 1
    b = 2
    summary = 0
    combination_list = []

    # aは最小のため、333までを考えればよく、bはcより小さいため、500までで十分
    for a in range(1, 333):
        for b in range(a + 1, 500):
            c = math.sqrt(a ** 2 + b ** 2)

            # cが自然数かどうかの判定を行い、自然数の場合、総和を算出する
            if c.is_integer():
                c = int(c)
                summary = a + b + c
                # 総和が1000かどうかを判定し、1000の場合はa,b,cの組み合わせリストに追加する
                if summary == 1000:
                    combination_list.append([a, b, c])

                    # abcの積を求める
                    answer = a * b * c
                    print(combination_list, answer)
                    break



