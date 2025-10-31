import os, json, pprint, csv

# path = "files"
# file_name = "data.json"

# os.makedirs(path, exist_ok = True)
# file_name = os.path.join(path, file_name)

# data = [
#   {'name': 'Tom', 'age': 24, 'phone': '258 693 254'},
#   {'name': 'Jane', 'age': 31, 'phone': '147 325 189'},
#   {'name': 'John', 'age': 29, 'phone': '410 189 239'},
# ]

# with open(file_name, mode = "w", encoding = "utf-8") as f:
#     filecontent = f.write(json.dumps(data, indent=2))

# with open(file_name, mode = "r", encoding = "utf-8") as f:
#     filecontent = json.loads(f.read())

# pprint.pp(filecontent)

# path = "files"
# file_name = "data.csv"

# os.makedirs(path, exist_ok = True)
# file_name = os.path.join(path, file_name)

# head = ['Name', 'Age', 'Phone']
# data = [
#   ['John', '56', '856 635 125'],
#   ['Jane', '49', '187 058 327'],
#   ['Tim', '47', '200 001 510'],
#   ['Tom', '50', '436 741 189'],
# ]

# with open(file_name, mode = "w", encoding="utf-8") as file:
#     writer = csv.writer(file)

#     writer.writerow(head)
#     writer.writerows(data)

# with open(file_name, mode = "r", encoding="utf-8") as file:
#     reader = csv.reader(file)

    # print(reader)
    # for x in reader:
    #     print(f"{x[0]:<10}{x[1]:<10}{x[2]}")
    #     print("-"*45)
    # for x in reader:
    #     if x[0] == "Tim" and int(x[1])<=19:
    #         print(x[2])


path2 = 'files2'
filename2 = 'data2.csv'

os.makedirs(path2, exist_ok=True)
filename2 = os.path.join(path2, filename2)

data = [
  {'name': 'Dato', 'age': 25, 'phone': "555 80 70 50"},
  {'name': 'Nika', 'age': 23, 'phone': "595 15 18 21"},
  {'name': 'Koba', 'age': 27, 'phone': "557 98 97 96"},
  {'name': 'Lika', 'age': 22, 'phone': "599 90 95 00"},
]
 
# head = ["name", "age", "phone"]

with open(filename2, mode = 'a', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())

    writer.writeheader()
    writer.writerows(data)

    writer.writerow({"name" : "Elene", "age" : 23, "phone" : "122 20 13 21"})

# path2 = 'files2'
# filename2 = 'data2.csv'

# os.makedirs(path2, exist_ok=True)
# filename2 = os.path.join(path2, filename2)


# with open(filename2, mode = 'r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
    
#     w1 = 10
#     w2 = 10
#     lines = 36
#     count = 0
#     for x in reader:
#         if count == 0:
#             head = tuple(x.keys())
#             print(f" {head[0]:<{w1}}{head[1]:<{w2}}{head[2]}")
#             count += 1
#         # print(f" {x['name']:<{w1}}{x['age']:<{w2}}{x['phone']}")
#         # print("-"*lines)
        










