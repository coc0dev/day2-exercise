# # Simple Calculator
# print("_________________________________________________________________________")
# print("\nUse this calculator to Add, Subtract, Multiply or Divide a whole number.")
# print("\nType 'quit' to exit the calculator.")
# active = True
# while active:
# 	number1 = int(input("\nchoose a  whole number: "))
# 	operator = (input("\nchoose an operator: "))
# 	number2 = int(input("\nchoose a second whole number: "))
# 	if operator == '+':
# 		answer = number1 + number2
# 		print("\nAnswer: " + str(answer))
# 	if operator == '-':
# 		answer = number1 - number2
# 		print("\nAnswer: " + str(answer))
# 	if operator == '*':
# 		answer = number1 * number2
# 		print("\nAnswer: " + str(answer))
# 	if operator == '/':
# 		answer = number1 / number2
# 		print("\nAnswer: " + str(answer))
# 	leave = input("Continue? (y/n): ")
# 	if leave == "n":
# 		active = False

# Pyramid
def pyramid(x):
    z = x - 1
    for i in range(0, x): # creates the number of rows
     
        for r in range(0, z): # makes the spaces before the x
            print(end=" ")
        z = z - 1
     
        for r in range(0, i + 1): # x then a space before the line ends
            print("x ", end="")
     
        print("\r")
 
x = 10
pyramid(x)