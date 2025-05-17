birth = input("輸入你的生日(ex:20031203): ")

life = 0
for i in range(8):
    life += int(birth[i])

gift1 = life // 10
gift2 = life %  10

if life >= 10:
    life = life // 10 + life % 10

star = 0
date = int(birth[4:])

if 120 <= date and date <= 218:
    star = 2
elif 219 <= date and date <= 320:
    star = 3
elif 321 <= date and date <= 419:
    star = 1
elif 420 <= date and date <= 520:
    star = 2
elif 521 <= date and date <= 620:
    star = 3
elif 621 <= date and date <= 722:
    star = 4
elif 723 <= date and date <= 822:
    star = 5
elif 823 <= date and date <= 922:
    star = 6
elif 923 <= date and date <= 1022:
    star = 7
elif 1023 <= date and date <= 1121:
    star = 8
elif 1122 <= date and date <= 1221:
    star = 9
else:
    star = 1

for i in range(1, 4):
    for j in range(i, i+7, 3):
        show = (j == life or j == gift1 or j == gift2 or j == star)
        for k in range(8):
            show = show or (j == int(birth[k]))
        if show:
            print(j, end = ' ')
        else:
            print('·', end = ' ')
    print()