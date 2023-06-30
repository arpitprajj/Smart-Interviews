t=int(input())
for l in range(1,t+1):
    n=int(input())
    k=n//2
    p=str(l)
    print("Case #"+p+":")
    for i in range(n):
        if i==0 or i==n-1:
            print(" "*k+"*")
        elif i<=k:
            print(" "*(k-i)+"*"+" "*(2*i-1)+"*")
        else:
            print(" "*(i-k)+"*"+" "*(2*(n-i-1)-1)+"*")
        
