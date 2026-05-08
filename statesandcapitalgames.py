# Elias Mandeville
# Thursday, 10.2.25
# 

def main():
    # Declare and initialize variables
    # strings for name and menuchoice
    userName = menuChoice = ""
    
    # Display Title/Intro
    print("WELCOME TO THE CAPITAL PROGRAM!!\n")
    
    # Prompt for name
    userName = input("First, let me get your name: ")
    
    # Display menu of state options
    print("\nPlease choose from the following menu: ")
    print("A) PA \nB) SC \nC) GA \nD) FL")
    
    # Prompt for menuchoice
    menuChoice = input("\nEnter your choice here: ") #"A"
    
    # Selection structure to determine which capital to display to user
    if menuChoice == "A" or menuChoice == "a":
        print("The capital of Pennsylvania is Hassisonburg")
    elif menuChoice =="B" or menuChoice == "b":
        print("The capital of South Carolia is Columbia")
    elif menuChoice == "C" or menuChoice == "c":
        print("The capital of Georgia is Atlanta")
    elif menuChoice == "D" or menuChoice == "d":
        print("The capital of Florida is Tallahassee")
    else:
        print("Sorry, you must choose A,B,C, OR D,")
        
    
    # Display outro
    print(f"\nThank you mande14 for playing my state capitals game!")


# Call main function
main()
