import tkinter as tk
from tkinter import *
import bestGamesOne  
import rateGame
import reviews

def open_best_games():
    """Open Best Games inside the same window"""
    mainMenu.pack_forget()  # Hide main menu first
    bestGamesOne.show_best_games(root, mainMenu)  # Open Best Games page

def open_rate_game():
    mainMenu.pack_forget()
    rateGame.show_rate_game(root, mainMenu)

def open_reviews():
    mainMenu.pack_forget()
    reviews.show_reviews_page(root, mainMenu)

# Initialize main window
root = tk.Tk()
root.geometry("1440x900")
root.config(bg="#2C2F33")
root.title("Rate My Game!")

# Main menu UI
mainMenu = Frame(root, bg="#2C2F33")

top_header = tk.Label(mainMenu, text="Rate My Game!", font=("Arial", 48, "bold"), fg="white", bg="#2C2F33")
sub_header = tk.Label(mainMenu, text="The highest rated game this week is Minecraft", font=("Arial", 24), fg="white", bg="#2C2F33")

buttonRate = tk.Button(mainMenu, text="Rate a Game", font=("Arial", 14), bg="#7289DA", fg="white", command=open_rate_game)
buttonReviews = tk.Button(mainMenu, font=("Arial", 14), bg="#7289DA", fg="white", text="Recent Reviews", command=open_reviews)
buttonBestGames = tk.Button(mainMenu, font=("Arial", 14), bg="#7289DA", fg="white", text="Best Games", command=open_best_games)

# Pack elements in the main menu
top_header.pack(pady=10)
sub_header.pack(pady=5)
buttonRate.pack(pady=5)
buttonReviews.pack(pady=5)
buttonBestGames.pack(pady=5)

# Start with the main menu properly
mainMenu.pack(fill="both", expand=True)

root.mainloop()
