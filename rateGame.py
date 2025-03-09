import tkinter as tk
from tkinter import *
from tkinter import messagebox  #  Added for error handling and alerts
import reviews

gameselected_ = False  # Tracks if a game has been selected
ratingselected_ = False  # Tracks if a rating has been selected

def show_rate_game(root, mainMenu):
    """Displays the Rate Game page and hides the main menu."""
    global gameselected_
    gameselected_ = False
    global ratingselected_
    ratingselected_ = False
    mainMenu.pack_forget()  # Hide the main menu

    # Create the Rate Game frame
    rateGameFrame = tk.Frame(root, bg="#2C2F33")
    rateGameFrame.pack(fill="both", expand=True)

    # Create navigation bar
    nav_frame = tk.Frame(rateGameFrame, bg="#23272A")
    nav_frame.pack(fill="x", pady=10)
    
    back_button = tk.Button(nav_frame, text="← Home", font=("Arial", 14), bg="#7289DA", fg="white", 
                            command=lambda: return_to_home(rateGameFrame, mainMenu))
    back_button.pack(side="left", padx=10, pady=5)

    header = tk.Label(rateGameFrame, text="Rate Game", font=("Arial", 24, "bold"), fg="white", bg="#2C2F33")
    header.pack(pady=10)

    # Added game options list for user to select from
    gameoptionslist = [
        "The Legend of Zelda: Breath of the Wild", "The Witcher 3: Wild Hunt", 
        "Super Mario Odyssey", "Fortnite", "Minecraft"
    ]
    selectedgame = tk.StringVar()
    selectedgame.set("Choose a game to rate")

    gameoption = tk.OptionMenu(rateGameFrame, selectedgame, *gameoptionslist, command=gameselected)
    gameoption.pack(pady=10)

    # Added review text box with defined dimensions
    gamereview = tk.Text(rateGameFrame, height=5, width=50)
    gamereview.pack(pady=20)

    # Rating selection dropdown
    rating = [1, 2, 3, 4, 5]
    selectedrating = tk.StringVar()
    selectedrating.set("Choose a rating")

    chooserating = tk.Label(rateGameFrame, text="Choose a rating on a scale of 1 to 5", font=("Arial", 14), fg="white", bg="#2C2F33")
    chooserating.pack()

    ratingoption = tk.OptionMenu(rateGameFrame, selectedrating, *rating, command=ratingselected)
    ratingoption.pack(pady=20)

    #  Added secure input validation to ensure correct user input
    global submitreview 
    submitreview = tk.Button(rateGameFrame, text="Submit Review", font=("Arial", 14), bg="#7289DA", fg="white", 
                             command=lambda: submit_rating(rateGameFrame, mainMenu, selectedgame, gamereview, selectedrating))
    submitreview.pack()

def return_to_home(rateGameFrame, mainMenu):
    """Returns to the main menu from the Rate Game page."""
    rateGameFrame.pack_forget()
    mainMenu.pack()

#  Added input validation and error handling
def submit_rating(root, mainMenu, gametext, reviewtext, ratingtext):
    """Handles review submission with validation checks."""
    global gameselected_
    global ratingselected_

    game = gametext.get()
    review = reviewtext.get("1.0", "end").strip()
    rating = ratingtext.get()

    #  Check if a game has been selected
    if game == "Choose a game to rate":
        messagebox.showerror("Input Error", "Please select a game.")  #  Added error message
        return

    #  Check if review text is empty
    if not review:
        messagebox.showerror("Input Error", "Review cannot be empty.")  #  Added error message
        return

    # Validate that a valid rating is selected
    if rating not in ['1', '2', '3', '4', '5']:
        messagebox.showerror("Input Error", "Please select a valid rating.")  # Added error message
        return

    # If all inputs are valid, save the review
    newData = {'game': game, 'review': review, 'rating': int(rating)}
    reviews.reviews.append(newData)
    messagebox.showinfo("Success", "Your review has been submitted!")  # Added success confirmation
    return_to_home(root, mainMenu)

def gameselected(value):
    """Marks that a game has been selected."""
    global gameselected_
    gameselected_ = True

def ratingselected(value):
    """Marks that a rating has been selected."""
    global ratingselected_
    ratingselected_ = True