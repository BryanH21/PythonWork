import tkinter as tk
from tkinter import ttk
import os

def return_to_home():
    root.destroy()
    os.system("python3 home.py")

# Sample game data
games = [
    {
        'name': 'Minecraft',
        'rating': 5,
        'image': 'minecraft1.png',  
        'description': 'A thrilling adventure game set in a vast open world.',
        'reasons': ['Creative freedom', 'Endless adventure', 'Engaging gameplay'],
        'store_links': ['Store 1', 'Store 2']
    },
    {
        'name': 'Fortnite',
        'rating': 4,
        'image': 'fortnite1.png',  
        'description': 'An action-packed battle royale with character customization and endless gameplay modes.',
        'reasons': ['Great combat system', 'Multiple game modes', 'Engaging multiplayer'],
        'store_links': ['Store 1', 'Store 2']
    }
]

def filter_games():
    for widget in game_frame.winfo_children():
        widget.destroy()  # Clear previous results

    for game in games:
        if game['rating'] >= 4: 
            display_game(game)

def display_game(game):
    frame = tk.Frame(game_frame, borderwidth=2, relief="ridge", padx=10, pady=10)
    frame.pack(pady=10, fill="x")

    text_frame = tk.Frame(frame)
    text_frame.pack(side="left", padx=10)

    # Load Image (only supports PNG)
    try:
        img = tk.PhotoImage(file=game['image'])  # Tkinter's built-in image handling
        img_label = tk.Label(frame, image=img)
        img_label.image = img  # Keep reference to avoid garbage collection
        img_label.pack(side="left", padx=10)
    except tk.TclError:
        img_label = tk.Label(frame, text="[Image Not Found]", fg="red")
        img_label.pack(side="left", padx=10)

    tk.Label(text_frame, text=game['name'], font=("Arial", 14, "bold")).pack(anchor="w")
    tk.Label(text_frame, text=f"⭐ Rating: {game['rating']}", font=("Arial", 12)).pack(anchor="w")
    tk.Label(text_frame, text=game['description'], wraplength=300, justify="left").pack(anchor="w")

    reasons_label = tk.Label(text_frame, text="Reasons to Buy:", font=("Arial", 10, "bold"))
    reasons_label.pack(anchor="w")

    for reason in game['reasons']:
        tk.Label(text_frame, text=f"- {reason}", font=("Arial", 10)).pack(anchor="w")

    store_links = tk.Label(text_frame, text=f"Buy from: {', '.join(game['store_links'])}", fg="blue", cursor="hand2")
    store_links.pack(anchor="w")

root = tk.Tk()
root.title("Best Games")

header = tk.Label(root, text="Best Games Right Now", font=("Arial", 18, "bold"))
header.pack(pady=10)

filter_button = tk.Button(root, text="Show Only 4 & 5 Star Games", command=filter_games)
filter_button.pack()

game_frame = tk.Frame(root)
game_frame.pack(pady=10, fill="both", expand=True)

home_button = tk.Button(root, text="Return to Home", command=return_to_home)
home_button.pack(pady=10)  

filter_games()

root.mainloop()