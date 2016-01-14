# Alice Zhou and Jacqueline Young
# CS111 Final Project
# Jelly Blobs of Doom

import animation

class Blob(animation.AnimatedObject):

    def __init__(self, canvas, player, app, xy, wh, ink, delta):
        '''Initializes the enemy blob class; defines the canvas, speed, blob, and player'''
        self.canvas = canvas
        self.app = app
        self.delta = delta
        self.id = self.canvas.create_oval(xy[0], xy[1], xy[0]+wh[0], xy[1]+wh[1], fill=ink, width=0)   
        self.player = player
 
        
    def doRectanglesIntersect(self, arect, brect):
        '''Checks to see if the two inputted bounding boxes (player and enemy blob) intersect'''
        (aleft, atop, aright, abottom) = arect
        (bleft, btop, bright, bbottom) = brect
        return (aleft <= bright and bleft <= aright 
            and atop <= bbottom and btop <= abottom)
    
                    
    def move(self):
        '''Defines how the player blob reacts to different sizes of enemy blobs'''
        # Moves the enemy blobs
        self.canvas.move(self.id, self.delta, 0)
        
        # Finds the bounding box tuple (four elements) of the player and corresponding width
        playerBoundingBox = self.player.getBoundingBox()
        widthPlayer = playerBoundingBox[2] - playerBoundingBox[0]
        
        # Finds the bounding box tuple (four elements) of the enemy blobs and corresponding width
        blobBoundingBox = self.getBoundingBox()
        widthBlob = blobBoundingBox[2] - blobBoundingBox[0]
        
        # Calls the function otherSide so the player appears on the other side of the screen if they go off screen
        self.otherSide()
        
        # If the player and enemy collide
        if self.doRectanglesIntersect(playerBoundingBox, blobBoundingBox):
            # If the player's width is larger than or equal to the enemy's width
            if widthPlayer >= widthBlob: 
                # Removes the enemy blob   
                self.removeBlob()
                # Scales the player's blob to be 10% larger
                self.canvas.coords(self.player.id,self.scaleBy(1.1, playerBoundingBox))
                # Checks if the size of the player is large enough to win
                self.winOrLose()
                
            # If the player's width is smaller than the enemy's width
            elif widthPlayer < widthBlob:
                self.removeBlob()
                # Scales the player's blob to be 30% smaller
                self.canvas.coords(self.player.id,self.scaleBy(.7, playerBoundingBox))
                # Checks if the size of the player is small enough to lose
                self.winOrLose()
     
                           
    def scaleBy(self, factor, bbox):
        '''Scales the player blob so that the aspect ratio of the player blob remains the same throughout the game'''
        # Finds the bounding box and corresponding width and height of the player
        playerBoundingBox = self.player.getBoundingBox()
        width = playerBoundingBox[2] - playerBoundingBox[0]
        height = playerBoundingBox[3] - playerBoundingBox[1]
        
        # Stores the tuple elements in individual variables
        (l,t,r,b) = bbox
        # Calculates the new left, top, right, and bottom coordinates
        lNew = l-((factor*width)/2 - width/2)
        tNew = t-((factor*height)/2 - height/2)
        rNew = r + ((factor*width)/2 - width/2)
        bNew = b + ((factor*height)/2 - height/2)

        return (lNew,tNew, rNew, bNew)

        
    def removeBlob(self):
        '''Removes the blob from the canvas'''
        self.canvas.removeItem(self)      
       
         
    def getBoundingBox(self):
        '''Finds the bounding box of the given blob'''
	return self.canvas.bbox(self.id)
    
    
    def otherSide(self):
        '''Mmoves the player blob to the other size of the screen if it goes off screen in a given direction'''
        
        # Finds the bounding box of the player
        playerBoundingBox = self.player.getBoundingBox()
        
        # If the player goes completely off screen, change the coordinates to move the player to the opposite side of the screen
        if playerBoundingBox[2] <= 0:
            self.canvas.coords(self.player.id, (playerBoundingBox[0]+800,playerBoundingBox[1],playerBoundingBox[2]+800,playerBoundingBox[3]))
        elif playerBoundingBox[0] >= 800:
            self.canvas.coords(self.player.id, (playerBoundingBox[0]-800,playerBoundingBox[1],playerBoundingBox[2]-800,playerBoundingBox[3]))
        elif playerBoundingBox[3] <= 0:
            self.canvas.coords(self.player.id, (playerBoundingBox[0],playerBoundingBox[1]+500,playerBoundingBox[2],playerBoundingBox[3]+500))
        elif playerBoundingBox[1] >= 500:
            self.canvas.coords(self.player.id, (playerBoundingBox[0],playerBoundingBox[1]-500,playerBoundingBox[2],playerBoundingBox[3]-500))  
	
	
    def winOrLose(self):
        '''Checks to see if the player is past a maximum or minimum width in order to determine if game is won or lost'''
        
        # Finds the bounding box and corresponding width of the player
        playerBoundingBox = self.player.getBoundingBox()
        width = playerBoundingBox[2] - playerBoundingBox[0]
        
        # If the player width is greater than one third of the canvas width
        if width >= 800/3:
            # Stops the animation
            self.canvas.stop() 
            # Creates and positions win text     
            self.app.textId = self.canvas.create_text(400, 225)
            # Adds text to canvas
            self.canvas.itemconfig(self.app.textId, text="\t   You win! :) \nPress the space bar to play again", font = ('Levenim MT', 30))

        # If the player width is less than or equal to 20
        elif width <= 20:
            # Stops the animation
            self.canvas.stop()
            # Creates and positions lose text 
            self.app.textId = self.canvas.create_text(400, 225)
            # Adds text to canvas
            self.canvas.itemconfig(self.app.textId, text="\t   You lose. :( \nPress the space bar to play again", font = ('Levenim MT', 30))

