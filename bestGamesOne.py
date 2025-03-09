import tkinter as tk
from tkinter import *

def show_best_games(root, mainMenu):
    """Displays the Best Games page and hides the main menu."""
    mainMenu.pack_forget()  # Hide the main menu

    # Create the Best Games frame
    bestGamesFrame = tk.Frame(root, bg="#2C2F33")
    bestGamesFrame.pack(fill="both", expand=True)

    # Create the navigation bar
    nav_frame = tk.Frame(bestGamesFrame, bg="#23272A")
    nav_frame.pack(fill="x", pady=10)
    
    # Back button to return to home page
    back_button = tk.Button(nav_frame, text="← Home", font=("Arial", 14), bg="#7289DA", fg="white", 
                            command=lambda: return_to_home(bestGamesFrame, mainMenu))
    back_button.pack(side="left", padx=10, pady=5)

    # Page header label
    header = tk.Label(bestGamesFrame, text="Best Games Right Now", font=("Arial", 24, "bold"), fg="white", bg="#2C2F33")
    header.pack(pady=10)

    # List of games with details
    games = [
        {
            'name': 'Minecraft',
            'rating': 5,
            'image': 'images/minecraft1.png',  # Added image path
            'description': 'A thrilling adventure game set in a vast open world.',
            'reasons': ['Creative freedom', 'Endless adventure', 'Engaging gameplay'],
            'store_links': ['Store 1', 'Store 2']
        },
        {
            'name': 'Fortnite',
            'rating': 4,
            'image': 'images/fortnite1.png',  # Added image path
            'description': 'An action-packed battle royale with multiple game modes.',
            'reasons': ['Great combat system', 'Multiple game modes', 'Engaging multiplayer'],
            'store_links': ['Store 1', 'Store 2']
        }
    ]

    def display_game(game):
        """Displays individual game information including name, rating, description, and an image."""
        game_frame = tk.Frame(bestGamesFrame, bg="#23272A", padx=10, pady=10)
        game_frame.pack(pady=10, fill="x")

        # Added: Attempt to load the image, otherwise display an alternate text
        try:
            img = tk.PhotoImage(file=game['image'])
            img_label = tk.Label(game_frame, image=img, bg="#23272A")
            img_label.image = img  
            img_label.pack(side="left", padx=10)
        except tk.TclError:
            img_label = tk.Label(game_frame, text="⚠️ [Image Not Found]", fg="red", bg="#23272A")  # Added alternate text
            img_label.pack(side="left", padx=10)

        # Create a text frame for game details
        text_frame = tk.Frame(game_frame, bg="#23272A")
        text_frame.pack(side="left", padx=10)

        # Game title
        tk.Label(text_frame, text=game['name'], font=("Arial", 16, "bold"), fg="white", bg="#23272A").pack(anchor="w")

        # Game rating
        tk.Label(text_frame, text=f"⭐ Rating: {game['rating']}", font=("Arial", 12), fg="white", bg="#23272A").pack(anchor="w")

        # Game description
        tk.Label(text_frame, text=game['description'], wraplength=400, justify="left", fg="white", bg="#23272A").pack(anchor="w")

        # Reasons to buy
        reasons_label = tk.Label(text_frame, text="Reasons to Buy:", font=("Arial", 10, "bold"), fg="white", bg="#23272A")
        reasons_label.pack(anchor="w")

        for reason in game['reasons']:
            tk.Label(text_frame, text=f"- {reason}", font=("Arial", 10), fg="white", bg="#23272A").pack(anchor="w")

        # Store links (Clickable)
        store_links = tk.Label(text_frame, text=f"Buy from: {', '.join(game['store_links'])}", fg="#7289DA", cursor="hand2", bg="#23272A")
        store_links.pack(anchor="w")

    # Loop through and display each game
    for game in games:
        display_game(game)

def return_to_home(bestGamesFrame, mainMenu):
    """Hides the Best Games page and returns to the main menu."""
    bestGamesFrame.pack_forget()
    mainMenu.pack()