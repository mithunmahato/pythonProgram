largest_number = -999999

number=int(input("Enter 1st number (enter -1 to exit :: "))

while number != -1:
    if number > largest_number:
        largest_number=number
    number=int(input("Enter a number ( press -1 to esit) :: "))
print("largest number :: ", largest_number)