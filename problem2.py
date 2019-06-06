"""
フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
数列の項の値が400万以下の, 偶数値の項の総和を求めよ.

Note:この問題は最近更新されました. お使いのパラメータが正しいかどうか確認してください.

"""

import numpy as np

if __name__ == '__main__':
    fibonacci = np.array([1, 2])
    next_number = fibonacci[-1] + fibonacci[-2]

    # 項の値が400万以下までのフィボナッチ数列を作成する
    while next_number <= 4000000:
        next_number = fibonacci[-1] + fibonacci[-2]

        # 400万以下の場合のみ配列に追加
        if next_number <= 4000000:
            fibonacci = np.append(fibonacci, next_number)

    print(fibonacci)

    # 偶数値のみの配列を作成する
    even_valued_fibonacci = fibonacci[fibonacci % 2 == 0]

    answer = np.sum(even_valued_fibonacci)
    print(answer)






