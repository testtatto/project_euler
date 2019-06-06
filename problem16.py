"""
2^15 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.

同様にして, 2^1000 の各位の数字の和を求めよ.

注: Problem 20 も各位の数字の和に関する問題です。解いていない方は解いてみてください。
"""


if __name__ == '__main__':
    number = 2 ** 1000
    # 計算結果を各桁ごとに分割してリストにする
    str_number = str(number)
    split_str_number_list = [str_number[i] for i in range(0, len(str_number))]
    # intに直して総和をとる
    split_number_list = [int(s) for s in split_str_number_list]
    answer = sum(split_number_list)
    print(answer)


