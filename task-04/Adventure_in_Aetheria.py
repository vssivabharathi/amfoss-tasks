number = int(input())  
input1 = input()
input2 = list(map(int, input1.split()))  
minimum = min(input2)  
count = input2.count(minimum)  
if count > 1:
    print("Still Aetheria")
else:
    print(input2.index(minimum) + 1)  
