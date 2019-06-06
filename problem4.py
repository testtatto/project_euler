"""
左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.

では, 3桁の数の積で表される回文数の最大値を求めよ.
"""


def check_palindromic_number(number):
    str_number = str(number)
    char_list = list(str_number)

    for i in range(0, 3):
        if char_list[i] != char_list[-1 - i]:
            return False

    return True


if __name__ == '__main__':
    a = 100
    b = 100
    palindromic_number_list = []

    # 3桁同士の掛け算を行い、回文数かどうかを確認する
    for a in range(100, 1000):
        for b in range(100, 1000):
            c = a * b

            # 回文数だったものをリストに入れていく
            if check_palindromic_number(c):
                palindromic_number_list.append(c)

    answer = max(palindromic_number_list)
    print(answer)













