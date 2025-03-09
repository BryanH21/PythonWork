import tkinter as tk
from tkinter import Frame
import bestGamesOne  
import rateGame
import reviews

# Function to open the Best Games page
def open_best_games():
    mainMenu.pack_forget()  # Hide the main menu
    bestGamesOne.show_best_games(root, mainMenu)  # Show the Best Games page

# Function to open the Rate a Game page
def open_rate_game():
    mainMenu.pack_forget()  # Hide the main menu
    rateGame.show_rate_game(root, mainMenu)  # Show the Rate Game page

# Function to open the Reviews page
def open_reviews():
    mainMenu.pack_forget()  # Hide the main menu
    reviews.show_reviews_page(root, mainMenu)  # Show the Reviews page

# Initialize the main window
root = tk.Tk()
root.geometry("1440x900")  # Set the window size
root.config(bg="#2C2F33")  # Set the background color to dark gray
root.title("Rate My Game!")  # Set the title of the application

# Create the main menu frame
mainMenu = Frame(root, bg="#2C2F33")

# Header Labels
top_header = tk.Label(mainMenu, text="Rate My Game!", font=("Arial", 48, "bold"), fg="white", bg="#2C2F33")
sub_header = tk.Label(mainMenu, text="The highest-rated game this week is Minecraft", font=("Arial", 24), fg="white", bg="#2C2F33")

# Define a common button style for a modern look
button_style = {
    "font": ("Arial", 18),  # Set font size
    "bg": "#A0AEC0",  # Light gray button background
    "fg": "#2C2F33",  # Dark gray text for better contrast
    "width": 20,  # Set button width
    "height": 2,  # Set button height
    "relief": "flat",  # Flat button style
    "bd": 5  # Slightly rounded edges
}

# Create buttons for navigation
buttonRate = tk.Button(mainMenu, text="Rate a Game", command=open_rate_game, **button_style)
buttonReviews = tk.Button(mainMenu, text="Recent Reviews", command=open_reviews, **button_style)
buttonBestGames = tk.Button(mainMenu, text="Best Games", command=open_best_games, **button_style)

# Pack UI elements into the main menu
top_header.pack(pady=20)  # Add space around the header
sub_header.pack(pady=10)  # Add space below the header
buttonRate.pack(pady=10)  # Add space between buttons
buttonReviews.pack(pady=10)
buttonBestGames.pack(pady=10)

# Display the main menu
mainMenu.pack(fill="both", expand=True)

# Start the main event loop
root.mainloop()
