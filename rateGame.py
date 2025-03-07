import tkinter as tk
from tkinter import *
from tkinter import ttk
import reviews

def clicked():
    print("game selected")

def show_rate_game(root, mainMenu):
    mainMenu.pack_forget()

    rateGameFrame = tk.Frame(root, bg="#2C2F33")
    rateGameFrame.pack(fill="both", expand=True)

    # Navigation bar
    nav_frame = tk.Frame(rateGameFrame, bg="#23272A")
    nav_frame.pack(fill="x", pady=10)
    
    back_button = tk.Button(nav_frame, text="← Home", font=("Arial", 14), bg="#7289DA", fg="white", command=lambda: return_to_home(rateGameFrame, mainMenu))
    back_button.pack(side="left", padx=10, pady=5)

    # Header
    header = tk.Label(rateGameFrame, text="Rate Game", font=("Arial", 24, "bold"), fg="white", bg="#2C2F33")
    header.pack(pady=10)

    # List of registered games to rate
    gameoptionslist = ["The Legend of Zelda: Breath of the Wild", "The Witcher 3: Wild Hunt", "Super Mario Odyssey", "Fortnite", "Minecraft"]
    selectedgame = tk.StringVar()
    selectedgame.set("Choose a game to rate")

    gameoption = tk.OptionMenu(rateGameFrame, selectedgame, *gameoptionslist)
    gameoption.pack(pady=10)

    # Review textbox
    gamereview = tk.Text(rateGameFrame)
    gamereview.pack(pady=20)

    # Rating selection
    rating = [1, 2, 3, 4, 5]
    selectedrating = tk.StringVar()
    selectedrating.set("Choose a rating")
    
    chooserating = tk.Label(rateGameFrame, text="Choose a rating on a scale of 1 to 5", font=("Arial", 14), fg="white", bg="#2C2F33")
    chooserating.pack()

    ratingoption = tk.OptionMenu(rateGameFrame, selectedrating, *rating)
    ratingoption.pack(pady=20)

    # Submit rating button
    submitreview = tk.Button(rateGameFrame, text="Submit Review", font=("Arial", 14), bg="#7289DA", fg="white", command=lambda: submit_rating(rateGameFrame, mainMenu, selectedgame.get(), gamereview.get("1.0", "end"), selectedrating.get()))
    submitreview.pack()

def return_to_home(rateGameFrame, mainMenu):
    """Return to Home Page"""
    rateGameFrame.pack_forget()  # Hide Best Games page
    mainMenu.pack()  # Show the main menu again

def submit_rating(root, mainMenu, game, review, rating):
    print(game)
    print(review)
    print(rating)
    return_to_home(root, mainMenu)
    # I think we should save ratings to a text file to make them easier to access and so that user-submitted reviews aren't erased upon closing the program