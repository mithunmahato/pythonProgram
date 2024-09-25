blocks=int(input("Enter block number :: "))

height=0
in_layer=1
while in_layer<=blocks:
    height+=1
    blocks-=in_layer
    in_layer+=1
print("Height",height)
