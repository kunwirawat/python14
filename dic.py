car = {"brand" : "ford" ,
    "model" : "Mustang" ,
    "year" : 1964
}
print(car["brand"])
print(car)
x = car.keys()
print(x)
#เพิ่มค่าในdic
car["color"] = "white"
print(car)
#แก้ค่าในdic
car["color"] = "red"
print(car)
#การupdatedic
car.update({"light":"blue"})
print(car)
#ลบค่าdic
car.pop("light")
print(car)
del car ["color"]
print(car)
#เพิ่มค่าdicแบบ list
car.update9[{"part":["body","wheel",light]}]
print(car)
#เพิ่มต่าdicแบบ Nested dic
myfamily = {
    "child1" : "Emil" ,
    "year" : "2004"
}

