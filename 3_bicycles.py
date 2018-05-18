#bicycles = ["trek","cannondale","redline","specialized"]
#print(bicycles)
#print(bicycles[0].title())

#names = ['a','b','c','d']
#print(names [0] + " , how are you?")
#print(names [-2] + " , how are you?")
#print(names [-1] + " , how are you?")
#print(names [-1] + " , how are you?")

#message = "My first bicycle was a " + bicycles[-1].title() + "."
#print(message)

#修改
#print(bicycles)
#bicycles[2] = "bmw"
#print(bicycles)

#增加
#print(bicycles)
#bicycles.append("bmw")
#print(bicycles)

car = []
car.append("benz")
car.append("volkswagen")
car.append("bmw")
car.append("ferrari")
print(car)

#插入
#car.insert(2,"ford")
#print(car)

#del删除
del car[-3]
#del car[:]
print(car)

#pop删除
#pop默认弹出最后一个元素
#popped_car = car.pop(-2)
#print(car)
#print(popped_car)
#print("The last car I owned was a " + popped_car.upper() + ".")

#remove删除
#car.remove("bmw")
#print(car)

#expensive = "bmw"
#car.remove(expensive)
#print(car)
#print("\nA " + expensive.title() + " is too expensive for me.")