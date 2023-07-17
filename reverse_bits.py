t=int(input())
for _ in range(t):
    n=int(input())
    n=bin(n)
    re=n[-1:1:-1]
    re=re+(32-len(re))*'0'
    print(int(re,2))
