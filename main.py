import game
import pygame
from tkinter import messagebox

try:
    pygame.init()
    game_ = game.Game()
    game_.run()
except:
    messagebox.showwarning('ERROR', '''An Unknown Error was Encountered,
Please Restart the game''')
    pygame.quit()
                      
