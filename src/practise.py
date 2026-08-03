

n=int(input())
f=True
for i in range(2,n//2):
    if n%i==0:
        f=False
        break
if f:
    print("Prime")
else:
    print("Not Prime")
    