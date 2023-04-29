import csv
import random

# 設定參數
num_workshops = 3
workshop_capacities = {'學長姐經驗分享(在學、畢業)：實習、研究所、就業': 30, 
                       'AI的應用——以chatGPT為例': 50, 
                       '履歷面試技巧分享': 30}
# 設定ANSI escape codes
COLOR_YELLOW = "\033[33m"
COLOR_RESET = "\033[0m"

# 讀入csv並排除重複填寫同一工作坊的學生
students = []
duplicates = []
total_students = 0
with open('跨域日學生志願.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        first_choice = row['第一志願']
        second_choice = row['第二志願']
        third_choice = row['第三志願']
        workshop_set = set([first_choice, second_choice, third_choice])
        if len(workshop_set) < 3:
            duplicates.append(row)
        else:
            students.append(row)
            total_students += 1
print(f"總學生數：{total_students}")
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 輸出重複填寫的學生
if len(duplicates) > 0:
    print("以下學生重複填寫同一個工作坊：")
    for student in duplicates:
        print(student['姓名'], student['第一志願'], student['第二志願'], student['第三志願'])
else:
    print("所有學生的三個志願都不重複。")
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 分配學生到工作坊
first_choice_count = {k: 0 for k in workshop_capacities.keys()}
second_choice_count = {k: 0 for k in workshop_capacities.keys()}
third_choice_count = {k: 0 for k in workshop_capacities.keys()}
random.shuffle(students)#隨機排列 list
for student in students:
    for i, choice in enumerate(['第一志願', '第二志願', '第三志願']):
        workshop = student[choice]
        if workshop in workshop_capacities and workshop_capacities[workshop] > 0:
            student['最終分配結果'] = workshop
            workshop_capacities[workshop] -= 1
            index = i + 1
            if index == 1:
                first_choice_count[workshop] += 1
            elif index == 2:
                second_choice_count[workshop] += 1
            else:
                third_choice_count[workshop] += 1
            break
    else:
        student['最終分配結果'] = 'N/A'
        print(f"{student['姓名']} 未被分配到任何志願")
        continue
    print(f"{student['姓名']} 被分配到了 {student['最終分配結果']} 工作坊（第 {index} 志願）")
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 輸出分配到第一、第二、第三志願的人數
print("分配到第一志願的人數：")
for workshop_name, count in first_choice_count.items():
    print(f"{workshop_name}: {count}")
print("分配到第二志願的人數：")
for workshop_name, count in second_choice_count.items():
    print(f"{workshop_name}: {count}")
print("分配到第三志願的人數：")
for workshop_name, count in third_choice_count.items():
    print(f"{workshop_name}: {count}")
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 輸出最終結果為第一、第二、第三志願的人數
first_choice_result_count = 0
second_choice_result_count = 0
third_choice_result_count = 0
for student in students:
    if student['最終分配結果'] == 'N/A':
        continue
    if student['最終分配結果'] == student['第一志願']:
        first_choice_result_count += 1
    elif student['最終分配結果'] == student['第二志願']:
        second_choice_result_count += 1
    elif student['最終分配結果'] == student['第三志願']:
        third_choice_result_count += 1
print("最終結果為第一志願的人數：", first_choice_result_count)
print("最終結果為第二志願的人數：", second_choice_result_count)
print("最終結果為第三志願的人數：", third_choice_result_count)
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 輸出剩餘工作坊容量
print("剩餘工作坊容量:")
for i, capacity in enumerate(list(workshop_capacities.values())):
    workshop_name = list(workshop_capacities.keys())[i]
    print(f"{workshop_name}: {capacity}")
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 檢查是否需要進行第二階段分配
over_capacity = [i for i, cap in enumerate(workshop_capacities.values()) if cap < 0]
if len(over_capacity) > 0:
    print("以下工作坊已超過容量，需要進行第二階段分配：")
    for i in over_capacity:
        workshop_name = list(workshop_capacities.keys())[i]
        print(f"{workshop_name} 超過容量 {workshop_capacities[workshop_name]} 人")
    for student in students:
        if student['最終分配結果'] == list(workshop_capacities.keys())[over_capacity[0]] and student['第二志願'] != list(workshop_capacities.keys())[over_capacity[0]]:
            workshop_index = list(workshop_capacities.keys()).index(student['第二志願'])
            if workshop_capacities[list(workshop_capacities.keys())[workshop_index]] > 0:
                student['最終分配結果'] = student['第二志願']
                workshop_capacities[list(workshop_capacities.keys())[workshop_index]] -= 1
        elif student['最終分配結果'] == list(workshop_capacities.keys())[over_capacity[0]] and student['第二志願'] == list(workshop_capacities.keys())[over_capacity[0]] and student['第一志願'] != list(workshop_capacities.keys())[over_capacity[0]]:
            workshop_index = list(workshop_capacities.keys()).index(student['第一志願'])
            if workshop_capacities[list(workshop_capacities.keys())[workshop_index]] > 0:
                student['最終分配結果'] = student['第一志願']
                workshop_capacities[list(workshop_capacities.keys())[workshop_index]] -= 1
else:
    print("沒有工作坊超過容量")
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

for workshop_name, capacity in workshop_capacities.items():
    print(f"{workshop_name}：")
    for student in students:
        if student['最終分配結果'] == workshop_name:
            print(student['姓名'])
print(f"{COLOR_YELLOW}{'-'*50}{COLOR_RESET}")

# 將結果寫入新的CSV檔案
with open('跨域日學生志願分發結果.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['姓名', '第一志願', '第二志願', '第三志願', '最終分配結果'])
    writer.writeheader()
    for student in students:
        writer.writerow(student)

print("學生分配完成，結果輸出至「跨域日學生志願分發結果.csv」")
