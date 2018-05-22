check_address = input("Is your address correct(yes/no)? ")
if check_address == "yes":
    print("Thanks. Your address has been saved")
else:
    del("address")
    print("Your address has been deleted. Try again")