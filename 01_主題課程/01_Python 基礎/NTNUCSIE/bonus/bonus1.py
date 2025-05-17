x = input("輸入你的生日（ex:20031203）: ")

LifePathNumber = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) + int(x[4]) + int(x[5]) + int(x[6]) + int(x[7])
print(f"{x[0]}+{x[1]}+{x[2]}+{x[3]}+{x[4]}+{x[5]}+{x[6]}+{x[7]} = {LifePathNumber}")

if LifePathNumber >= 10:
    strLifePathNumber = str(LifePathNumber)
    LifePathNumber = int(strLifePathNumber[0]) + int(strLifePathNumber[1])
    print(f"{strLifePathNumber[0]} + {strLifePathNumber[1]} = {LifePathNumber}")

print(f"你是生命靈數 {LifePathNumber} 號人")


