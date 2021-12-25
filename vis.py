import tkinter as tk
from tkinter import ttk
import enviroment # Change this to the actual learning
import math

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600

BOX_SIZE = 100
GAP_SIZE = 10

class LearningUI:
    
    def __init__(self, master):
        # Create instance of the learning sim
        self.states,self.q_s = enviroment.run((5, 1), 'PGreedy', 0.30, 0.5, 0) # ***Change this to the actual one
        
        
        self.frameMain = tk.Frame(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bd=1)
        self.frameMain.pack(side=tk.LEFT)
        self.canvasLeft = tk.Canvas(self.frameMain, width=CANVAS_WIDTH/2, height=CANVAS_HEIGHT, bg = "white")
        self.canvasLeft.pack(side=tk.LEFT, fill=tk.BOTH)
        self.canvasRight = tk.Canvas(self.frameMain, width=CANVAS_WIDTH/2, height=CANVAS_HEIGHT, bg = "white")
        self.canvasRight.pack(side=tk.LEFT, fill=tk.BOTH)


        self.controlsFrame = tk.Frame(master, width=400, height=CANVAS_HEIGHT, bd=2, relief=tk.RAISED)
        self.controlsFrame.pack(side=tk.RIGHT, fill=tk.BOTH)
       
        
        # Forward Flight Simulation Tab

        self.varStep = tk.StringVar()  
        self.scaleStep = tk.Scale(self.controlsFrame,
                variable   = self.varStep,    # MVC-Model-Part value holder
                from_      =  0,       # MVC-Model-Part value-min-limit
                to         = 5500,       # MVC-Model-Part value-max-limit
                length     =  600,         # MVC-Visual-Part layout geometry [px]
                digits     =    1,         # MVC-Visual-Part presentation trick
                resolution =  1,       # MVC-Controller-Part stepping
                command    = self.SetStep
                )
       
        
        self.scaleStep.pack(side=tk.TOP)
        
        #self.Draw()
        
    def Draw(self):
        self.canvasLeft.delete(tk.ALL)
        self.canvasRight.delete(tk.ALL)
        
        # Draw the q values on the left
        self.DrawGridSquares(self.canvasLeft, True)
        
        for col in range (5):
            for row in range(5):
                
                x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
                x1 = x0 + BOX_SIZE
                y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
                y1 = y0 + BOX_SIZE
          
                self.canvasLeft.create_polygon(x0, y0, x1, y0, (x0+x1)//2, (y0 +y1)//2, width=1, fill="purple")#pickup purple
                self.canvasLeft.create_polygon(x0, y1, x1, y1, (x0+x1)//2, (y0 +y1)//2, width=1, fill="red")#pickup purple
        #self.canvasLeft.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        
        # Draw the cells on the right
        self.DrawGridSquares(self.canvasRight)
        # Get the board state
        step = int(self.varStep.get())

        state = self.GetState(step)
        q_s = self.GetQs(step)
        
        row = state[0] - 1
        col = state[1] - 1
        #function draws the triangle and picks the value
        
        
        col = 5 - 1
        row = 3 - 1
        count = state[3]
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
          
        self.canvasRight.create_rectangle(x0, y0, x1, y1, width=1, fill="purple")#pickup purple
        self.canvasRight.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        
        col = 2 - 1
        row = 4 - 1
        count = state[4]
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
          
        self.canvasRight.create_rectangle(x0, y0, x1, y1, width=1, fill="purple")#pickup purple
        self.canvasRight.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        #[(3,5)],pickup_blocks[(4,2)],dropoff_blocks[(1, 1)], dropoff_blocks[(1, 5)], dropoff_blocks[(3, 3)], dropoff_blocks[(5, 5)]))
        
        col = 1 - 1
        row = 1 - 1
        count = state[5]
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
          
        self.canvasRight.create_rectangle(x0, y0, x1, y1, width=1, fill="yellow")#dropoff purple
        self.canvasRight.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        
        col = 5 - 1
        row = 1 - 1
        count = state[6]
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
          
        self.canvasRight.create_rectangle(x0, y0, x1, y1, width=1, fill="yellow")#dropoff purple
        self.canvasRight.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        
        col = 3 - 1
        row = 3 - 1
        count = state[7]
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
          
        self.canvasRight.create_rectangle(x0, y0, x1, y1, width=1, fill="yellow")#dropoff purple
        self.canvasRight.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        
        col = 5 - 1
        row = 5 - 1
        count = state[8]
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
          
        self.canvasRight.create_rectangle(x0, y0, x1, y1, width=1, fill="yellow")#dropoff purple
        self.canvasRight.create_text(x0+GAP_SIZE, y0+GAP_SIZE, text=str(count))
        
        
        row = state[0] - 1
        col = state[1] - 1
        carry = state[2] == 1
        x0 = GAP_SIZE + col * (GAP_SIZE + BOX_SIZE)
        x1 = x0 + BOX_SIZE
        y0 = GAP_SIZE + row * (GAP_SIZE + BOX_SIZE)
        y1 = y0 + BOX_SIZE
        
        if carry:
            self.canvasRight.create_oval(x0, y0, x1, y1, width=1, fill="green")
            
        else:
            self.canvasRight.create_oval(x0, y0, x1, y1, width=1, fill="red")
            
        for idy in range(5):
            y0 = GAP_SIZE + idy * (GAP_SIZE + BOX_SIZE) + BOX_SIZE//2
            for idx in range(5):
                x0 = GAP_SIZE + idx * (GAP_SIZE + BOX_SIZE) + BOX_SIZE//2
                self.canvasRight.create_text(x0, y0, text="({},{})".format(idy+1,idx+1))
        
    def DrawGridSquares(self, canvas, crossed = False):
        
        for idy in range(5):
            y0 = GAP_SIZE + idy * (GAP_SIZE + BOX_SIZE)
            y1 = y0 + BOX_SIZE
            for idx in range(5):
                x0 = GAP_SIZE + idx * (GAP_SIZE + BOX_SIZE)
                x1 = x0 + BOX_SIZE
                
                canvas.create_line(x0,y0,x1,y0, width=1, dash=(2,4), fill="#242424")
                canvas.create_line(x1,y0,x1,y1, width=1, dash=(2,4), fill="#242424")
                canvas.create_line(x1,y1,x0,y1, width=1, dash=(2,4), fill="#242424")
                canvas.create_line(x0,y1,x0,y0, width=1, dash=(2,4), fill="#242424")
                
                if crossed:
                    canvas.create_line(x0,y0,x1,y1, width=1, dash=(2,4), fill="#242424")
                    canvas.create_line(x1,y0,x0,y1, width=1, dash=(2,4), fill="#242424")
        
    
    
    def SetStep(self, value):

        self.Draw()
    
    def GetState(self, step):
        if step < 0:
            step = 0
        elif step >= len(self.states):
            step = -1

        return self.states[step]
    
    def GetQs(self, step):
        if step < 0:
            step = 0
        elif step >= len(self.q_s):
            step = -1

        return self.q_s[step]
        
root = tk.Tk()
root.title("Group Learning Assignment v0.1")
app = LearningUI(root)

root.mainloop()
#root.destroy()