import readfilms, addfilms, updatefilms, deletefilms, search

def read_file(file_path): # file_path is a parameter/variable
    try:
        with open(file_path) as readfile:
            rf = readfile.read()
        # with open(file_path) as rf:
        #     rf.read()
        return rf
    
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
# Testing file path 
# print(read_file("Python/FilmFlix Python project/menuoptions.txt"))       
        
def film_menu():
    option = 0 # initialise/assign the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"]
    # call the read_file function and assign to a variable(menu_choices)
    menu_choices = read_file("Python/FilmFlix Python project/menuoptions.txt")

    # repeat the menu options until user select the to quit
    while option not in optionsList:
        print(menu_choices) # print the menu_choices variable because it is a function
        # re-assign the option variable a string value 
        option = input("Enter an option from the menu choice above: ")

        # check if the input provided in options variable is not outside of 1,2,3,4,5,6
        if option not in optionsList:
            print(f"{option} is not a valid choice! ")
    return option

# testing 
# print(films_menu())
# create and use a boolean flag Variable

# for visual studio code v3.9.6 which doesn't yet take mactch case

mainProgram = True # toggle to False to exit out of the while loop
# ........
while mainProgram: # while True
    
     # call the songs_menu function and assign to a variable(main_menu)
    main_menu = film_menu()

    # use match case # same as swith in javascript
    if main_menu == "1":
            # call the readsong file and the function display all songs
            readfilms.all_films()
    elif main_menu == "2":
            addfilms.insert_films()
    elif main_menu == "3":
            updatefilms.update_films()
    elif main_menu == "4":
            deletefilms.delete_aFilm()
    elif main_menu == "5":
            search.search_films()
    else:
        mainProgram = False # set mainProgram = False to exit the menu
input("Press enter to exit......")