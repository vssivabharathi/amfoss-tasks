n=int(input())

for _ in range(n):
    value1="amfoss"
    value2= input().lower()
    count = 0
    
    for i in range (len(value1)):
        if value1[i] != value2[i]:
            count += 1
          

    print(count)
