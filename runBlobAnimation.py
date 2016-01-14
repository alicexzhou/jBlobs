# Alice Zhou and Jacqueline Young
# CS 111 Final Project
# Jelly Blobs of Doom

import os
import Tkinter as tk
import animation
import blob
import random
import player


WIDTH, HEIGHT = 800, 500 # Stores the width and height of the canvas in variables
SPEED = 40   # Smaller for faster, 40 means 1 frame per 40ms == 25 fps

# List of colors
colors = ['snow', 'peach puff',
    'lemon chiffon', 'mint cream','medium blue', 'royal blue',  'blue', 'dodger blue', 
    'steel blue', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan', 'cadet blue', 
    'medium aquamarine', 'dark green', 'dark olive green', 'dark sea green', 'sea green', 
    'medium sea green', 'spring green', 'lawn green', 'medium spring green', 'green yellow', 
    'lime green', 'yellow green','forest green', 'pale goldenrod', 'light goldenrod yellow', 
    'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark salmon', 'salmon', 'orange', 
    'dark orange', 'coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink',
    'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 
    'purple', 'medium purple', 'thistle','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 
    'turquoise1', 'cyan4', 'aquamarine2','SeaGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3',
    'SpringGreen4', 'green2','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 
    'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 
    'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1','IndianRed1', 'salmon1', 'salmon2', 
    'salmon3', 'salmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 
    'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 
    'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red4', 'DeepPink2', 'DeepPink3', 
    'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4','pink3', 'pink4', 'maroon1',
    'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'magenta4', 'orchid1', 'plum4',
    'MediumOrchid1', 'DarkOrchid4', 'purple1', 'thistle1']
    
    

class App(tk.Frame):
    
    def __init__(self, myroot):
        '''Initializes the entire game'''
        
        myroot.title("Jelly Blobs of Doom")
        self.frame = tk.Frame(myroot) 
        self.frame.pack()
        # Creates the canvas from the imported animation file
        self.canvas = animation.AnimationCanvas(self.frame, width=WIDTH, height=HEIGHT, bg='SkyBlue1') 
        self.canvas.pack()
 
        # Creates the player and sets the coordinates, width, height, color, and speed
        self.player = player.Player(self.canvas, (100,200), (60,30), 'darkblue', 0)
        
        # Binds events to specific keys and calls corresponding method
        myroot.bind('<Left>', self.player.left)
        myroot.bind('<Right>', self.player.right) 
        myroot.bind('<Up>', self.player.up)
        myroot.bind('<Down>', self.player.down)
        myroot.bind('<space>', self.restart)
        
        # Invokes addBlob function to add the enemy blobs
        self.addBlob() 
        # Starts the animation
        self.canvas.start()
        
    def restart(self, event):
        '''Returns the game back to its original condition'''
        
        # Accesses all the items on the canvas in a list
        allBlobs = self.canvas.items[:]
        
        # Removes each blob in allBlobs
        for enemyBlob in allBlobs:
            self.canvas.removeItem(enemyBlob)
        # Deletes the text from the canvas
        self.canvas.delete(self.textId)
        
        # Starts the function that creates enemy blobs 
        self.addBlob() 
        # Starts the animation
        self.canvas.start()
        
        # Returns the player to its original size and starting point
        self.canvas.coords(self.player.id, (70,185,130,215))        

        
        
    def addBlob(self):
        '''Creates the enemy blobs with random colors, starting points, sizes, and speeds'''
        
        # Width between 1 and 200 inclusive is chosen randomly
        width = random.randint(1,200)
        # Height of enemy blob is always half the width
        height = width/2
        
        # Blobs have a 50% chance to appear from the left 
        if random.randint(0,1) == 0:  
            # Adds blob to canvas with random starting position from the left, with random width, height, color, and speed
            self.canvas.addItem(blob.Blob(self.canvas, self.player, self, (-800, random.randrange(HEIGHT)), (width, height), random.choice(colors), random.randint(2, 7)))
            # Adds the blob every 1500 milliseconds
            self.canvas.after(1500, self.addBlob)
        
        # Blobs have a 50% chance to appear from the right 
        else: 
            # Adds blob to canvas with random starting position from the right, with random width, height, color, and speed
            self.canvas.addItem(blob.Blob(self.canvas, self.player, self, (805, random.randrange(HEIGHT)), (width, height), random.choice(colors), random.randint(-7, -2)))
            # Adds the blob every 1500 milliseconds
            self.canvas.after(1500, self.addBlob)
   
   
    
root = tk.Tk()
app = App(root)
# For Macs only: Bring root window to the front
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to True' ''')

root.mainloop() 

