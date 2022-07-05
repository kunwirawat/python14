student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for i in student:
    if i["score"]>= 80:
        print(i["name"],"score","grade 4")
    elif 79 >= i["score"] >= 70:
        print(i["name"],"score","grade 3")
    elif 69 >= i["score"] >= 60:
        print(i["name"],"score","grade 2")
    elif 59 >= i["score"] >= 50:
        print(i["name"],"score","grade 1")
    elif i["score"] < 50:
        print(i["name"],"score","grade 0")
#กุญช์วีรวัชร์ สังข์ชัย เลขที่ 30 