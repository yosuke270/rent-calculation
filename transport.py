#必要な家賃と、居住坪数を入力すれば、補助の金額を計算してcsvに出力する。
#5500円以下なら0円
#Windowsのデスクトップから実行する場合は、プロパティリンク先(T)に Python のインタープリタファイルとプログラムファイルのパスを入力。
from decimal import Decimal, ROUND_HALF_UP
import csv
import os

print("部屋の名前、URL、家賃、居住坪数を入力してください。")
room_name = input("部屋の名前:")
url = input("URL:")
rent = float(input("家賃(円) ※共益費、管理費、駐車場は含まない:"))   
area = float(input("居住面積(m^2):"))
area_tubo = float(Decimal(area / 3.3).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
area_jou = Decimal(area /1.548).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
default_subsidy = 8500
#2畳を1坪、3.3m^2を1坪とし、少数第二位を四捨五入する

if rent >= 100000:
    rent = 100000

subsidy = (rent -8500 -(1800*area_tubo))*0.325
subsidy = int(subsidy / 1000) * 1000
rent = int(rent)
if subsidy < 5500:
    subsidy = 0
elif subsidy >=35000:
    subsidy = 35000
print("補助金は", subsidy, "円です。")
actual_rent = rent - subsidy - default_subsidy
print(room_name, "の実負担額は", actual_rent, "円です。")

#以下で、部屋の名前、家賃、居住坪数、補助金、実負担額にcsvに出力する。
file_exists = os.path.isfile("rent.csv")
with open("rent.csv", "a", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["部屋の名前", "家賃", "畳", "補助金", "実負担額","URL"])
    writer.writerow([room_name, rent, area_jou, subsidy, actual_rent ,url])
        













