import random

a, b = input("生成的數的區間: ").split(' ')

for i in range(5):
    print(random.randint(int(a), int(b)))

