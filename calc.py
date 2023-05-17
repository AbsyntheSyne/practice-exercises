def calc():
    num1 = input('Enter the first number: \n')
    num2 = input('Enter the second number: \n')
    operator = input('Enter the operator: \n')
    num1 = int(num1)
    num2 = int(num2)
    match operator:
        case '*':
            ans = num1 * num2
        case '-':
            ans = num1 - num2
        case '+':
            ans = num1 + num2
        case '/':
            ans = num1 / num2

    print("The answer is ", ans)

lick = "yes"

while lick == "Yes" or lick == "yes" :
    calc()
    lick = input('Would you like to do another? \n')
print('Have a good day!')