import random

def get_user_guesses():
    # get 4 inputs 
    # these inputs must be words
    print("Please type in your guesses")
    
    guesses = []
    for i in range(0,4):
        guess = input() 
        guesses.append(guess)

    return guesses

def check_guess(guesses, categories):
    # Need to change "categories" to the words in the "wordlist" / dictionary words
    for x in guesses:
        print(x, end = " ")
        print()
    for i in range(len(guesses)):
        if guesses[i] == categories[i]:
            print("????",end ="")
        elif guesses[i] in categories:
            print("????",end="")
        else:
            print("",end="")
             
      #if word present return true else return false
    if guesses == categories:
        return 1
    else:
        return 0

#    print(guesses)
#    print(selected_categories)
#    for word in guesses:
#        for category in selected_categories:
#            for item in category:
#                if word == item:
#                    print("Found a word")
                   
    # how do i compare the contents of two lists and check if they contain all of the same
    # items, doesnt matter the order
    # for i in range (0, len(list)):
    # if list[i][0]==searchstring:
    # list[i][4]=do_a_bunch_of_stuff

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
    "words": ["COD black ops", "Minecraft", "Halo", "GoldenEye 007"]
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
    # category_1, category_2, category_3, category_4 = selected_catgeories
    # 4_categories = []
    # for category in selected_categories:
    #     for word in category['words']:
    #         4_categories.append(word)
    # return 4_categories, [category_1, category_2, category_3, category_4], category_1, category_2, category_3, category_4

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
    # print(grid)
    return grid

def play_game():
    pass

def main():
    # this is the order in which things occur
    word_categories = []
    selected_categories = setup_word_categories() # go and grab the 4 categories to use in the game
    grid = create_word_grid() # creates a grid
    populated_grid = populate_grid(word_categories, grid) #populates the grid with the words from chosen categories
    unsorted_grid = populate_grid(selected_categories, grid) 
    shuffled_grid = shuffle_words(unsorted_grid) # shuffles the words in the grid
    print(shuffled_grid) 
    # play_game()
    guesses = get_user_guesses()
    check_guess(guesses, word_categories)

    # if check_guess(guesses, shuffled_grid):
    #     print("Your guess contains one of the keywords")
    # else:
    #     print("Your guess does not contain any keywords.")
            # compare them against the guess list/ categories
    
main()

# compare the category in categories
# i need to make the dictionary / word catgories easily accessible to the rest of my code through defining the four categories chosen in "selected_categories" 
#an example: selected_categories(category_1, category_2, category_3, category_4) 
# this will make it easier to cross check the answer in "check_guess"