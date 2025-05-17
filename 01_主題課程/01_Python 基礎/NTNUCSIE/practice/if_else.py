num = 100

x = int(input("guess a number(1 ~ 100): "))

if x > num:
    print("太大")
elif x < num:
    print("太小")
elif x == num:
    print("恭喜答對!")