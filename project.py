print("="*30)
print("wecome to the interactive personal data collector!")
print("="*30)

#user input

name=input(" please enter your name ")
age=input(" please enter your age ")
height=float(input(" please enter your height in meters "))
number=input(" please enter your favourite number ")

print("="*30)
print("thanks! here is the infomation we collected:")
print("="*30)

print("name:",name)
print("type:",type(name))
print("memory address:",id(name))
print("age",age)
print("type:",type(age))
print("memory address:",id(age))
print("height:",height)
print("type:",type(height))
print("meight address:",id(height))
print("number:",number)
print("type:",type(number))
print("memory address:",id(number))

print("="*30)
print("thank you for using the personal data collector. good bye!")
print("="*30)
