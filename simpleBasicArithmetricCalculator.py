num1 =     int(input('Enter 1st number: '))
operator = input('Enter operator: ')
num2 =     int(input('Enter 2nd number: '))


if operator == '+':
    print ('The result of addition is: ', num1+num2)
    
elif operator == '-':
    print ('The result of subtraction is: ',num1-num2)
    
elif operator == '*':
    print ('The result of multiplication is: ', num1*num2)
    
elif operator == '/':
    print ('The result of division is: ', num1/num2)

else:
    print ('The calculator cann\'t perform the operator')
