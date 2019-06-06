"""
2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.

では, 20×20 のマス目ではいくつのルートがあるか.
"""

import math

if __name__ == '__main__':
    ROW = 20
    COLUMN = 20

    # ルートの組み合わせは右移動20回、下移動20回の合計40回の重複あり順列と考えられる。解は 40! / (20! * 20!)
    answer = int(math.factorial(ROW + COLUMN) / (math.factorial(ROW) * math.factorial(COLUMN)))
    print(answer)
