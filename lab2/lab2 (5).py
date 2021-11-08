number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())
x = []
y = []

if number_one % 2 != 0:
    x.append(number_one)
else:
    y.append(number_one)

if number_two % 2 != 0:
    x.append(number_two)
else:
    y.append(number_two)

if number_three % 2 != 0:
    x.append(number_three)
else:
    y.append(number_three)

if number_four % 2 != 0:
    x.append(number_four)
else:
    y.append(number_four)    
print('Непарные: ', sorted(x))
print('Парные: ', sorted(y))

    
    
