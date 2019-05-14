keychain =0
while(True):
    print("1. Add Keychain \n 2. Remove Keychain \n 3. Check Keychains \n 4. Exit")
    choice = input("Please enter your choice : ")

    if(int(choice)==1):
        print("Current No of Keychains : " + str(keychain))
        addKeychain = input("How many keychians to add? ")
        (keychain)= (keychain)+int(addKeychain)
        print("No of Keychains : " + str(keychain))

    if(int(choice)==2):
        print("Current No of Keychains : " + str(keychain))
        addKeychain = input("How many keychians to Remove? ")
        keychain= keychain-int(addKeychain)
        print("No of Keychains : " + str(keychain))

    if(int(choice)==3):
        print("Current No of Keychains : " + str(keychain))

    if (int(choice) == 4):
           exit()