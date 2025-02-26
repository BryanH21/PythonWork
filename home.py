import tkinter as tk
from tkinter import *
import subprocess

def switchPages():
    print("Clicked!")
    mainMenu.pack_forget() # I changhed to allow returning to home
    rateGame.pack()

def return_to_main():
    rateGame.pack_forget()
    mainMenu.pack()

def open_best_games():
    subprocess.Popen(["python3", "bestGamesOne.py"]) #opens best games
    
root = tk.Tk()
root.geometry(f"{1440}x{900}")
root.title("Rate My Game!")

mainMenu = Frame(root)
rateGame = Frame(root)

top_header = tk.Label(mainMenu, text="Rate My Game!")
top_header.config(font =("Arial", 48))

sub_header = tk.Label(mainMenu, text="The highest rated game this week is God of War: Ragnarok")
sub_header.config(font =("Arial", 24))

buttonRate = tk.Button(mainMenu, text="Rate a Game", command=switchPages)
buttonReviews = tk.Button(mainMenu, text="Reviews", command=switchPages)
buttonBestGames = tk.Button(mainMenu, text="Best Games", command=open_best_games)

testButton = tk.Button(rateGame, text="return to main menu", command=return_to_main)


top_header.pack()
sub_header.pack()

buttonRate.pack()
buttonReviews.pack()
buttonBestGames.pack()
testButton.pack()

mainMenu.pack()


root.mainloop()
