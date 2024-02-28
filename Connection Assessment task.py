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
    "linking_words": "Time periods",
    "words": {"century", "decade", "millennium", "year"}
    }
    lazy_category = {
    "linking_words": "lazy",
    "words": {"sloth", "couch", "sleepy", "indolent"}
    }
    smelly_category = {
    "linking_words": "smelly",
    "words": {"rank", "BO", "skunks", "barbage"}
    }
    body_part_category = {
    "linking_words": "body_parts",
    "words": {"legs", "arms", "fingers", "feet"}
    }
    NBA_Greats_category = {
    "linking_words": "NBA_Greats",
    "words": {"Bird", "Curry", "James", "Jordan"}
    }
    news_paper_category = {
    "linking_words": "parts of a news paper",
    "words": {"sports", "opinion", "entertainment", ""}
    }
    iconic_videogame_characters_categories = {
    "linking_words": "Iconic video game characters",
    "words": {"COD black ops", "minecraft", "Halo", "GoldenEye 007"}
    }
    deep_fried_food_categories = {
    "linking_words": "deep fried foods",
    "words": {"", "", "", ""}
    }
    word_for_walking_heavily = {
    "linking_words": "deep fried foods",
    "words": {"", "", "", ""}
    }

    word_categories.append(Time_period_category)
    word_categories.append(lazy_category)
    word_categories.append(smelly_category)
    word_categories.append(body_part_category)
    word_categories.append(NBA_Greats_category)
    word_categories.append(news_paper_category)
    word_categories.append(iconic_videogame_characters_categories)
    word_categories.append(deep_fried_food_categories)
    "figure out how to used shuffle (random.shuffles)"

    return word_categories

def create_word_grid():
    """
    Create a 4x4 grid with a placeholder word in each cell.
    """
    grid_size = 4
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append('word')
        word_grid.append(row)

    return word_grid

def populate_grid(word_categories, grid):
    # do some things
    # choose 4 categories and fill the goddam grid!!!!
    populated_grid = "Test"
    return populated_grid


def full_word_grid():
    """
    Placeholder function to later populate the grid with words from categories.
    This could include random selection and placement of words.
    """
    pass


def play_game(populated_grid):
    pass

def main():
    # this is the order in which things occur
    word_categories = setup_word_categories()
    grid = create_word_grid()
    populated_grid = populate_grid(word_categories, grid)
    play_game(populated_grid)
    

main()
# Test