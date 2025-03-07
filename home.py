import tkinter as tk
from tkinter import *
import bestGamesOne  
import rateGame
import reviews

def return_to_main():
    """Return to the main menu"""
    rateGame.pack_forget()
    mainMenu.pack()

def open_best_games():
    """Open Best Games inside the same window"""
    mainMenu.pack_forget()  # Hide main menu first
    bestGamesOne.show_best_games(root, mainMenu)  # Open Best Games page

def open_rate_game():
    mainMenu.pack_forget()
    rateGame.show_rate_game(root, mainMenu)

# Initialize main window
root = tk.Tk()
root.geometry("1440x900")
root.title("Rate My Game!")

# Main menu UI
mainMenu = Frame(root)

top_header = tk.Label(mainMenu, text="Rate My Game!", font=("Arial", 48))
sub_header = tk.Label(mainMenu, text="The highest rated game this week is God of War: Ragnarok", font=("Arial", 24))

buttonRate = tk.Button(mainMenu, text="Rate a Game", command=open_rate_game)
buttonReviews = tk.Button(mainMenu, text="Reviews")
buttonBestGames = tk.Button(mainMenu, text="Best Games", command=open_best_games)

# Pack elements in the main menu
top_header.pack(pady=10)
sub_header.pack(pady=5)
buttonRate.pack(pady=5)
buttonReviews.pack(pady=5)
buttonBestGames.pack(pady=5)

# Start with the main menu properly
mainMenu.pack()

root.mainloop()
