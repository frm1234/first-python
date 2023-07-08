


def playgame():
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
            break 
        elif num >value:
            print('小一點')
            max = num - 1
        elif num < value:
            print('大一點')
            min = num + 1
        print(f'共猜了{sum}次')


while True:
    playgame()
    play = input('還要玩嗎(y/n):')
    if not (play == 'y'):
        break
print('遊戲結束')
