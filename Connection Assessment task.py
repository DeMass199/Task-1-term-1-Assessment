import random

def play_again_prompt():
    play_again_prompt = input("would you like another chance Type: Y for Yes or N for No: ")
    if play_again_prompt == "Y" or "y":
        main()
        return True
    elif play_again_prompt == "N" or "n":
        return True
    elif play_again_prompt not in ("Y" or "y", "N" or "n"):
        print("please type in")
        return False
    
def get_user_guesses(previous_guesses):
    # get 4 inputs 
    # these inputs must be words
    print("Beware you have to type the word exactly the way it says")
    print("Now please type in your guesses")
    
    guesses = []

    # what you really want to do, is compares guesses to any previous attempts that are correct
    for i in range(0,4):
        try:
            guess = input("Guess {}: ".format(i+1))
            # Check if the guess is already in the previous guesses
            guesses.append(guess)
        except Exception as e:
            print("Invalid input: ", e)

    return guesses, previous_guesses

def check_guess(guesses,selected_categories,correctly_guessed_categories_words):

    # you could perhaps check if they have ALREADY guessed tthat categgory before 
    for category in correctly_guessed_categories_words:
        if category == set(guesses):
            return False, "Already Guessed"

    # now it needs to check if the words are from the same category
    guesses = set(guesses) 
    category_solved = False

    for category in selected_categories:
        if guesses == set(category["words"]): # look at each list of words inside of each dictionary
            category_solved = True
            break

    if category_solved == True:
        return True, category
    else:
        print("Incorrect!")
        return False, None      

def print_words_from_categories(word_categories):
    """ 
    Loop through each category to print its words. 
    """
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories():
    """
    Initialize a list to store different categories of words and define 
    each category with a descriptive name and a list of related words
    """
    word_categories = []
    
    category1 = {
    "linking_word": "Time periods",
    "words": ["Century", "Decade", "Millennium", "Year"]
    }
    category2 = {
    "linking_word": "lazy",
    "words": ["Sloth", "Loafer", "Sleepy", "Indolent"]
    }
    category3 = {
    "linking_word": "smelly",
    "words": ["Rank", "BO", "Skunks", "Garbage"]
    }
    category4 = {
    "linking_word": "body_parts",
    "words": ["Legs", "Arms", "Fingers", "Feet"]
    }
    category5 = {
    "linking_word": "NBA_Greats",
    "words": ["Bird", "Curry", "James", "Jordan"]
    }
    category6 = {
    "linking_word": "sections of a news paper",
    "words": ["Sports", "Opinion", "Entertainment", "Headlines"]
    }
    category7 = {
    "linking_word": "Iconic video games",
    "words": ["COD Black Ops", "Minecraft", "Halo", "GoldenEye"]
    }
    category8 = {
    "linking_word": "Snack foods that can be deep fried",
    "words": ["Chips", "Egg roll", "Chicken", "Tofu"]
    }
    category9 = {
    "linking_word": "Verbs for walking heavily",
    "words": ["Stomping", "Trudging", "Hiking", "Treking"]
    }
    category10 = {
    "linking_word": "Greek Gods",
    "words": ["Zeus", " Apollo", "Hermes", "Poseidon"]
    }
    category11 = {
    "linking_word": "Nukes dropped",
    "words": ["Little Boy", "Fat Man", "Tsar Bomba", "Gilda"]
    }
    category12 = {
    "linking_word": "Breakfast food",
    "words": ["Eggs", "Bacon", "Pancakes", "Toast"]
    }
    category13 = {
    "linking_word": "Religions",
    "words": ["Christianity", "Islam", "Hinduism", "Buddhism"]
    }
    category14 = {
    "linking_word": "Poker actions",
    "words": ["Bet", "Call", "Check", "Fold"]
    }
    category15 = {
    "linking_word": "Skin types",
    "words": ["Combination", "Dry", "Normal", "Oily"]
    }
    category16 = {
    "linking_word": "Types of Beans",
    "words": ["Green", "Lima", "Pinto", "Black"]
    }
    category17 = {
    "linking_word": "Water Activites",
    "words": ["Dive", "Surf", "Swim", "Kayak"]
    }
    category18 = {
    "linking_word": "Basic Colour",
    "words": ["Red", "Green", "Yellow", "Blue"]
    }

    # category19 = {
    # "linking_word": "topic",
    # "words": ["", "", "", ""]
    # }


    word_categories.append(category1)
    word_categories.append(category2)
    word_categories.append(category3)
    word_categories.append(category4)
    word_categories.append(category5)
    word_categories.append(category6)
    word_categories.append(category7)
    word_categories.append(category8)
    word_categories.append(category9)
    word_categories.append(category10)
    word_categories.append(category11)
    word_categories.append(category12)
    word_categories.append(category13)
    word_categories.append(category14)
    word_categories.append(category15)
    word_categories.append(category16)
    word_categories.append(category17)
    word_categories.append(category18)


    # Randomly select 4 categories
    selected_categories = random.sample(word_categories, 4)
    "randomise the individual words for the array"
    "use the number to grab the categories in the array"
    "make sure it doesn't grab the same numbers twice"
    return selected_categories
