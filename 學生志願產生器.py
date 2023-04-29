import csv
import random

# 建立學生名單
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack",
            "Kelly", "Leo", "Mary", "Nancy", "Oliver", "Peter", "Queenie", "Rose", "Sam", "Tom",
            "Una", "Victor", "Wendy", "Xavier", "Yvonne", "Zoe", "Amy", "Ben", "Cathy", "Danny",
            "Emily", "Fred", "George", "Hannah", "Isaac", "Julia", "Kevin", "Linda", "Mike", "Nina",
            "Oscar", "Patty", "Quentin", "Rita", "Sophie", "Tina", "Ulysses", "Vivian", "Winnie",
            "Xander", "Ying", "Zack", "Amanda", "Brian", "Carol", "Daniel", "Ellen", "Fiona",
            "Greg", "Helen", "Iris", "Jackie", "Kurt", "Lily", "Mark", "Nora", "Owen", "Paula",
            "Queen", "Roger", "Samantha", "Toby", "Uma", "Vera", "Walt", "Xena", "Yuki", "Zara",
            "Annie", "Barry", "Chloe", "David", "Elaine", "Faye", "Gordon", "Heather", "Isabel",
            "Jeff", "Katie", "Lucy", "Maggie", "Nick", "Olive", "Penelope", "Quincy", "Rachel",
            "Sara", "Tiffany", "Una", "Vincent", "Wendy", "Xavier", "Yvette", "Zachary"]

# 建立志願清單
majors = ["履歷面試技巧分享", "學長姐經驗分享(在學、畢業)：實習、研究所、就業", "AI的應用——以chatGPT為例"]

# 隨機生成每位學生的志願
data = []
for student in students:
    major1 = random.choice(majors)
    majors2 = majors.copy()
    majors2.remove(major1)
    major2 = random.choice(majors2)
    majors3 = majors2.copy()
    majors3.remove(major2)
    major3 = random.choice(majors3)
    data.append([student, major1, major2, major3])

# 寫入CSV檔案
with open("跨域日學生志願.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '第一志願', '第二志願', '第三志願'])
    writer.writerows(data)
    print("已輸出至跨域日學生志願.csv")
