#!/usr/local/bin/python3

def avg(*args):
    total=sum(args)
    avg = total/len(args)
    return float(avg)

print(avg(2,5,7))