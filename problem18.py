"""
以下の三角形の頂点から下まで移動するとき, その数値の和の最大値は23になる.

3
7 4
2 4 6
8 5 9 3
この例では 3 + 7 + 4 + 9 = 23.

以下の三角形を頂点から下まで移動するとき, その最大の和を求めよ.

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
注: ここではたかだか 16384 通りのルートしかないので, すべてのパターンを試すこともできる. Problem 67 は同じ問題だが100行あるので, 総当りでは解けない. もっと賢い方法が必要である.
"""

"""
【方針】
底辺から見ていき、最終段で最大となる値とひとつ上の行を足して、段を減らしていく
最終的に最上段まで足していったものが最大値をとるルートとなる
"""


# 行を最終段から1つ手前の行から最上段0行まで、結合を行っていき残った最大値を返す関数
def calculate_merge_row(number_list):
    # 行を最終段から1つ手前の行から最上段0行まで
    for row_index in range(13, -1, -1):
        # ある1行に対して、下の行の最大値となるものを各列ごとに加えていく
        for column_index in range(0, len(number_list[row_index])):
            merge_number = number_list[row_index][column_index]  # 今の行と下の行の最大値を足したものを格納する変数
            bigger_number = max(number_list[row_index + 1][column_index], number_list[row_index + 1][column_index + 1])
            merge_number += bigger_number
            number_list[row_index][column_index] = merge_number

    return merge_number


if __name__ == '__main__':
    str_number = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
    # 配列に整形する
    str_number_list = str_number.strip().split('\n')  # 改行箇所でリストに分割
    divide_str_number_list = [row.split(' ') for row in str_number_list]  # 行ごとに配列を閉じる
    divide_number_list = [[int(x) for x in row] for row in divide_str_number_list]  # intに直す

    answer = calculate_merge_row(divide_number_list)
    print(answer)
