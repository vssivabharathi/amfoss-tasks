s = input()
hello = "hello"
index = 0
for char in s:
    if char == hello[index]:
        index += 1
        if index == len(hello):
            print("YES")
            break
if index < len(hello):
    print("NO")