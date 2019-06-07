"""
次の情報が与えられている.

1900年1月1日は月曜日である.
9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
2月は28日まであるが, うるう年のときは29日である.
うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.
20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
"""

days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11]
February = [2]


# 期間内の年と月の組み合わせを生成する関数
def month_first_day_list(start_year, end_year):
    year_month_list = []
    for i in range(start_year, end_year + 1):
        for j in range(1, 13):
            year_month_list.append([i, j])

    return year_month_list


# 当月の日数を計算する関数
def calculate_days_next_month(date):
    year = date[0]
    month = date[1]

    if month in days_31:
        days = 31
    elif month in days_30:
        days = 30
    elif month in February:
        if year % 4 == 0:
            if year % 400 != 0 & year % 100 == 0:
                days = 28
            else:
                days = 29
        else:
            days = 28

    return days


if __name__ == '__main__':
    weekday_dict = {"月": 0, "火": 1, "水": 2, "木": 3, "金": 4, "土": 5, "日": 6}
    year_month_list = month_first_day_list(1900, 2000)
    # 1900年の1月1日は月曜日なので0をリストに追加
    year_month_list[0].append(0)

    for i in range(1, len(year_month_list)):
        next_days = calculate_days_next_month(year_month_list[i-1])
        # 前月の曜日を参照し、日数から曜日を特定する
        weekday = ((next_days-1) % 7 + year_month_list[i-1][2]) % 7
        # 曜日を年と月の組み合わせのリストに追加する
        year_month_list[i].append(weekday)

    # 20世紀、かつ、日曜日(2列目が6)になっているものを抽出する
    target_list = [a for a in year_month_list if (a[0] != 1900) & (a[2] == 6)]
    print(target_list)
    answer = len(target_list)
    print(answer)

