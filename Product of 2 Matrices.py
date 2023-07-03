t=int(input())
for _ in range(t):
    n1,m1=map(int,input().split())
    a=[[0]*m1]*n1
    for i in range(n1):
        a[i]=list(map(int,input().split()))
    n2,m2=map(int,input().split())
    b=[[0]*m2]*n2
    for i in range(n2):
        b[i]=list(map(int,input().split()))
    if m1!=n2:
        print("Not Possible")
    else:
        c=[[0]*m2]*n1
        for i in range(n1):
            
            for j in range(m2):
                z=0
                
                for k in range(n2):
                    z+=a[i][k]*b[k][j]
                #c[i][j]=z
                print(z,end=" ")
                z=0
            print()
                   
