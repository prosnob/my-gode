import tkinter

# 1 - Crate a window
window = tkinter.Tk()

# 2 - Set size
window.geometry("500x300")

# 3 - Create a frame
frame = tkinter.Frame()

#  Set the tile
frame.master.title("MY PICTURE")

# Create the cavas to draw
canvas = tkinter.Canvas(frame)
# eye1
canvas.create_oval(60,30,190,80)
# circle1
canvas.create_oval(100,30,150,80,outline="black",fill="black") 
# # eye2
canvas.create_oval(260,30,390,80)
# # circle2
canvas.create_oval(300,30,350,80,outline="black",fill="black") 
# Nose
canvas.create_oval(200,150,250,200,outline="black",fill="red")
# Mouth
canvas.create_rectangle(100,250,350,260,  outline="red", fill="red")
canvas.create_rectangle(100,215,110,260,  outline="red", fill="red")
canvas.create_rectangle(340,235,350,260,  outline="red", fill="red")
# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()