# Need to add more categories
def create_empty_grid():
    """
    Create a 4x4 grid with a placeholder word in each cell.
    """
    grid_size = 4 
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append(' _ ')
        word_grid.append(row)
    return word_grid

def make_grid_look_nice(populated_grid):
    for row in populated_grid:
        print("|", end="  ")
        for cell in row:
            print(cell.center(12), end="  |  ")
        print()

def populate_grid(selected_categories, grid): 
    
    # rather than just print off empty grid, use the words in the dictionaries inside selected_categories
    # [dictionary, dictionary, dictionary, dictionary]
    # array of [word connection:values, words: values]
    row = 0
    for category in selected_categories:
        col = 0
        for word in category["words"]:
            grid[row][col] = word # put the word inside the grid
            col += 1
        row = row + 1
        
    return grid
    
def shuffle_words(grid):
# flattening the 2D grid with words in it to be 1D loop
    all_words_flat = []
    for row in grid:
        for word in row:
            all_words_flat.append(word)
# shuffling all the words around in the 1D grid
    random.shuffle(all_words_flat)
    # print(all_words_flat)

    word_index = 0
    i = 0
    j = 0
    rows = 4
    columns = 4
    grid = []
    while j < columns:
        i = 0
        row = []
        while i < rows:            
            row.append(all_words_flat[word_index])
            word_index += 1
            i = i + 1
        grid += [row]
        j+=1
    # print(grid)
    return grid

def main():
    # This is the order in which things occur
    # need to loop the main so that the user can play to game more than once without haveing to relaunch the code
    word_categories = []
    game_won = False
    correctly_guessed_categories = 0
    lives = 4
    previous_guesses = []
    correctly_guessed_categories_words = []
    selected_categories = setup_word_categories() # go and grab the 4 categories to use in the game
    grid = create_empty_grid() # creates a grid
    populated_grid = populate_grid(word_categories, grid) #populates the grid with the words from chosen categories
    unsorted_grid = populate_grid(selected_categories, grid) 
    shuffled_grid = shuffle_words(unsorted_grid) # shuffles the words in the grid 
    make_grid_look_nice(shuffled_grid)


    while lives > 0 and game_won == False:
        print(f"You have {lives} Lives remaining")
        guesses, previous_guesses = get_user_guesses(previous_guesses)
        guess_result, category_guessed = check_guess(guesses, selected_categories, correctly_guessed_categories_words)
        make_grid_look_nice(shuffled_grid)
        
        if guess_result == False and category_guessed == "Already Guessed":
            print("You have already guessed that category, try again...")
        elif guess_result == False:
            lives -= 1
        else:
            correctly_guessed_categories += 1
            category_guessed = check_guess(guesses, selected_categories,correctly_guessed_categories_words)
            print(category_guessed)
            correctly_guessed_categories_words.append(set(category_guessed[1]["words"]))
            print(f"You guessed correctly. The category you have found is {category_guessed[1]["linking_word"]}")


        if correctly_guessed_categories == 4:
            game_won = True
            print("You win the game.")
            play_again_prompt()


    if lives == 0:
        print("You ran out of Lives. Game over.")
        play_again_prompt()
main()
# Fix the update categories function
# make sure that the user cannot use the same words he has already found

    