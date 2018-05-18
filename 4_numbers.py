#range不能生成尾数
#for value in range(1,5):
#    print(value)

#numbers = list(range(1,6))
#print(numbers)

#odd_numbers = list(range(1,12,2))
#print(odd_numbers)

#squares = []
#for value in range(1,6):
##    square = value**2
##    squares.append(square)
#    squares.append(value**2)
#print(squares)

#a = min(squares)
#b = max(squares)
#c = sum(squares)
#print(a,b,c)

#squares = [value**2 for value in range(1,6)]
#print(squares)

#threes = list(range(3,31))
#for value in threes:
#    print(value)

cubics = [value**3 for value in range(1,11)] 
print(cubics)