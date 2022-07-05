from pickle import TUPLE1, TUPLE2, TUPLE3


fruits = ("apple" , "banana" ,  "cherry")
print(fruits[0])
fruits = ("apple" , "banana" ,  "cherry" , "orange" , "kiwi" , "melon" , "mango")
print(fruits[2:5])
print(fruits[:5])
print(fruits[2:])
#เพิ่มค่าใน
x = ("apple" , "banana" ,  "cherry")
y = list(x)#แปลงเปHนlistแล้วเก็บค่าเข้าy
y[1] = "kiwi"
x = tuple(y) #แปลงเป็นlistแล้วเก็บค่าเข้าy
print(x)
#ลบค่าในtuple
x = ("apple" , "banana" ,  "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#join
TUPLE1 = ("a" , "b" , "c")
TUPLE2 = (1 , 2 , 3)
TUPLE3 = TUPLE1 = TUPLE2
print(tuple)
x = range(3 , 6)
for n in x:
    print(n)
x = range(3 , 20 , 2)
for n in x:
    print("rangeแบบstep2" , n)
#กั้ณฑ์อเนก ทรงแสงธรรม เลขที่ 13