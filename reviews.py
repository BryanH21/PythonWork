import tkinter as tk
from tkinter import scrolledtext

# List of reviews with star ratings
reviews = [
    {"game": "The Legend of Zelda: Breath of the Wild", "review": "An incredible open-world experience with stunning visuals and engaging gameplay.", "rating": 5},
    {"game": "The Witcher 3: Wild Hunt", "review": "A masterpiece of storytelling and character development in an expansive fantasy world.", "rating": 5},
    {"game": "Super Mario Odyssey", "review": "A joyous and inventive platformer that showcases the best of Mario's adventures.", "rating": 4},
    {"game": "Fortnite", "review": "A slowly paced game that speeds up over time. Fight to be the last one standing in this 3-person shooter.", "rating": 3},
    {"game": "Minecraft", "review": "A relaxed survival experience that focuses on surviving throughout the night, crafting, and building to gain advantages.", "rating": 4}
]

# Function to display reviews inside a scrollable text box
def display_reviews(frame):
    text_reviews = scrolledtext.ScrolledText(
        frame, width=75, height=20, bg="#2C2F33", fg="white",
        font=("Arial", 12), wrap=tk.WORD, borderwidth=2, relief="solid"
    )
    text_reviews.pack(pady=10, padx=20, fill="both", expand=True)

    for review in reviews:
        stars = "★" * review["rating"] + "☆" * (5 - review["rating"])
        text_reviews.insert(
            tk.END, f"🎮 Game: {review['game']}\n📝 Review: {review['review']}\n⭐ Rating: {stars}\n{'-'*50}\n\n"
        )
    
    text_reviews.config(state=tk.DISABLED)  # Make text read-only

# Function to display the reviews page
def show_reviews_page(root, mainMenu):
    mainMenu.pack_forget()  # Hide the main menu

    # Create the review frame
    reviewFrame = tk.Frame(root, bg="#23272A")
    reviewFrame.pack(fill="both", expand=True)

    # Create a navigation bar at the top
    nav_frame = tk.Frame(reviewFrame, bg="#2C2F33", height=50)
    nav_frame.pack(fill="x", pady=5)

    # Create a back button to return to the home page
    back_button = tk.Button(
        nav_frame, text="← Home", font=("Arial", 14, "bold"), bg="#A0AEC0", 
        fg="#2C2F33", relief="flat", padx=10, pady=5, bd=5, 
        command=lambda: return_to_home(reviewFrame, mainMenu)
    )
    back_button.pack(side="left", padx=10, pady=5)

    # Title label for the page
    label_title = tk.Label(
        reviewFrame, text="🎮 Game Reviews", font=("Arial", 24, "bold"), fg="white", bg="#23272A", pady=10
    )
    label_title.pack()

    # Display the reviews
    display_reviews(reviewFrame)

# Function to return to the home page
def return_to_home(reviewFrame, mainMenu):
    reviewFrame.pack_forget()  # Hide the reviews page
    mainMenu.pack()  # Show the main menu again
