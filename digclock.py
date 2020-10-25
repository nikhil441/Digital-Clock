from tkinter import Label, Tk
import time
#Defining the Tkinter function
app_window = Tk()
#Giving title to application window
app_window.title("Digital Time")
#Defining the size of video
app_window.geometry("350x150")
#The window is not resizable, because the text values are not responsive design. And we don’t want our design to look weird when the window size is changed.
app_window.resizable(0,0)
#Label Design
text_font= ("Boulder", 61, 'bold')
background = "blue"
foreground= "grey"
#Colour can be entered in any format of your choice(RGB,Hex,or name)
border_width = 25
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)
digital_clock()
app_window.mainloop()
