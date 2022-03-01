from tkinter import *
from turtle import *
def centeredscreen(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - 200)
    center_y = int(screen_height/2 - 200)

    # set the position of the window to the center of the screen
    root.geometry(f'400x400+{center_x}+{center_y}')

if __name__=="__main__":
    root = Tk()
    root.title("TicTaeToe")
    centeredscreen(root)
    root.resizable(False,False)
    


    root.mainloop()