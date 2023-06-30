t=int(input())
for _ in range(1,t+1):
    n=int(input())
    k=str(_)
    print("Case #"+k+":")
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
