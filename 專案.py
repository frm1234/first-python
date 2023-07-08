

import random

min = 1
max = 100
value = random.randint(min,max)
print(value)
sum = 0

while True:
    num = int(input(f'猜數字範圍{min}~{max}值'))
    sum += 1
    if num == value :
        print(f'猜對了，答案是{value}')
        print(f'共猜了{sum}')
        print('win')
       #break 
        a = input('是否在玩一次?(yse/no)')
        if a == 'yes':
            min = 1
            max = 100
            sum = 0
        else:
            break
    elif num >value:
        print('小一點')
        max = num - 1
    elif num < value:
        print('大一點')
        min = num + 1
    print(f'共猜了{sum}次')



