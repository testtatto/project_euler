"""
13195 の素因数は 5, 7, 13, 29 である.

600851475143 の素因数のうち最大のものを求めよ.
"""

if __name__ == '__main__':
    divisor = 2
    number_to_be_divided = 600851475143
    prime_number_list = []

    while number_to_be_divided != 1:
        if number_to_be_divided % divisor == 0:
            number_to_be_divided = number_to_be_divided / divisor

            # 割った素数をリストに入れていく
            prime_number_list.append(divisor)
        else:
            divisor = divisor + 1

    answer = prime_number_list[-1]
    print(answer)
