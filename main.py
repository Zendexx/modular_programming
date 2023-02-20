import operators
import others
import trig

# x=functionss.add(5,2)
# print(x)
# y=functionss.subtract(12,9)
# print(y)
# from operators import add
# x=add(12,5)
# print(x)
# from operators import subtract
# y=subtract(12,8)
# print(y)


# building a better calculator
# getting user input
operator=input("enter operator: ")
if operator=='cube':
    num=eval(input("enter number: "))
    w=others.cube(num)
    print(w)
elif operator=='sin':
    angle=eval(input("enter angle in degrees: "))
    x=trig.get_sin(angle)
    print(x)

elif operator=='tan':
    angle=eval(input("enter angle in degrees: "))
    print(trig.get_tan(angle))

elif operator=='cosin':
    angle=eval(input("enter angle in degreees: "))
    print(trig.get_cosin(angle))
else:
    num1=eval(input("enter first number: "))
    num2=eval(input("enter second number: "))

    if operator=='+':
        x=operators.add(num1,num2)
        print(x)


    elif operator=='-':
        y=operators.subtract(num1,num2)
        print(y)

    elif operator=='/':
        z=operators.divide(num1,num2)
        print(z)

    elif operator=='*'or'x' or'X':
        x=operators.multiply(num1,num2)
        print()
