t=int(input())
for i in range(t):
    n1=input().split()
    if int(n1[1])%int(n1[0])==0:
        print("Yes")
    else:
        print("No")