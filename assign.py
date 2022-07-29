import csv
import math

num_shuo = 0
num_daniel = 0
num_eric = 0

result_list = [['姓名,信箱\n'], ['姓名,信箱\n'], ['姓名,信箱\n']]

def zoom_csv_gen(shuo, dan, eric):
    pass

def check_case(f1, f2, f3):
    if f1 and f2: #金融業、科技業
        if num_shuo > num_daniel:
            return 1
        else:
            return 0
    if f1 and f3: #金融業、管顧業
        if num_shuo > num_eric:
            return 2
        else:
            return 0
    if f2 and f3: # 科技業、管顧業
        if num_daniel > num_eric:
            return 2
        else:
            return 1
    if f1:
        return 0 #金融
    if f2:
        return 1 #科技
    if f3:
        return 2 #管顧
    return -1 # Error


with open('data.csv', 'r') as f:
    rd = csv.reader(f)
    next(rd)
    for r in rd:
        res = r[8] #志願序
        gmail = r[6]
        name = r[1]
        flag1 = False
        flag2 = False
        flag3 = False
        #print(name, gmail)
        if "金融" in res: flag1 = True
        if "科技" in res: flag2 = True
        if "管顧" in res: flag3 = True
        sep = check_case(flag1, flag2, flag3)
        if sep == 0:
            num_shuo += 1
        if sep == 1:
            num_daniel += 1
        if sep == 2:
            num_eric += 1
        #print(sep)
        result_list[sep].append(name + str(',') + gmail + '\n')
        #print(result_list[sep][1])

    print('Shuo-ru 學姊房人數：', num_shuo)
    print('Daniel  學長房人數：', num_daniel)
    print('Eric    學長房人數：', num_eric)

with open('shuo_room.csv', 'w') as f:
    for s in result_list[0]:
        f.write(s)

with open('daniel_room.csv', 'w') as f:
    for s in result_list[1]:
        f.write(s)

with open('eric_room.csv', 'w') as f:
    for s in result_list[2]:
        f.write(s)
