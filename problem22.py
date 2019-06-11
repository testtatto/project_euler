"""
5000個以上の名前が書かれている46Kのテキストファイルnames.txt を用いる. まずアルファベット順にソートせよ.

のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.

たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある. またCOLINは 3 + 15 + 12 + 9 + 14 = 53 という値を持つ. よってCOLINは 938 × 53 = 49714 というスコアを持つ.

ファイル中の全名前のスコアの合計を求めよ.
"""


# テキストファイルを読み込んで文字列を返す
def read_text_file(file_name):
    with open(file_name, 'r') as f:
        for row in f:
            row.strip()

    return row


# アルファベットを数値に変換して、和を出す
def calculate_alphabet(name):
    sum_alphabet_numbers = 0  # アルファベットを数値に変換した後の各項の和
    # 受け取った名前を分割し、数値に変換して足す
    split_name = list(name)
    for alphabet in split_name:
        alphabet_number = ord(alphabet) - ord('A') + 1
        sum_alphabet_numbers += alphabet_number

    return sum_alphabet_numbers


if __name__ == '__main__':
    str_names = read_text_file('names.txt')
    # 整形した後、アルファベット順に並び替え
    names_list = str_names.replace('"', '').split(',')
    names_list.sort()

    sum_names_score = 0  # スコアの総和の格納する変数
    for i in range(0, len(names_list)):
        name_score = (i+1) * calculate_alphabet(names_list[i])
        sum_names_score += name_score

    answer = sum_names_score
    print(answer)

