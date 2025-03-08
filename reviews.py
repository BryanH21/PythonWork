import tkinter as tk
from tkinter import scrolledtext

# List of reviews with star ratings
reviews = [
    {"game": "The Legend of Zelda: Breath of the Wild", "review": "An incredible open-world experience with stunning visuals and engaging gameplay.", "rating": 5},
    {"game": "The Witcher 3: Wild Hunt", "review": "A masterpiece of storytelling and character development in an expansive fantasy world.", "rating": 5},
    {"game": "Super Mario Odyssey", "review": "A joyous and inventive platformer that showcases the best of Mario's adventures.", "rating": 4},
    {"game": "Fortnite", "review": "A slowly paced game that speeds up over time. Fight to be the last one standing in this 3 person shooter.", "rating": 3},
    {"game": "Minecraft", "review": "A relaxed survival experience that focuses on surviving throughout the night, craft and build to make yourself have every advantage possible.", "rating": 4}
]

# Function to display reviews
def display_reviews(frame):
    text_reviews = scrolledtext.ScrolledText(frame, width=75, height=40, bg="#23272A", fg="white")
    text_reviews.pack(pady=10)

    for review in reviews:
        stars = "★" * review["rating"] + "☆" * (5 - review["rating"])
        text_reviews.insert(tk.END, f"Game: {review['game']}\nReview: {review['review']}\nRating: {stars}\n{'-'*40}\n")
    text_reviews.config(state=tk.DISABLED)

def show_reviews_page(root, mainMenu):
    mainMenu.pack_forget()

    # Creates the reviews frame
    reviewFrame = tk.Frame(root, bg="#2C2F33")
    reviewFrame.pack(fill="both", expand=True)

    #  Initializes and packs the navigation bar
    nav_frame = tk.Frame(reviewFrame, bg="#23272A")
    nav_frame.pack(fill="x", pady=10)
    
    back_button = tk.Button(nav_frame, text="← Home", font=("Arial", 14), bg="#7289DA", fg="white", command=lambda: return_to_home(reviewFrame, mainMenu))
    back_button.pack(side="left", padx=10, pady=5)\
    
    # Create and place title
    label_title = tk.Label(reviewFrame, text="Game Reviews", font=("Arial", 24, "bold"), fg="white", bg="#2C2F33")
    label_title.pack(pady=10)

    # Display reviews
    display_reviews(reviewFrame)


# Exits the review game page and returns to the main menu
def return_to_home(reviewFrame, mainMenu):
    """Return to Home Page"""
    reviewFrame.pack_forget()  # Hide Reviews Games page
    mainMenu.pack()  # Show the main menu again
