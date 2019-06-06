"""
素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

10 001 番目の素数を求めよ.
"""


# 素数かどうかの判定関数
def check_prime_number(number, number_list):
    for i in number_list:
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    target_number = 2  # 素数判定を行う数字の初期設定
    prime_number_list = [2]  # 素数を格納するリストの初期設定

    while len(prime_number_list) < 10001:
        if check_prime_number(target_number, prime_number_list):
            # 素数の場合は素数リストに追加する
            prime_number_list.append(target_number)

        target_number = target_number + 1

    answer = prime_number_list[-1]
    print(answer)
