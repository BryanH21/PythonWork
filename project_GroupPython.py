import tkinter as tk
from tkinter import *

def switchPages():
    print("Clicked!")
    mainMenu.destroy()
    rateGame.pack()
    
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
buttonBestGames = tk.Button(mainMenu, text="Best Games", command=switchPages)

testButton = tk.Button(rateGame, text="return to main menu", command=switchPages)


top_header.pack()
sub_header.pack()

buttonRate.pack()
buttonReviews.pack()
buttonBestGames.pack()
testButton.pack()

mainMenu.pack()


root.mainloop()