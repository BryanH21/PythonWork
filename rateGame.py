import tkinter as tk
from tkinter import *
from tkinter import ttk
import reviews

gameselected_ = False # This value shows whether or not a game to rate has been selected
ratingselected_ = False # This value shows whether or not a rating has been selected

# Both of the variables above must be set to True in order to submit a review

def show_rate_game(root, mainMenu):
    # Hides the main menu page, resets gameselected_ and ratingselected_ back to their defaults, and begins initalizing and packing the rate game page
    global gameselected_ 
    gameselected_ = False
    global ratingselected_ 
    ratingselected_ = False
    mainMenu.pack_forget()

    rateGameFrame = tk.Frame(root, bg="#2C2F33")
    rateGameFrame.pack(fill="both", expand=True)

    #  Initializes and packs the navigation bar
    nav_frame = tk.Frame(rateGameFrame, bg="#23272A")
    nav_frame.pack(fill="x", pady=10)
    
    back_button = tk.Button(nav_frame, text="← Home", font=("Arial", 14), bg="#7289DA", fg="white", command=lambda: return_to_home(rateGameFrame, mainMenu))
    back_button.pack(side="left", padx=10, pady=5)

    #  Initializes and packs the header
    header = tk.Label(rateGameFrame, text="Rate Game", font=("Arial", 24, "bold"), fg="white", bg="#2C2F33")
    header.pack(pady=10)

    # Initializes and packs the list of registered games to rate
    gameoptionslist = ["The Legend of Zelda: Breath of the Wild", "The Witcher 3: Wild Hunt", "Super Mario Odyssey", "Fortnite", "Minecraft"]
    selectedgame = tk.StringVar()
    selectedgame.set("Choose a game to rate")

    gameoption = tk.OptionMenu(rateGameFrame, selectedgame, *gameoptionslist, command=gameselected)
    gameoption.pack(pady=10)

    # Initializes and packs the review textbox
    gamereview = tk.Text(rateGameFrame)
    gamereview.pack(pady=20)

    # Initializes and packs the rating selection
    rating = [1, 2, 3, 4, 5]
    selectedrating = tk.StringVar()
    selectedrating.set("Choose a rating")
    
    chooserating = tk.Label(rateGameFrame, text="Choose a rating on a scale of 1 to 5", font=("Arial", 14), fg="white", bg="#2C2F33")
    chooserating.pack()

    ratingoption = tk.OptionMenu(rateGameFrame, selectedrating, *rating, command=ratingselected)
    ratingoption.pack(pady=20)

    # Initializes and packs the submit rating button
    global submitreview 
    submitreview = tk.Button(rateGameFrame, text="Submit Review", font=("Arial", 14), bg="#7289DA", fg="white", command=lambda: submit_rating(rateGameFrame, mainMenu, selectedgame.get(), gamereview.get("1.0", "end"), selectedrating.get()))
    submitreview.pack()

# Exits the rate game page and returns to the main menu
def return_to_home(rateGameFrame, mainMenu):
    """Return to Home Page"""
    rateGameFrame.pack_forget()  # Hide Best Games page
    mainMenu.pack()  # Show the main menu again

# Adds the review to a list in the reviews page
def submit_rating(root, mainMenu, gametext, reviewtext, ratingtext):
    global gameselected_
    global ratingselected_
    if gameselected_ and ratingselected_ == True:
        reviews.reviews.append(gametext)
        reviews.reviews.append(reviewtext)
        reviews.reviews.append(ratingtext)
        print(gametext)
        print(reviewtext)
        print(ratingtext)
        return_to_home(root, mainMenu)

# Executes when a game has been selected
def gameselected(value):
    global gameselected_
    global ratingselected_
    gameselected_ = True

# Executes when a rating has been selected
def ratingselected(value):
    global ratingselected_
    global gameselected_
    ratingselected_ = True
    # I think we should save ratings to a text file to make them easier to access and so that user-submitted reviews aren't erased upon closing the program