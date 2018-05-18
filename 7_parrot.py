#input()获取字符串输入
#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print("hello " + name.title() + "!")

#int()获取数值输入
#age = input("how old are you? ")
#age = int(age)
#if age >=18: 
#    print(age)

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#if number % 2 == 0:
#    print("\nThe number " + str(number) + " is even.")
#else:
#    print("\nThe number " + str(number) + " is odd.")

#car = input("which car would you like? ")
#print("let me see if i can find a " + car.title())

number = input("how many people?\n " )
number = int(number)
if number >= 8:
    print("not empty")
elif number < 8:
    print("empty")