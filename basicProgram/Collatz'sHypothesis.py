c0=int(input("Enter a number :: "))
count=0
while c0>1:
    if c0 % 2 == 0:
        c0=c0//2
    elif c0%2!=0:
        c0=3*c0 + 1
    count +=count
    print(c0)
print("Count", count)
