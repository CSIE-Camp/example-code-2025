grade = [0, 0, 0, 0, 0]

for i in range(5):
    grade[i] = int(input(f"輸入第 {i+1} 個同學的成績: "))

print("90分以上有")
for i in range(5):
    if grade[i] >= 90:
        print(f"{i+1} 號")

