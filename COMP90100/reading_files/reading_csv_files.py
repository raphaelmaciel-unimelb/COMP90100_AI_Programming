# import csv
# visitors = open("COMP90100/vic_visitors.csv")
# data = csv.reader(visitors)
# header = next(data)
# for row in data:
#     total = 0
#     cols = 0
#     for entry in row[1:]:
#         print(f"{entry}")
#         total = total + float(entry)
#         cols += 1
#     print(f"{row[0]}: {total/cols:.0f} : {total:.0f} : {cols}")
# visitors.close()

# import csv
# visitors = open("COMP90100/vic_visitors.csv")
# data = csv.reader(visitors)
# data_2d = list(data)
# print(data_2d[3][2])
# visitors.close()

# import csv
# cities = open("COMP90100/city_rainfall.csv")
# print(csv.DictReader(cities))
# for row in csv.DictReader(cities):
#     total = 0
#     for month in ("Jun", "Jul", "Aug"):
#         total = total + float(row[month])
#     print(f"{row['city']}: {total/3:.0f}")
# cities.close()

import csv
data_2d = [[1, 2, 3], [4, 5, 6]]
csv_file = open("COMP90100/2d-data.csv", "w")
writer = csv.writer(csv_file)
writer.writerows(data_2d)
csv_file.close()

csv_file = open("COMP90100/2d-data.csv", "r")
print(csv_file.read())
csv_file.close()