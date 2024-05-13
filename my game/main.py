import tkinter as tk
from pyautogui import size
from tkextrafont import Font
import tksvg

# Get screen size
wnx, wny = size()

# Create Tkinter window
wn = tk.Tk()
wn.title("Froggy Engine")
wn.geometry(f"{wnx}x{wny}")
wn.attributes("-fullscreen", True)
wn.configure(background="black")

# Use the Font class
font = Font(file="assets/akrobat/Akrobat-ExtraBold.ttf",family="Akrobat-ExtraBold", size=25)

im = tk.PhotoImage(file="assets/bg.png")
im1 = tk.PhotoImage(file="assets/logo.png")
# Replace the image path with your SVG file path

frame = tk.Label(wn, image=im, width=wnx, height=wny)
frame.place(x=0,y=0)
# Create frame1
frame1 = tk.Frame(wn, bg="black",width=10,height=10)
frame1.pack(anchor=tk.NW,expand=False)

btn1 = tk.Frame(wn, bg="brown", width=300, height=100)
btn1.place(x=wnx/2-100)    # Position the frame using grid

btn = tk.Frame(wn, bg="white", width=450, height=wny-300)
btn.place(x=20,y=240) 

cv = tk.Canvas(wn, bg="white", width=70, height=wny-300)
cv.place(x=515,y=240)

win = tk.Label(wn, bg="white", width=650, height=wny-300)
win.place(x=1240,y=240) 

win.columnconfigure((0, 1), weight=1)
win.rowconfigure((0, 1), weight=1)

cv = tk.Canvas(win, bg="black", width=670, height=wny-700)
cv.grid(row=0,column=0)

text = tk.Canvas(wn, bg="white", width=70, height=wny-300)
text.place(x=515,y=240) 


tr = tk.Text(wn, bg="white", width=25, height=13,font=font)
tr.place(x=600,y=240) 

# Configure frame1
frame1.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
frame1.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1)

# Create label and label1 within frame1
label = tk.Label(frame1, bg="black", image=im1)
label.grid(row=0, column=0)  # Position the label within the frame using grid



# Create frame
# Position the frame at the top of the window



wn.mainloop()
