list1 = []
lines = int(input())

for i in range(lines):
    msg = input()
    list1.append(msg)

print(list1)

for i in list1:
    parts = i.split()
    print(int(parts[0]) * str(parts[1]))

