t=int(input())
for __ in range(t):
    x,y=map(int,input().split())
    arr=['0']*32
    arr[31-x]='1'
    arr[31-y]='1'
    
    arr="".join(arr)
    
    print(int(arr,2)%1000000007)
