import csv

def menu():
    '''Displays menu whenever menu() is called'''
    print("Welcome to the best PokeDex in the World of Pokemon")
    print("1: Display Pokemon with their types and statistics")
    print("2: Display the first Pokemon of a Type of your choice")
    print("3: Display all Pokemons of a Type of your choice")
    print("4: Display all Pokemons with Total Base stat of your choice")
    print("5: Display Pokemon with a minimum set of stats")
    print("6: Display all Legendary Pokemon of specific Type1 and Type2")
    print("7: Stat comparison between two Pokemons")
    print("0: Quit")
    print()

def check_digit(check):
    '''Takes in input(check), checks if it is a digit
       If it is a digit, returns input after typecasting it to int
       Else, prints error message, returns None to check for'''
    
    if check.isnumeric(): #checks if input is number before typecasting to prevent error
        return int(check)
    else:
        print("\nInvalid input. Try again with a valid number\n") #prints message
        return None #returns None value to be checked for 

def option1():
    '''Takes in user input for number of pokemon to be displayed, and displays as such'''
    num_poke = input("Enter the number of Pokemon to be displayed: ")
    num_poke = check_digit(num_poke)
    if num_poke == None:
        return #breaks loop if words are entered instead of number
    else:
        print()
        with open("Pokemon.csv", "r", newline = "") as f:
            reader = csv.reader(f)                
            for line in range(num_poke+1): #add 1 to include header
                line = next(reader) #next reads the next line and converts it into a list
                print("{:<3}  {:<25}  {:<8}  {:<8}  {:<6}  {:<6}  {:<8}  {:<8}  {:<8}  {:<8}  {:<6}  {:<11}  {:<9}".format(*line))
            #< left alligns the element to the specified width, *data takes in the elements from the line
            # and matches them to the correct {}
    print() #adds new line for readability        

def option2():
    '''Takes in user input of a type, then displays first pokemon that matches that type'''
    type_poke = input("Enter Type: ").title()
    print()
    with open("Pokemon.csv", "r", newline="") as f:
        reader = csv.reader(f)
        data = [next(reader)] #header is alr included here by using the next function
        for line in reader:
            if type_poke in line: #checks if type is in the line 
                data.append(line)
                break
        if len(data) == 1: #if type was found, then there would be another element in list, so len should return 2
            print("No pokemon of this type")
        elif len(data) == 2: #2 cos only one pokemon
            for line in data:
                print("{:<3}  {:<25}  {:<8}  {:<8}  {:<6}  {:<6}  {:<8}  {:<8}  {:<8}  {:<8}  {:<6}  {:<11}  {:<9}".format(*line))
            #< left alligns the element to the specified width, *data takes in the elements from the line
            # and matches them to the correct {}
    print()

def option3():
    '''Takes in user input of a type, then displays all pokemon that match that type'''
    type_poke = input("Enter Type: ").title()
    print()
    with open("Pokemon.csv", "r", newline="") as f:
        reader = csv.reader(f)
        data = [next(reader)] #header is alr included here by using the next function
        for line in reader:
            if type_poke in line: #checks if type is in the line 
                data.append(line)
        if len(data) == 1: #if type was found, then there would be another element in list, so len should return 2
            print("No Pokemon of this type has been found")
        elif len(data) >= 2: #greater than 2 cos got more than 1 pokemon
            for line in data:
                print("{:<3}  {:<25}  {:<8}  {:<8}  {:<6}  {:<6}  {:<8}  {:<8}  {:<8}  {:<8}  {:<6}  {:<11}  {:<9}".format(*line))
            #< left alligns the element to the specified width, *data takes in the elements from the line
            # and matches them to the correct {}
    print()

def option4():
    '''Takes in user input for total stats, then displays all Pokemon with that Total Base Stat'''
    total_stats = input("Enter total stats: ")
    total_stats = check_digit(total_stats)
    if total_stats == None:
        return #breaks out of function
    print()
    with open("Pokemon.csv", "r", newline="") as f:
        reader = csv.reader(f)
        data = [next(reader)]
        for line in reader:
            if total_stats == int(line[4]): #checks index 4 since index of total stats is 4
                data.append(line)
        if len(data) == 1: #if pokemon was found, then there would be another element in list, so len should return >2
            print("No Pokemon with this Total Base Stat")
        elif len(data) >= 2:
            for line in data:
                print("{:<3}  {:<25}  {:<8}  {:<8}  {:<6}  {:<6}  {:<8}  {:<8}  {:<8}  {:<8}  {:<6}  {:<11}  {:<9}".format(*line))
            #< left alligns the element to the specified width, *data takes in the elements from the line
            # and matches them to the correct {}
    print()

