t=int(input())
for i in range(t):
    n=int(input())
    l=[0]*n
    m=[]
    su=0
    for i in range(n):
        l[i]=list(map(int,input().split()))
    i=0
    a=0
    while(i<n):
        j=n-i-1
        k=0
        su=0
        while(j>=0):
            if k<n and j<n:
                su+=l[k][j]
            else:
                break
        
            k+=1
            j+=1
        m.append(su)
        i+=1
        a+=1
    i=1    
    while(i<n):
        j=0
        k=i
        su=0
        while(j<n):
            if k<n and j<n:
                su+=l[k][j]
            else:
                break
            k+=1
            j+=1
        m.append(su)
        i+=1
        a+=1 
    #m.append(l[n-1][0])
    print(*m)
    
    
    
