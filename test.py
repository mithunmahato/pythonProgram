import os

x=os.getsource(os)
print(x)

print("Programming","Essentials","in", sep = "***", end = "...")
print("Python")

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