def option5():
    '''Takes in user input for 3 diff stats, then displays all Pokemon with stats higher than or equal to the input'''
    spattack = input("Enter minimum Special Attack stat: ")
    spdefense = input("Enter minimum Special Defense stat ")
    speed = input("Enter minimum Speed stat: ")

    spattack = check_digit(spattack) #checks one by one to avoid displaying multiple error messages
    if spattack == None:
        return
    spdefense = check_digit(spdefense)
    if spdefense == None:
        return
    speed = check_digit(speed)
    if speed == None:
        return
    
    print()
    with open("Pokemon.csv", "r", newline="") as f:
        reader = csv.reader(f)
        data = [next(reader)]
        for line in reader:
            if int(line[8]) >= spattack: #nested if loop to check if each of the variables are greater than 
                if int(line[9]) >= spdefense:
                    if int(line[10]) >= speed:
                        data.append(line)
        if len(data) == 1:
            print("Such a powerful Pokemon has not been found yet")
        if len(data) >= 2:
            for line in data:
                print("{:<3}  {:<25}  {:<8}  {:<8}  {:<6}  {:<6}  {:<8}  {:<8}  {:<8}  {:<8}  {:<6}  {:<11}  {:<9}".format(*line))
            #< left alligns the element to the specified width, *data takes in the elements from the line
            # and matches them to the correct {}
    print()

def option6():
    '''Takes in user input for two types, then displays a Legendary Pokemon with both those stats'''
    type1 = input("Enter the first type: ").title()
    type2 = input("Enter the second type: ").title()
    print()
    with open("Pokemon.csv", "r", newline="") as f:
        reader = csv.reader(f)
        data = [next(reader)]
        for line in reader:
            if type1 in line: #uses nested if loop to check for both types and legendary status before appending to list
                if type2 in line:
                    if "TRUE" in line:
                        data.append(line)
        if len(data) == 1:
            print("No legendary Pokemon of this two types have been found")
        elif len(data) >= 2:
            for line in data:
                print("{:<3}  {:<25}  {:<8}  {:<8}  {:<6}  {:<6}  {:<8}  {:<8}  {:<8}  {:<8}  {:<6}  {:<11}  {:<9}".format(*line))
            #< left alligns the element to the specified width, *data takes in the elements from the line
            # and matches them to the correct {}
    print()

def option7():
    '''Takes in user input for two different Pokemon, then displays their stats in a table such that is easy to compare'''
    poke1 = input("Enter the name of the first Pokemon: ").lower()
    poke2 = input("Enter the name of the second Pokemon: ").lower()
    # .lower() is used instead of .title(), since pokemon names can have capital letters in the middle
    print()

    if poke1 == poke2: #checks for duplicates
        print("You have entered duplicate Pokemon. Please try again. ")
        print()
        return

    with open("Pokemon.csv", "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        poke1_list = None 
        poke2_list = None
        
        for line in reader: #iterates through each line to find the inputted Pokemon's data
            if poke1 == line[1].lower():
                poke1_list = line 
            elif poke2 == line[1].lower():
                poke2_list = line
        
        if poke1_list == None or poke2_list == None: # if the None value hasnt been replaced then the pokemeon hasnt been found
           print("Sorry, but either one or both of your Pokemon do not exist. Try again with Pokemon either from or before Generation 6.\n")
           return #return is used to break out of the function
    
    header.pop(0) #removes the number from the comparison since it isnt relevant
    poke1_list.pop(0)
    poke2_list.pop(0)
    
    # comparison = []
    for line1, line2, line3, in zip(header, poke1_list, poke2_list): #iterates over all 3 elements at the same time
        print(f"{line1:<11} | {line2:^26} | {line3:^26}")
    print()

option =  None #initialise option as None so that while condition is satisfied

while option != 0: # as soon as option == 0, loop is exited so that program can end
    menu() #calls menu and initialises option inside while loop so that they repeat each time
    option = input("Enter option: ")
    
    option = check_digit(option)
    if option == None:
        continue #if input is string skips over the rest of the loop for this iteration

    if option not in [1,2,3,4,5,6,7,0]: #checks if input is within the accepted range
        print("Sorry! It has not been implemented yet. Please choose a valid option from the list \n")
        continue #same reason as previous continue

    if option == 1: #calls respective function based on input
        option1()
    if option == 2:
        option2()
    if option == 3:
        option3()
    if option == 4:
        option4()
    if option == 5:
        option5()
    if option == 6:
        option6()
    if option ==7:
        option7()
            
if option == 0:
    print("Bye")
    print("Thank you for using this PokeDex!") #exits program
    input("Enter any key to exit the program")