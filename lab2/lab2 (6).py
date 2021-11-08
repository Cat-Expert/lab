number_one = int(input())
number_two = int(input())
number_three = int(input())

if number_one == number_two == number_three:
    print('1')
elif number_one == number_two or number_three == number_three or number_one == number_three:
    print('2')
else:
    print('3')    
    