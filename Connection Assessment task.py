import random

# def game_over():
#     pass

# def initialize_lives(num_lives):
#     lives = 4
#     num_lives = lives
#     return num_lives

# def decrease_lives(num_lives):
#     if check_guess == False:
#         if num_lives > 0:
#             num_lives -= 1
#         print("Oops! You got something wrong. Lives remaining:", num_lives)
#     else:
#         print("Game over! No lives remaining.")
#     return num_lives

# # Example usage:
# lives = initialize_lives(4)  # Initialize with 4 lives
# print("Starting lives:", lives)

# # Somewhere in your code, when something goes wrong:
# lives = decrease_lives(lives)  # Decrease lives when something goes wrong

def get_user_guesses():
    # get 4 inputs 
    # these inputs must be words
    print("Beware you have have to type the word exactly the way it says")
    print("Now please type in your guesses")
    
    guesses = []
    for i in range(0,4):
        guess = input() 
        guesses.append(guess)

    return guesses

def check_guess(guesses,word_categories):
    # now it needs to check if the words are from the same category
    # needs to say if the guesses are from the same category and greater than 3 three say there is 
    guesses = set(guesses) 
    category_solved = False

    for category in word_categories:
        if guesses == set(category["words"]): # look at each list of words inside of each dictionary
            category_solved = True
        
    if category_solved == True:
        print("You have gotten all the words for this category:  ")
        return True, category
    else:
        print("Incorrect!")
        return False, None
# need to make this check for, if three of the four words in the same catgory are correct
# Then make another else: that says if you the user has pick only 1 or 2 of the words than they will get a message that say try again           

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
    "words": ["Sloth", "Couch", "Sleepy", "Indolent"]
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
    "linking_word": "parts of a news paper",
    "words": ["sports", "Opinion", "Entertainment", "Headline"]
    }
    category7 = {
    "linking_word": "Iconic video game characters",
    "words": ["COD black ops", "Minecraft", "Halo", "GoldenEye"]
    }
    category8 = {
    "linking_word": "can / are deep fried",
    "words": ["Arancini", "Egg roll", "Chicken", "Tofu"]
    }
    category9 = {
    "linking_word": "words for walking heavily",
    "words": ["Stomping", "Rrudged", "Hiking", "Trek"]
    }
    
    word_categories.append(category1)
    word_categories.append(category2)
    word_categories.append(category3)
    word_categories.append(category4)
    word_categories.append(category5)
    word_categories.append(category6)
    word_categories.append(category7)
    word_categories.append(category8)
    word_categories.append(category9)

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

def play_game():
    pass

def update_categories():
    # take the original 4 categories defined at the beginning of the game
    # take the guesssed category that was right
    # remove the guessed category from the lsit of 4 categories
    # rebuild the grid and return
    pass

def main():
    # This is the order in which things occur
    # need to loop the main so that the user can play to game more than once without haveing to relaunch the code
    word_categories = []
    selected_categories = setup_word_categories() # go and grab the 4 categories to use in the game
    grid = create_empty_grid() # creates a grid
    populated_grid = populate_grid(word_categories, grid) #populates the grid with the words from chosen categories
    unsorted_grid = populate_grid(selected_categories, grid) 
    shuffled_grid = shuffle_words(unsorted_grid) # shuffles the words in the grid 
    make_grid_look_nice(shuffled_grid) 

    game_won = False
    guessed_categories = 0
    lives = 4
    while lives > 0 and game_won == False:
        print(f"You have {lives} guesses remaining")
        guesses = get_user_guesses()
        guess_result, category_guessed = check_guess(guesses, selected_categories)
        make_grid_look_nice(shuffled_grid)

        if guess_result == False:
            lives -= 1
        else:
            guessed_categories += 1
            print(f"You guessed correctly. The category is {category_guessed['linking_word']}")

        if guessed_categories == 4:
            game_won = True
            print("You win the game.")

    if lives == 0:
        print("You ran out of guesses. Game over.")


    # game_won = False
    # guessed_categories = 0
    # lives = 4
    # while lives > 0 and game_won == False:
    #     print(f"You have {lives} guesses remaining")
    #     guesses = get_user_guesses()
    #     guess_result, category_guessed = check_guess(guesses, selected_categories)
    #     print(shuffled_grid)


    #     if guess_result == False:
    #         lives = lives - 1
    #     else:
    #         guessed_categories += 1
    #         print(f"You guessed correctly. The category is {category_guessed}")
    #     if guessed_categories == 4:
    #         game_won = True
    #         print("You win the game.")
    


main()

# Need to create a lives function the ticks down if they get one of the word wrong