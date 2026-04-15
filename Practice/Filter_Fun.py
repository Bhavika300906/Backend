def oddeven(x):
    if x%2==0:
        return x

l=[1,2,3,4,5,6,7,8,9,0]

ans=filter(oddeven,l)

print(list(ans))

l1=[1,12,3,14,5,16,7,18,9,20]

ans1=map(oddeven,l1)

print(list(ans1))
