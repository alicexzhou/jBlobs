# Alice Zhou and Jacqueline Young
# CS 111 Final Project
# Jelly Blobs of Doom

class Player: 
    def __init__(self, canvas, xy, wh, ink, delta):
        '''Initials the player blob class'''
        
        # Creates instance variables to reference the canvas and the speed of the blob
        self.canvas = canvas
        self.delta = delta
        
        # Creates an instance variable to reference the player blob
        self.id = self.canvas.create_oval(xy[0], xy[1], xy[0]+wh[0], xy[1]+wh[1], fill=ink, width=2)
        
    def left(self, event): # Handler for left arrow key. Ignores event arg.
        '''Moves the player blob left by 5 pixels'''
        self.canvas.move(self.id, -5, 0)
        
    def right(self, event): # Handler for right arrow key. Ignores event arg.
        '''Moves the player blob right by 5 pixels'''
        self.canvas.move(self.id, 5, 0)
        
    def up(self, event): # Handler for up arrow key. Ignores event arg.
        '''Moves the player blob up by 5 pixels'''
        self.canvas.move(self.id, 0, -5)
        
    def down(self, event): # Handler down arrow key. Ignores event arg.
        '''Moves the player blob down by 5 pixels'''        
        self.canvas.move(self.id, 0, 5)
    
        
    def move(self):
        '''Moves the player blob'''
        self.canvas.move(self.id, self.delta, 0)
    

    def getBoundingBox(self):
	return self.canvas.bbox(self.id)

  