import tkinter as tk
from tkinter import *

def show_best_games(root, mainMenu):
    """ Display Best Games UI inside the same window """
    mainMenu.pack_forget()  # Hide the main menu

    # Create Best Games frame
    bestGamesFrame = tk.Frame(root, bg="#2C2F33")
    bestGamesFrame.pack(fill="both", expand=True)

    # Navigation bar
    nav_frame = tk.Frame(bestGamesFrame, bg="#23272A")
    nav_frame.pack(fill="x", pady=10)
    
    back_button = tk.Button(nav_frame, text="← Home", font=("Arial", 14), bg="#7289DA", fg="white", command=lambda: return_to_home(bestGamesFrame, mainMenu))
    back_button.pack(side="left", padx=10, pady=5)

    header = tk.Label(bestGamesFrame, text="Best Games Right Now", font=("Arial", 24, "bold"), fg="white", bg="#2C2F33")
    header.pack(pady=10)

    # Sample game data
    games = [
        {
            'name': 'Minecraft',
            'rating': 5,
            'image': 'images/minecraft1.png',
            'description': 'A thrilling adventure game set in a vast open world.',
            'reasons': ['Creative freedom', 'Endless adventure', 'Engaging gameplay'],
            'store_links': ['Store 1', 'Store 2']
        },
        {
            'name': 'Fortnite',
            'rating': 4,
            'image': 'images/fortnite1.png',
            'description': 'An action-packed battle royale with multiple game modes.',
            'reasons': ['Great combat system', 'Multiple game modes', 'Engaging multiplayer'],
            'store_links': ['Store 1', 'Store 2']
        }
    ]

    def display_game(game):
        """Display a game in the UI"""
        game_frame = tk.Frame(bestGamesFrame, bg="#23272A", padx=10, pady=10)
        game_frame.pack(pady=10, fill="x")

        # Load Image (PNG only)
        try:
            img = tk.PhotoImage(file=game['image'])
            img_label = tk.Label(game_frame, image=img, bg="#23272A")
            img_label.image = img  # Keep reference to avoid garbage collection
            img_label.pack(side="left", padx=10)
        except tk.TclError:
            img_label = tk.Label(game_frame, text="[Image Not Found]", fg="red", bg="#23272A")
            img_label.pack(side="left", padx=10)

        text_frame = tk.Frame(game_frame, bg="#23272A")
        text_frame.pack(side="left", padx=10)

        tk.Label(text_frame, text=game['name'], font=("Arial", 16, "bold"), fg="white", bg="#23272A").pack(anchor="w")
        tk.Label(text_frame, text=f"⭐ Rating: {game['rating']}", font=("Arial", 12), fg="white", bg="#23272A").pack(anchor="w")
        tk.Label(text_frame, text=game['description'], wraplength=400, justify="left", fg="white", bg="#23272A").pack(anchor="w")

        reasons_label = tk.Label(text_frame, text="Reasons to Buy:", font=("Arial", 10, "bold"), fg="white", bg="#23272A")
        reasons_label.pack(anchor="w")

        for reason in game['reasons']:
            tk.Label(text_frame, text=f"- {reason}", font=("Arial", 10), fg="white", bg="#23272A").pack(anchor="w")

        store_links = tk.Label(text_frame, text=f"Buy from: {', '.join(game['store_links'])}", fg="#7289DA", cursor="hand2", bg="#23272A")
        store_links.pack(anchor="w")

    for game in games:
        display_game(game)

def return_to_home(bestGamesFrame, mainMenu):
    """Return to Home Page"""
    bestGamesFrame.pack_forget()  # Hide Best Games page
    mainMenu.pack()  # Show the main menu again