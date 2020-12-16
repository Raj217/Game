import game
import pygame
from tkinter import messagebox
import tkinter

root = tkinter.Tk()
root.withdraw()
try:
    if game.DEVELOPER == "Rajdristant Ghose":
        pygame.init()
        game_ = game.Game()
        game_.run()
    else:
        raise Exception
except:
    messagebox.showwarning('ERROR', '''An Unknown Error was Encountered,
Please Restart the game''')
    pygame.quit()
