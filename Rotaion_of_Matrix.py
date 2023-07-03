t=int(input())
for x in range(1,t+1):
    n=int(input())
    l=[0]*n
    x=str(x)
    print("Test Case #"+x+":")
    for i in range(n):
        l[i]=list(map(int,input().split()))
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp=l[i][j]
            l[i][j]=l[n-j-1][i]
            l[n-j-1][i]=l[n-i-1][n-1-j]
            
            l[n-i-1][n-1-j]=l[j][n-1-i]
            l[j][n-1-i]=temp
    for i in range(n):
        print(*l[i])
            
