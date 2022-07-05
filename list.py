#การแสดงคำในlist
fruits = ["apple" , "banana" , "cherry" , "watermelon", "blueberry"]
print(fruits[1])
#เปลี่ยนค่าในlist
fruits[1] = "blackcurrent"
print(fruits[1])
#เปลี่ยนค่าในlistหลายตำแหน่ง
fruits[1:2] = ["kiwi" , "mango" , "pineapple"]
print(fruits)
fruits.append("orange")
print(fruits)
#เพิ่มในที่กำหนด
fruits.insert(3 , "grape")
print(fruits)
tropical = ["mango" , "pineapple" , "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบคำในlist
fruits.remove("watermelon")
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#ณัฐณิชา อุ่นแก้ว ชั้น 6/14 เลขที่ 37