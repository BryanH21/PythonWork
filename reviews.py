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
def display_reviews():
    for review in reviews:
        stars = "★" * review["rating"] + "☆" * (5 - review["rating"])
        text_reviews.insert(tk.END, f"Game: {review['game']}\nReview: {review['review']}\nRating: {stars}\n{'-'*40}\n")
    text_reviews.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Game Reviews")

# Create and place the widgets
label_title = tk.Label(root, text="Game Reviews", font=("Helvetica", 16))
label_title.pack(pady=10)

text_reviews = scrolledtext.ScrolledText(root, width=60, height=20)
text_reviews.pack(pady=10)

# Display reviews
display_reviews()

# Run the application
root.mainloop()
