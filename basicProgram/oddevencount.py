odd_number=0
even_number=0

number=int(input("Enter 1st number :: (press 0 to exit) :: "))
while number!=0:
    if number % 2 !=1:
        odd_number+=1
    else:
        even_number+=1
    number = int(input("enter number (0 to exit):: "))
print("odd number count == ", odd_number)
print("even number count == ", even_number)