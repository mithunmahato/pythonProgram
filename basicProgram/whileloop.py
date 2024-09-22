while True:
    tests_available = input("Are ThousandEyes test results available? ")
    if tests_available.lower() == "yes":
        print("Tests are available, breaking away from while loop!")
        break
    else:
        print("ThousandEyes test results not available yet")