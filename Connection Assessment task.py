import random

def check_guess(guess, category ):
    for category in categories:
        print("it worked")
        # print the words only
        # compare them against the guess list

def get_user_guesses():
    # get 4 inputs 
    # these inputs must be words
    print("Please type in your guesses")
    
    guesses = []
    for i in range(0,4):
        guess = input() 
        guesses.append(guess)

    print(guesses)


    return guesses

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
    
    Time_period_category = {
    "linking_word": "Time periods",
    "words": ["Century", "Decade", "Millennium", "Year"]
    }
    lazy_category = {
    "linking_word": "lazy",
    "words": ["Sloth", "Couch", "Sleepy", "Indolent"]
    }
    smelly_category = {
    "linking_word": "smelly",
    "words": ["Rank", "BO", "Skunks", "Garbage"]
    }
    body_part_category = {
    "linking_word": "body_parts",
    "words": ["Legs", "Arms", "Fingers", "Feet"]
    }
    NBA_Greats_category = {
    "linking_word": "NBA_Greats",
    "words": ["Bird", "Curry", "James", "Jordan"]
    }
    news_paper_category = {
    "linking_word": "parts of a news paper",
    "words": ["sports", "Opinion", "Entertainment", "Headline"]
    }
    iconic_videogame_characters_categories = {
    "linking_word": "Iconic video game characters",
    "words": ["COD black ops", "Minecraft", "Halo", "GoldenEye 007"]
    }
    deep_fried_food_categories = {
    "linking_word": "can / are deep fried",
    "words": ["Arancini", "Egg roll", "Chicken", "Tofu"]
    }
    word_for_walking_heavily = {
    "linking_word": "words for walking heavily",
    "words": ["Stomping", "Rrudged", "Hiking", "Trek"]
    }
    

    word_categories.append(Time_period_category)
    word_categories.append(lazy_category)
    word_categories.append(smelly_category)
    word_categories.append(body_part_category)
    word_categories.append(NBA_Greats_category)
    word_categories.append(news_paper_category)
    word_categories.append(iconic_videogame_characters_categories)
    word_categories.append(deep_fried_food_categories)
    word_categories.append(word_for_walking_heavily)

    # Randomly select 4 categories
    selected_categories = random.sample(word_categories, 4)
    # Print the randomly selected categories
    # for category in selected_categories:
    #    print(f"Words: {category['words']}")

    "randomise the individual words for the array"
    "use the number to grab the categories in the array"
    "make sure it doesn't grab the same numbers twice"
    return selected_categories

def create_word_grid():
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
    return grid

def play_game(populated_grid):
    pass

def main():
    # this is the order in which things occur
    selected_categories = setup_word_categories() # go and grab the 4 categories to use in the game
    grid = create_word_grid()
    unsorted_grid = populate_grid(selected_categories, grid)
    shuffled_grid = shuffle_words(unsorted_grid)
    get_user_guesses()
    check_guess(guess, category)


    # print(grid)
    # populated_grid = populate_grid(word_categories, grid)
    # play_game(populated_grid)
    # grid = create_word_grid()
    # for row in grid:
    #     print(row)
    

main()

# compare the category in categories